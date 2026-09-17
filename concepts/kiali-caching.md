---
title: Kiali Caching
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, caching, architecture]
sources:
  - raw/articles/kiali-doc-auth-and-security.md
  - raw/articles/kiali-repo-cache.md
  - raw/articles/kiali-kep-multi-session-auth.md
  - raw/articles/kiali-kep-graph-cache.md
  - raw/articles/kiali-doc-STATUS.md
confidence: high
---

# Kiali Caching

From `CACHE.md` (master, ingested 2026-09-17) plus the graph-cache design:

### Layer 1 — Kiali cache (`cache/`)

Mesh metadata for UI responsiveness: mesh-wide config (control planes
discovered from ConfigMaps, istiod env vars, etc.), ambient-mode flag, build
info, known cluster list, **Istio validation results per cluster/namespace**,
namespaces per cluster, **proxy (xDS) status**, service registry data, waypoint
workload data, webhook availability, ztunnel config dumps, ztunnel pod list.
^[raw/articles/kiali-repo-cache.md]

### Layer 2 — Kubernetes cache

Controller-runtime informer caches (per cluster, built at startup, see
[[kiali-architecture]]) for: ConfigMaps; workloads (DaemonSets, Deployments,
Pods, ReplicaSets, StatefulSets, Endpoints); Services; Istio resources
(DestinationRules, EnvoyFilters, Gateways, Sidecars, ServiceEntries,
Telemetries, TrafficExtensions, VirtualServices, WasmPlugins, WorkloadEntries,
WorkloadGroups); security (AuthorizationPolicies, PeerAuthentications,
RequestAuthentications); Gateway API (Gateways, GRPCRoutes, HTTPRoutes,
ReferenceGrants, TCPRoutes, TLSRoutes).

**Never cached — fetched live from the K8s API**: CronJobs,
DeploymentConfigs, Jobs, ReplicationControllers.
^[raw/articles/kiali-repo-cache.md]

### Layer 3 — Prometheus cache

Request-rate metrics per cluster/namespace: app, service, workload request
rates. (Graph traffic data is *not* this — see the session-scoped graph cache
in [[kiali-graph-engine]].) ^[raw/articles/kiali-repo-cache.md]

### Layer 4 — Tempo cache

Cached traces from Tempo for trace-analysis performance.
^[raw/articles/kiali-repo-cache.md]

### Layer 5 — graph cache

Per-session in-memory namespace-graph cache with background refresh (full
mechanics, config keys, and the security rationale for per-session keying in
[[kiali-graph-engine]]; design origin: Graph Cache KEP, shipped; builds on the
still-open Controller Model KEP). ^[raw/articles/kiali-kep-graph-cache.md]

### Cross-cutting design notes

- **Read model & RBAC**: most *reads* in the backend run with the Kiali SA
  (informer caches, broad scope); the user's token is used for login
  validation, writes, and namespace-scope enforcement (allowed-namespace list
  checked against requested resources). This split is why the graph cache and
  session cookies are keyed per session and why the `isInaccessible` graph
  metadata exists — caching can never be a bypass of RBAC (an explicit
  graph-cache KEP non-goal). ^[raw/articles/kiali-kep-multi-session-auth.md]
  ^[raw/articles/kiali-kep-graph-cache.md]
- **Secrets never enter the conversation**: token/CA rotation, audit logging,
  and the CA-bundle trust store are all file/Secret-backed (see
  CredentialManager); credentials for external services live in the Kiali CR /
  `kiali-secret`, not in wiki or chat.
- **Degrade, don't die**: Prometheus unreachable → `NoopClient` +
  `DisabledReason`; tracing init async; CA-pool failure → system CAs + watcher.
  ^[raw/articles/kiali-doc-backend-architecture.md]
  ^[raw/articles/kiali-doc-auth-and-security.md]

## Related pages

- [[kiali-auth-and-caching]] — the authentication strategies and session model
- [[kiali-architecture]] — backend startup, middleware, client factory
- [[kiali-graph-engine]] — the per-session graph cache and its request flow
- [[kiali]] — project, releases, governance

## Open questions / watch items

- Multi-session auth KEP: 2 of 6 roadmap items done as of the 2026-09-17
  ingest; mesh-cluster-only login (no mgmt-cluster creds) is an open TODO in
  the OpenShift controller.
- 2.31.0 shipped an OpenID/Keycloak logout fix and 2.30.0 shipped OpenShift
  impersonation for multi-cluster auth — auth behavior is actively moving;
  re-verify against the release notes before writing operator runbooks.
  ^[raw/articles/kiali-docs-news-release-notes.md]
