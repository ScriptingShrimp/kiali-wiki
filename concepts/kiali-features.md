---
title: Kiali Features Overview
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, istio, service-mesh, reference, tracing, configuration, operator]
sources: [raw/articles/kiali-docs-features-index.md, raw/articles/kiali-docs-features-topology.md, raw/articles/kiali-docs-features-health.md, raw/articles/kiali-docs-features-details.md, raw/articles/kiali-docs-features-tracing.md, raw/articles/kiali-docs-features-wizards.md, raw/articles/kiali-docs-features-configuration.md, raw/articles/kiali-docs-features-validations.md, raw/articles/kiali-docs-ai-index.md, raw/articles/kiali-docs-news-release-notes.md]
confidence: high
---

# Kiali Features Overview

Kiali is the observability and configuration console for the Istio service mesh.
This page is the feature map of the standalone Kiali console as of Kiali v2.32.0
(released 2026-09-14), with each section linking to the raw source that covers it
in depth. The same feature set is embedded in [[ossmc]] (OpenShift Service Mesh
Console) and in the Backstage plugin ([[kiali-integrations]]). Deployment options
are in [[kiali-installation]] and the AI surface in [[kiali-ai-chat-and-mcp]].
^[raw/articles/kiali-docs-features-index.md]

## Feature inventory

The official index (kiali.io/docs/features) covers these areas, each with its own
raw page: Application Wizards, Detail Views, Health, Internationalization,
Istio Ambient Mesh, Istio Configuration, Istio Infrastructure Status,
Multi-cluster, Multi-mesh, Security, Topology, Tracing, and Validation. The
sections below summarize the major ones. ^[raw/articles/kiali-docs-features-index.md]

## Topology and the Graph

The default landing page is the mesh **Overview**: a high-level view of clusters,
control planes, data planes, and configuration combining service/app information
with telemetry, validations, and health. The **Namespaces** page (Kiali >= 2.23)
adds filtering, sorting, and presentation options for namespaces. The **Graph**
is the core feature: it combines real-time request traffic with Istio
configuration and offers four graph types:

- **workload** — low-level communication between workloads.
- **app** — workloads aggregated by app label (logical view).
- **versioned app** — app-level, broken out by version.
- **service** — high-level view aggregating all traffic for defined services.

Graph nodes are decorated with route options (virtual services, service entries),
special configuration (fault injection, circuit breakers), and health/error
indicators. A collapsible **side panel** provides charts, health details,
response-code/host breakdowns, and traces for the selection. Double-clicking a
node opens a **node detail graph** (traffic from that node's proxy viewpoint).
Other capabilities: **traffic animation** (HTTP: circles = successful requests,
red diamonds = errors, density = request rate, speed = response time;
TCP = offset circles where speed indicates traffic rate). **Ranking**
(normalizes nodes 1..100 on criteria
such as inbound-edge count, combined with find/hide), **replay** of past
time periods (fully bookmarkable), and **operation nodes** (Istio 1.6+ request
classification, drawn as pentagons; not compatible with service graphs). ^[raw/articles/kiali-docs-features-topology.md]

## Health

Kiali reflects mesh health at several levels: the **Masthead** shows
infrastructure health (including multi-cluster) with color severity and hover
detail; the **Overview dashboard** shows applications grouped by health plus
**Service Insights** (top error-rate and p95-latency services); the **Graph**
colors nodes/edges with a standard orange/red degradation scale and supports
pause and replay. Health is computed by combining indicators; the **global
health of a resource is the most severe of its indicators**. Two indicators
exist: **Pod Status** (not configurable) and **Traffic Health** (configurable).
Statuses are NA / Healthy / Degraded / Failure, and custom request-health
overrides exist for situations where default thresholds misfire (e.g. expected
404s). Health pre-compute/cache was introduced in v2.22 (release notes).
^[raw/articles/kiali-docs-features-health.md] ^[raw/articles/kiali-docs-news-release-notes.md]

## Detail Views

Filtered list and detail pages exist for **Applications, Istio Configuration,
Services, and Workloads**. Each detail page has an **Overview** tab (default):
health, a mini-graph of traffic involving the component, related-component
links, validation info, and an **Action menu** (wizards + actions). Type-specific
tabs: **Traffic** (in/out tables), **Logs** (unified app + Envoy proxy log view
with substring/regex Show-Hide, full-screen, proxy log-level change without pod
restart), **Metrics** (in/out dashboards, customizable dimensions, source- vs
destination-proxy metrics, trace-span overlay), **Traces** (native Jaeger/Tempo),
and **Dashboards** (built-in and custom). ^[raw/articles/kiali-docs-features-details.md]

**Built-in dashboards** are shipped for runtimes that emit Prometheus metrics
(full per-runtime detail in `raw/articles/kiali-docs-features-details.md`):
**Envoy** (most important, five subtabs, applies to any workload with an Envoy
proxy), **Go**, **Node.js**, **Quarkus**, **Spring Boot** (3), **Thorntail**,
**Vert.x** (5), and **Kiali** (self-monitoring). Each is enabled via the pod
annotation `kiali.io/dashboards: <name>`; custom dashboards are also supported.
^[raw/articles/kiali-docs-features-details.md]

## Tracing

Kiali integrates natively with **Jaeger** and **Grafana Tempo**, and correlates
traces with the other observability pillars:

- **Workload detail** — Traces tab with trace/span detail; a **heatmap**
  compares a trace's duration against aggregated metrics (green = faster,
  red = slower).
- **Metric correlation** — span overlays on metric charts (enable `spans`).
- **Graph correlation** — the side panel lists traces for a selected node and
  overlays spans on the graph.
