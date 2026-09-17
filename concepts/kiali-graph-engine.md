---
title: Kiali Graph Engine
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, architecture, backend, graph, prometheus, istio, caching, ambient, service-mesh]
sources:
  - raw/articles/kiali-doc-graph-engine.md
  - raw/articles/kiali-kep-graph-cache.md
  - raw/articles/kiali-docs-features-topology.md
  - raw/articles/kiali-doc-STATUS.md
confidence: high
---

# Kiali Graph Engine

The traffic graph is Kiali's central feature: a visualization of **actual**
traffic flowing through the mesh at query time, enriched with Istio
configuration, health, security policy, and Ambient/waypoint topology.
^[raw/articles/kiali-docs-features-topology.md] All engine code lives under
`graph/`; the Istio telemetry implementation under `graph/telemetry/istio/`.
^[raw/articles/kiali-doc-graph-engine.md]

Per-request pipeline (namespace graph): (1) parse HTTP params into a typed
`Options` struct; (2) query Prometheus for raw Istio telemetry
(`istio_requests_total` + related); (3) build a `TrafficMap` (directed graph
of typed nodes/edges); (4) run the ordered `Appender` pipeline (health,
mTLS, Istio config, Ambient/waypoint, labels, ...); (5) convert `TrafficMap`
to the serialisable config format (`graph/config/common`); (6) cache the
result per browser session and refresh it in the background (see
[[kiali-graph-cache]] below). ^[raw/articles/kiali-doc-graph-engine.md]

> Source note: the graph-engine deep-dive was reviewed
> `PASS_WITH_ANNOTATIONS` (2026-05-26 scribe scan) — one annotation was a
> Prometheus counter-name fix (`kiali_graph_cache_evictions_total`, not
> `graph_cache_evictions_total`), already reflected here.
> ^[raw/articles/kiali-doc-STATUS.md]

## Data model (`graph/types.go`)

- **`TrafficMap`** = `map[string]*Node`; node IDs are deterministic strings
  derived from identity (cluster + namespace + workload/app/version/service +
  graph type), computed by `NewNode(...)`.
- **`Node`** fields: `ID`, `NodeType` (`app`|`service`|`workload`|`box`|
  `aggregate`|`unknown`), `Cluster`, `Namespace`, `Workload`, `App`,
  `Version`, `Service`, `Edges []*Edge`, `Metadata` (open-ended enrichment).
  Fields are trimmed per type (service nodes drop app/workload/version;
  workloads with `Unknown` labels get them cleared).
- **`Edge`** = `{Source, Dest *Node; Metadata}` — carries protocol, response
  codes, rates, security metadata.
- **Sentinels**: `BlackHoleCluster`/`PassthroughCluster` (Envoy internal
  clusters, flagged `isEgressCluster`); `Unknown` for traffic whose
  source/dest labels Istio could not resolve.

^[raw/articles/kiali-doc-graph-engine.md]

### Metadata keys (selection, `graph/meta.go`)