- **Logs correlation** — unified app logs (white), Envoy logs (gold), and trace
  spans (blue) sorted by time; clicking a span jumps to the trace.

Backend endpoints (Jaeger/Tempo) are configured in the Kiali CR under
`external_services.tracing`. ^[raw/articles/kiali-docs-features-tracing.md]

## Application Wizards

Wizards generate Istio config from UI actions, applied to **Services**,
**Workloads**, or **Namespaces**. Service actions: **Request Routing** (multiple
rules; matching on HTTP headers/URI/scheme/method/authority + Routes To
percentage; applied in order, order editable), **Fault Injection** (HTTP delay /
abort), **Traffic Shifting** (percentage routing), **Request Timeouts** (timeout
+ retry), and Advanced **Gateways** (expose via existing/new Gateway),
**Circuit Breaker** (connection pool + outlier detection), **Routing Rules
Preview** (review/edit full YAML before create), and **Security: Traffic Policy**
(TLS, auto PeerAuthentication, load balancing). Workload action: **Automatic
Sidecar Injection** (per workload, propagated into pod template). Namespace
actions: **Show** (navigate to that namespace's graph/apps/workloads/services/
config), **Automatic Sidecar Injection** (namespace label), **Canary Istio
upgrade** (label to a canary revision), **Security: Traffic Policies** (generate
an AuthorizationPolicy per workload to lock down observed traffic).
^[raw/articles/kiali-docs-features-wizards.md]

## Istio Configuration

The Istio configuration view provides filtering and navigation for Istio config
objects (VirtualServices, Gateways, etc.) with **inline editing** and **semantic
validation**. Kiali's validation goes beyond Istio's static checks: it performs
cross-object and (in some cases) cross-namespace semantic validation based on
runtime mesh status. As of **Kiali v2.25**, validation supports **multi-primary
Istio deployments**, including cross-cluster MeshConfig validation.

### Configuration wizards

From the Istio Config page: **AuthorizationPolicy** (selector, action ALLOW /
DENY / AUDIT / CUSTOM, rules, provider), **PeerAuthentication** (selector,
mTLS mode UNSET/DISABLE/PERMISSIVE/STRICT, port-level overrides),
**RequestAuthentication** (selector, JWT rules), **Gateway** (Istio),
**ServiceEntry**, **Sidecar**, **K8s Gateway** (Gateway API v1.5.0+), and
**K8s ReferenceGrants** (cross-namespace routing grants). From the Namespaces
page (>= 2.23) and Service Detail: traffic-policy and routing-rule wizards.

### AI-assisted configuration

Since Kiali v2.22, Istio configuration can also be created and managed through
the **AI Chatbot** (dev preview) using natural-language prompts — see
[[kiali-ai-chat-and-mcp]]. ^[raw/articles/kiali-docs-features-configuration.md]

## Validations

Kiali ships ~73 semantic validation rules, namespaced by resource type (KIA0xxx)
— full list with resolution, severity, and examples in
`raw/articles/kiali-docs-features-validations.md` (2,679 lines, not reproduced).
Coverage spans these categories:

| Category | Codes | | Category | Codes |
|---|---|---|---|---|
| AuthorizationPolicy | KIA0101–0110 | | Telemetry | KIA1201+ |
| DestinationRules | KIA0201+ | | ServiceEntries | KIA1301+ |
| Gateways | KIA0301+ | | K8s Routes | KIA1401+ |
| Mesh policies | KIA0401+ | | Workloads | KIA1501+ |
| PeerAuthentication | KIA0501+ | | Ambient Workloads | KIA1601+ |
| Ports | KIA0601+ | | Generic | KIA1701+ |
| Services | KIA0701+ | | K8s Gateway | KIA1801+ |
| Sidecars | KIA0801+ | | K8s ReferenceGrants | KIA1901+ |
| VirtualServices | KIA0901+ | | Workload Groups | KIA2001+ |
| RequestAuthentication | KIA1001+ | | WasmPlugin | KIA1101+ |

Rules can be **disabled globally** (`kiali_feature_flags.validations.ignore:
[KIA0106]`) or **ignored per object** (annotation `kiali.io/ignore-validations` —
empty value ignores all, comma-separated codes ignore specific); ignored rules are
still logged but hidden from the UI. The reconcile interval can be set to `0s` to
disable validation on very large / resource-constrained clusters.
^[raw/articles/kiali-docs-features-validations.md]

## Ambient, multi-cluster, multi-mesh, security

The feature index also covers **Istio Ambient Mesh** (ztunnel / waypoint /
ambient policy), **Multi-cluster** (observe multiple clusters), **Multi-mesh**
(multiple Istio meshes in one cluster), and **Security** (mTLS visualization).
Each has its own documentation section; this note keeps them on the map only.
^[raw/articles/kiali-docs-features-index.md]

## AI features

Kiali's AI surface (chatbot, MCP tools, AI-assisted config) is documented on
its own page: [[kiali-ai-chat-and-mcp]]. The AI section was added to the
kiali.io docs in 2026 (kiali.io docs commit #955, March 2026); the chatbot
itself shipped in Kiali v2.22.0 as a Dev Preview. ^[raw/articles/kiali-docs-ai-index.md]

## Where to go next

- [[kiali-ai-chat-and-mcp]] — AI Chatbot, MCP tools, Kiali MCP server.
- [[ossmc]] — the OpenShift Console plugin that embeds the same features.
- [[kiali-installation]] — how to install any of this.
- [[kiali-integrations]] — Backstage plugin, ecosystem integrations.
- [[kiali-operator]] — the operator that deploys all of the above.