Typed constants, e.g.: `isAmbient`, `isDead`, `isEgressGateway`,
`isIngressGateway`, `isGatewayAPI`, `isIdle`, `isInaccessible` (outside the
caller's RBAC scope), `isMTLS`, `isOutOfMesh`, `isOutside`, `isRoot`,
`isServiceEntry`, `isWaypoint`, `hasCB`, `hasFaultInjection`, `hasMirroring`,
`hasTrafficShifting`, `hasVS`, `hasWorkloadEntry`, `healthData`/`healthStatus`,
`labels`, `responseTime`, `throughput`, `sourcePrincipal`/`destPrincipal`.
Edge keys add `protocol`, `responseTime`, `throughput`, `isMTLS`,
`destServices`. ^[raw/articles/kiali-doc-graph-engine.md]

## Options (`graph/options.go`)

`Options{ConfigVendor (default "common"), TelemetryVendor (default "istio"),
ConfigOptions, TelemetryOptions}`. Key `TelemetryOptions` defaults:
`Duration` 10m (Prometheus look-back), `GraphType` `workload`
(`workload`|`app`|`versionedApp`|`service`), `QueryTime` now, `Namespaces`,
`IncludeIdleEdges`/`InjectServiceNodes` false, `Rates.{Http,Grpc,Tcp,Ambient}`,
`BoxBy` `none` (`app`|`cluster`|`namespace`), `Appenders` (all by default, or
a comma-separated subset), `SessionID` (browser session value -> cache key),
`RefreshInterval`. `NewOptions(r, business, conf)` parses everything from path
vars + query params; `NodeOptions` drives the single-node detail graph.
^[raw/articles/kiali-doc-graph-engine.md]

## Telemetry pipeline

Entry: `graph/api/api.go` — `GraphNamespaces(ctx, business, prom, o)` and
`GraphNode(ctx, business, prom, o)` are the two functions the HTTP handlers
call; both route to `graph/telemetry/istio/istio.go` for the Istio vendor.
`BuildNamespacesTrafficMap` (package comment, verbatim): per namespace, query
Prometheus for source->destination dependencies and build a namespace-level
`TrafficMap`; apply namespace-scoped appenders (non-finalizers); merge the
namespace map into the global map. Then, for the global map, apply finalizer
appenders to the complete graph and convert to the requested config format
(Common) and return. For `graphType == "service"`,
`telemetry.ReduceToServiceGraph()` condenses the final map.
`MergeTrafficMaps` (`graph/telemetry/common.go`) prefers the namespace-local
copy of duplicate nodes (already appender-decorated) and dedupes edges. If
`Rates.Ambient != "none"`, a waypoint lookup (`GetWaypointMap()`) is built
before querying namespaces so the `AmbientAppender` finalizer can model
waypoint-routed traffic. ^[raw/articles/kiali-doc-graph-engine.md]

### Prometheus queries

Per namespace, `buildNamespaceTrafficMap` fires up to **four** instant-vector
queries on `istio_requests_total` (gRPC via `istio_*_messages`), grouped by
the full Istio telemetry label set (`source_cluster` ... `response_flags`,
incl. `request_protocol`, `response_code`, `grpc_response_status`): (0)
incoming **source** telemetry — failed requests that never reach a
destination workload (unserviced services); (1) incoming **Ambient source**
telemetry (Ambient namespaces only) — traffic from non-waypoint ingress
gateways missing from destination telemetry; (2) incoming **destination**
telemetry — the primary query; (3) outgoing **source** telemetry — traffic
leaving the namespace. The `source`/`destination` `reporter` label is chosen
by `util.GetReporter(side, rates)`; TCP uses
`istio_tcp_sent/received_bytes_total` with the same structure.
`populateTrafficMap` turns each series into nodes/edges; a SHA-256 hash of
each series' label set (`tsHash`) is stored in node metadata so refreshes can
detect changed telemetry. ^[raw/articles/kiali-doc-graph-engine.md]

## Appender pipeline

```go
type Appender[T any] interface {
    AppendGraph(ctx, trafficMap, globalInfo *GlobalInfo[T], namespaceInfo)
    IsFinalizer() bool   // true = runs once on the final merged graph
    Name() string        // selectable via query param
}
```

`GlobalInfo[T]` carries the business layer, Prometheus client, config,
cluster list, and the vendor struct (`*GlobalIstioInfo`), which caches
shared data (waypoint keys, app maps by `cluster:namespace`, service-entry
hosts, service/workload lists/maps) so appenders do not re-query.

- **Namespace-scoped order** (per namespace, in order): `ServiceEntryAppender`
  -> `DeadNodeAppender` (removes traffic-less, workload-less nodes early)
  -> `WorkloadEntryAppender` -> `ResponseTimeAppender`
  (`istio_request_duration_milliseconds` histograms -> p50/p95/p99/avg)
  -> `SecurityPolicyAppender` (mTLS `connection_security_policy` -> `isMTLS`
  + principals) -> `ThroughputAppender` -> `AggregateNodeAppender` (default
  attribute `request_operation`) -> `IdleNodeAppender` (service-type graphs
  with `injectServiceNodes` only) -> `MeshCheckAppender` (legacy alias
  `sidecarsCheck`).
- **Finalizers** (once, on the merged graph): `ExtensionsAppender` (always
  first; external extension nodes/edges) -> `OutsiderAppender` (always runs;
  `isOutside`/`isInaccessible`) -> `IstioAppender` (`hasVS`/`hasCB`/fault
  injection) -> `AmbientAppender` (re-wires edges to surface waypoint nodes)
  -> `HealthAppender` (after `OutsiderAppender` so inaccessible nodes are
  skipped) -> `LabelerAppender` -> `TrafficGeneratorAppender` (always last).

Users may request a subset via the `appenders` query param (`deadNode`,
`responseTime`, `securityPolicy`, `meshCheck`, ...); `ExtensionsAppender`,
`OutsiderAppender`, and `TrafficGeneratorAppender` always run regardless.
^[raw/articles/kiali-doc-graph-engine.md]

## Graph caching & background refresh

Kiali caches **only namespace graphs** (node-detail graphs are always
generated fresh), per browser session keyed by `SessionID`, and refreshes each
session's graph in the background via a per-session `RefreshJob` goroutine with
LRU eviction under a memory cap. The design, config keys, request flow, and
the `GraphCacheImpl`/`RefreshJob` mechanics live in [[kiali-graph-cache]].

## API entry point & Prometheus client

`graphNamespacesIstio` (behind `GraphNamespaces`): cluster list from
`business.Mesh.Clusters()` -> build `GlobalInfo` ->
`istio.BuildNamespacesTrafficMap` -> `generateGraph` (the config vendor's
`NewConfig()` produces the serialisable payload). The Prometheus side is
`prometheus/client.go`: a `Client` wrapping `prom_v1.API` (instant + range),
a `QueryRecorder` (logs queries/results to a file — powers `kiali gather`),
`ClientInterface` as the shared abstraction, and a no-op client for tests.
`graph.PromQuery` wraps `promApi.Query()` with error handling that panics
with a structured `graph.Error`, caught at handler level -> HTTP 500.
^[raw/articles/kiali-doc-graph-engine.md]

## User-facing surface (kiali.io docs)

The UI exposes graph types (workload/app/service/versioned-app), health
coloring of nodes and edges, find/hide, traffic animation, pausing, and
**replay** of past time windows (exactly what the `queryTime` cache-bypass
serves). The mesh Overview (default landing page, multi-cluster aware) and
the Namespaces page (Kiali >= 2.23) are the entry points.
^[raw/articles/kiali-docs-features-topology.md]

## Related pages

- [[kiali]] — project overview, releases (2.32.0 graph-cache/health work)
- [[kiali-architecture]] — where the graph handler sits in the backend
- [[kiali-auth-and-caching]] — session IDs, other Kiali caching layers
- [[kiali-graph-cache]] — the per-session graph cache & background refresh

## Open questions / watch items

- The 2.32.0 release notes include "AI: Mesh traffic graph health should use
  cached health Status" — the HealthAppender/health-cache interaction is
  moving; re-check `raw/articles/kiali-docs-news-release-notes.md` before
  documenting health-appender behavior in detail.
- Appender ordering and query-param names are contract for frontend and
  extension authors; verify against `graph/appender.go` on current master
  before writing an extension.
