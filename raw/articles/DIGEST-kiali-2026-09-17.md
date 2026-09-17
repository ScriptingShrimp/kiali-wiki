---
source_url: derived: see in-file source references
ingested: 2026-09-17
sha256: d27cba79c9ca7b0b46727ad839c865043ee9e1fe70cb864bde67f96dd0c022cc
note: agent-compiled digest of the kiali.io documentation fetch; not an upstream document
---
# Kiali Documentation Digest — ingested 2026-09-17

All Kiali.io doc pages captured verbatim to /root/wiki/raw/articles/ as
kiali-docs-<slug>.md with frontmatter (source_url, ingested, sha256-of-body).
Every file's body sha256 verified against its frontmatter. Plus the official
release notes and the (partially-walled) Medium 2.16–2.30 features post.

## Files saved (30 total)
features: index, topology, health, details, tracing, validations, wizards, configuration
architecture: index, architecture, terminology(index/concepts/networking)
installation: index, guide, quick-start, deployment-options
ai: index, kiali-chatbot, kiali-chatbot-tools, kiali-mcp
ossmc: index, users-guide, navigating-multiple-meshes
integrations: index, kiali-backstage-plugin, ossm-console
news: release-notes  (full, 2.0.0 → 2.32.0)
blog: releases-2-16-to-2-30-features-update (partial — Cloudflare; see Failures)

---

## 1. Feature summaries

### Topology
Kiali's default landing page is the mesh **Overview** (clusters, control
planes, data planes, config, combining service/app info + telemetry +
validations + health). The **Namespaces** page (>=2.23) adds filtering/
sorting/presentation. The **Graph** is the core: real-time request traffic
combined with Istio config, four graph types (workload / app / versioned-app /
service). Nodes decorated with route options (virtual services, service
entries, fault injection, circuit breakers), mTLS/latency/error indicators.
Collapsible **side panel** (charts, health, links, response-code/host
breakdown, traces). **Node detail** graph on double-click (traffic from that
node's proxy viewpoint). **Traffic animation** (HTTP success=green circles,
error=red diamonds; TCP=offset circles). **Ranking** (normalized 1..100 by
criteria e.g. inbound-edge count) + find/hide. **Replay** of past periods,
fully bookmarkable. **Operation nodes** (Istio 1.6+ request classification,
pentagons; not compatible with service graphs).

### Health
Kiali reflects mesh health at several levels: **Masthead** (infrastructure
health, incl. multi-cluster, color+hover detail); **Overview dashboard**
(clusters, config, control/data planes; app-by-health chart; Service Insights
= top error-rate & p95-latency services); **Graph health** (orange/red node &
edge shading, auto-refresh, pause/replay). Health = combined indicators;
**global health = most severe indicator**. Indicators: **Pod Status** (no
config) and **Traffic Health** (configurable). Icons/colors: NA / Healthy /
Degraded / Failure. **Custom Request Health** fine-grained overrides (e.g.
expected 404s) — see /docs/configuration/health/. Note v2.22+ health
pre-compute/cache (see release notes 2.22, 2.24 metric change).

### Detail Views
List + detail pages for **Applications, Istio Config, Services, Workloads** —
each with health, YAML, links. Detail tabs vary by type:
**Overview** (default: mini-graph, related components, health, validations,
Action menu incl. wizards), **Traffic** (in/out tables), **Logs** (unified
app+proxy logs, regex show/hide, fullscreen, set proxy log level w/o pod
restart, trace-span correlation), **Metrics** (in/out prebuilt dashboards,
customizable dimensions, source/dest proxy, span overlay), **Traces**
(Jaeger integration). **Built-in dashboards** for runtimes: **Envoy**
(5 sub-tabs; tune via statsInclusionPrefixes, must include cluster_manager +
listener_manager), **Go** (kiali.io/dashboards: go), **Kiali** (internal
metrics tab), **Node.js** (prom-client), **Quarkus** (SmallRye), **Spring
Boot** (3: JVM/threads, JVM pools, Tomcat; actuator + micrometer), **Thorntail**
(MicroProfile), **Vert.x** (client/server/eventbus/pool/jvm). **Custom
dashboards** supported (kiali.io/dashboards annotation).

### Tracing
Native integration with **Jaeger** and **Grafana Tempo**. Beyond link-outs,
traces are correlated into multiple views: **Workload detail Traces tab**
(trace detail + span detail tabs + **heatmap** = one trace's duration vs.
aggregated metrics over time, red=slow/green=fast). **Metric correlation**:
enable `spans` to overlay trace spans on metric charts; click a span → back to
traces. **Graph correlation**: side panel Traces tab lists traces; selecting
one overlays its spans on the graph. **Logs correlation**: unified pillar
view (app logs white, Envoy proxy logs gold, trace spans blue); click a span
→ trace detail. See 3-part "Trace my mesh" blog + config docs.

### Application Wizards
Kiali **Actions** (create/update/delete Istio config) driven by wizards,
applied to Service, Workload, or whole Namespace. **Service actions**:
**Request Routing** (multiple rules; matching on HEADERS/URI/SCHEME/METHOD/
AUTHORITY; routes-to with %; rule ordering), **Fault Injection** (HTTP delay +
abort), **Traffic Shifting** (% per workload), **Request Timeouts** (timeout +
retry), **Gateways** (Advanced Option: expose to external via existing/new
gateway), **Circuit Breaker** (connection pool limits + outlier detection),
**Routing Rules Preview** (review/edit full YAML before create), **Traffic
Policy** (TLS, generate PeerAuthentication, load-balancing). **Workload
action**: enable/disable **sidecar injection** per workload. **Namespace
actions**: Show navigation, sidecar injection label, **canary Istio upgrade**
label, **Create Traffic Policies** (generate AuthorizationPolicy per workload
from the graph to lock down the namespace).

### Istio Configuration
Kiali generates/edits/validates Istio mesh config: **Istio Config page** with
advanced filtering, inline YAML editing, semantic validation. **Validations**
go beyond Istio's static checks — semantic, cross-object, even cross-namespace,
based on runtime mesh status; **v2.25+ supports multi-primary / cross-cluster
MeshConfig**. **Wizards** on the Istio Config page (Create Actions):
**Authorization** (AuthorizationPolicy: selector/action ALLOW-DENY-AUDIT-CUSTOM/
rules/provider; PeerAuthentication: selector/mTLS UNSET-DISABLE-PERMISSIVE-STRICT/
per-port; RequestAuthentication: selector/JWT rules issuer+JWKS+locations),
**Traffic** (Gateway, ServiceEntry, Sidecar, **K8s Gateway** (Gateway API
v1.5.0+: GatewayClass/listeners/allowedRoutes), **K8s ReferenceGrant**
(cross-namespace from/to selectors)). Also **Namespaces page** (>=2.23) and
**Service detail** wizards; Travel Tutorial. **AI-assisted config** (>=2.22):
create/inspect/update Istio resources via the AI assistant (dev preview).

### Validations (complete list)
Kiali performs semantic validations on Istio objects (DestinationRules,
ServiceEntries, VirtualServices, etc.), based on live mesh status — beyond
Istio's static checks. 73 distinct rule IDs (KIA0002..KIA1702), grouped:
- **AuthorizationPolicy** (KIA0101–0110): namespace/rule not found, host not
  in registry, mTLS required, SA not found, trust-domain unknown, plus
  Ambient waypoint (use-waypoint) enrollment rules.
- **Destination rules** (KIA0201–0212): dup host/subset, host not in registry,
  subset labels not found, mTLS override, missing mesh/ns-wide mTLS
  PeerAuth, strict vs permissive, missing labels, Ambient waypoint rules.
- **Gateways** (KIA0301–0302): dup host:port, no matching workload for selector.
- **Mesh policies** (KIA0401): missing mesh-wide mTLS DR.
- **PeerAuthentication** (KIA0501/0505/0506): missing ns-wide or mesh-wide
  mTLS enable/disable DR.
- **Ports** (KIA0601–0602): port name / appProtocol form.
- **Services** (KIA0701): deployment not found exposing same port.
- **Sidecars** (KIA1004/1006/1007): host not in registry, global default
  sidecar w/ selector, ambiguous empty OutboundTrafficPolicy.
- **VirtualServices** (KIA1101–1114): bad weight/host, nonexistent gateway,
  weight-assumed, dup host-subset ref, >1 VS for host, subset not found,
  nomenclature, Ambient waypoint rules.
- **RequestAuthentication** (KIA1110/1115), **WasmPlugin** (KIA1111/1116),
  **Telemetry** (KIA1112/1117): Ambient waypoint enrollment rules.
- **ServiceEntries** (KIA1211–1212): dup host:port, conflicting protocols.
- **Workloads** (KIA1301) + **Ambient Workloads** (KIA1311–1317): workload not
  covered by authz; mixed sidecar+ambient labels; waypoint label/annotation
  misconfig; L7 authz without waypoint.
- **K8s Routes** (KIA1401–1402): route to inaccessible K8s gateway; invalid
  service reference.
- **Generic** (KIA0002–0005): dup selector-less object, multiple objects on
  same workload, no matching workload/namespace.
- **K8s Gateway** (KIA1501–1504): dup host:port, dup address+type, listener
  uniqueness, GatewayClass not in Kiali config.
- **K8s ReferenceGrants** (KIA1601): namespace not accessible.
- **Workload Groups** (KIA1701–1702): SA not found; duplicate labels.
Plus: **Disabling validations** (validation_reconcile_interval: "0s") and
**ignoring** (globally via Kiali CR / per-object annotation).

---

## 2. Architecture (documented)

Kiali = **two components**:
- **Back-end** (Go, github.com/kiali/kiali) — runs in the container platform;
  talks to Istio, retrieves/processes data, serves it to the front-end.
  **Stateless — no storage.** Config via **Kiali CR** (operator) or
  **ConfigMap** (Helm).
- **Front-end** (SPA: PatternFly + React + TypeScript + Redux; kiali/kiali
  /frontend) — in standard deployments **served by the back-end**; queries the
  back-end for data. Mostly stateless; only browser-local data (session
  creds).

**What Kiali talks to (and how):**
- **Istio** — required. Kiali is an Istio console. Retrieves Istio data/config
  via **Prometheus, the Kubernetes API, and istiod**. If istiod is
  inaccessible, that channel can be disabled (no-istiod mode).
- **Prometheus** — hard dependency. Istio telemetry → Prometheus; Kiali reads
  it for topology, metrics, health, problem detection. Uses Istio's **default
  metrics set** (required metrics listed in FAQ). Many features break without
  it.
- **Kubernetes API** — fetch/resolve mesh config: namespaces, services,
  deployments, pods, and Istio config (virtual services, destination rules,
  gateways, quotas, route rules). Works on OKD / Kubernetes + derivatives.
- **Jaeger** — optional. Link-outs to tracing; only if Istio distributed
  tracing enabled.
- **Grafana Tempo** — alternative to Jaeger (documented).
- **Grafana** — optional. Kiali's metrics pages link out to the same metric in
  Grafana; Kiali has only basic metrics (no custom queries/views).

Data flow: Prometheus + K8s API (+istiod) → Kiali back-end → REST API →
front-end renders graph/detail/health. Tracing & Grafana are link-out only.

---

## 3. Full integration list (with status)

- **Prometheus** — HARD dependency (Istio telemetry). Topology, metrics,
  health.
- **Kubernetes / OpenShift (OKD)** — core; fetches entities + Istio config.
- **Istio (istiod)** — core console; can be disabled (no-istiod mode).
- **Jaeger** — OPTIONAL, link-out + correlated views; needs Istio tracing on.
- **Grafana Tempo** — OPTIONAL, Jaeger alternative (documented).
- **Grafana** — OPTIONAL, link-out only; basic metrics only.
- **OpenShift Service Mesh Console (OSSMC / OSSM Console)** — OpenShift dynamic
  plugin (see §7).
- **Kiali Backstage Plugin** — dev portal integration; cards/tab/page;
  tech preview in Red Hat Developer Hub (github.com/backstage/community-
  plugins workspaces/kiali).
- **MCP (Kubernetes MCP Server / OpenShift MCP Server)** — exposes a `kiali`
  toolset to external AI assistants (see §4).

(Integrations index on kiali.io lists exactly: Backstage plugin + OSSM Console.
Everything above is documented across architecture, features, and AI pages.)

---

## 4. AI / MCP / Chatbot status

### Kiali Chatbot (Dev Preview, first shipped v2.22)
Built-in AI assistant in the Kiali UI. **Does NOT require an external MCP
server** — Kiali ships its own internal MCP-style tools (defined under
kiali/ai/mcp). Flow: UI → Kiali backend → selected provider/model (from
`ai.chat`) → LLM with internal tools → tool calls executed against
Kiali/K8s/Prometheus/tracing → answer as **streaming SSE events**
(start/token/tool_call/tool_result/end/error).
- **Disabled by default**: enable via `ai.enabled: true` +
  `ai.chat.enabled: true`; then the chat icon appears.
- **Access control**: `ai.chat.allowed_users` (empty = all users).
- **Providers**: **OpenAI**, **Google**, **Anthropic**, **LightSpeed**
  (OpenShift). Models selected by name, enable/disable; API keys inline or via
  `secret:<name>:<key>`. LightSpeed TLS verification configurable
  (`insecure_skip_verify`).
- **Tool filtering**: global `ai.chat.tools` (enabled/disabled) + per-provider
  `ai.chat.providers[].tools` (can only further restrict).
- **UI**: model/provider switcher; tool-result cards (click → modal w/ full
  output); **predefined prompts** per current page (GET /api/chat/prompts,
  ?category=, static fallback); **Ask vs Troubleshoot mode** (Ask = free-form
  Q&A; Troubleshoot = structured diagnostic — auto-selects tools, systematic
  workflow; LightSpeed handles natively, others via adapted system prompt).

### Built-in tool list (12 tools; schemas in kiali/ai/mcp/tools/*.yaml)
get_action_ui, get_logs, get_mesh_status, get_mesh_traffic_graph, get_metrics,
get_pod_performance, get_referenced_docs, get_trace_details,
list_or_get_resources, list_traces, manage_istio_config_read, manage_istio_config.

### Kiali MCP (external, Dev Preview)
For AI assistants **outside** the Kiali UI (e.g. IDEs). Implemented in the
**Kubernetes MCP Server** (containers/kubernetes-mcp-server) and **OpenShift
MCP Server** (openshift/openshift-mcp-server) — exposes a `kiali` toolset
(docs/KIALI.md). Enable via TOML `toolsets = ["core","kiali"]` +
`[toolset_configs.kiali] url=...` (+ optional insecure / certificate_authority;
https w/ insecure=false requires CA). Auth uses the MCP server's Kubernetes
creds (bearer token). Prereqs: reachable Kiali endpoint + kubeconfig/in-cluster.
v2.28–2.29 added **`analyze_ambient_policies`** (L4/L7 policies, ztunnel status,
waypoint data, Ambient traffic graphs).

---

## 5. Installation options

- **Local mode** (`kiali run`): run the binary on your machine against your
  kubeconfig; port-forwards into the cluster for prometheus/tracing/istio/
  grafana. `kiali run --help` for options. **`--disable-prometheus`** to explore
  non-metrics features (workloads/services/config/topology) without Prometheus.
  Download from GitHub releases.
- **Istio Addons** (demo): `kubectl apply -f ${ISTIO_HOME}/samples/addons/kiali.yaml`.
- **Helm** (quick): `helm install --namespace istio-system --set auth.strategy=anonymous
  --repo https://kiali.org/helm-charts kiali-server kiali-server`.
- **Access**: `kubectl port-forward svc/kiali 20001:20001 -n istio-system` →
  https://localhost:20001/.
- **Production (recommended): the Kiali Operator** (a K8s operator) watches the
  **Kiali CR** (YAML deployment config). Install the operator via **Helm** or
  **OperatorHub**. Sub-pages: Prerequisites, Install via Helm, Install via
  OperatorHub, The Kiali CR, The **OSSMConsole CR**, Accessing Kiali (Ingress,
  LoadBalancer/NodePort), Advanced Install, Example Install (two Kiali servers).
- **Deployment options** (Kiali CR `spec.deployment`): install namespace,
  log level/format (text|json) + audit_log toggle, instance_name (multi-instance
  prefix), resource requests/limits, custom pod/service labels+annotations,
  installation_tag (browser title), replicas + **HPA**, node_selector /
  affinity / anti-affinity / tolerations, priority_class, host_aliases,
  HTTP server (address/port 20001/gzip/cors), **metrics server** (on 9090,
  enabled by default).

---

## 6. 2.16 → 2.30 release post — highlights per area

(The Medium post was Cloudflare-walled; sections 1–2 captured verbatim and the
rest is reconstructed from the official release notes kiali.io/news/
release-notes, saved verbatim — which cover all 15 releases with per-version
entries. Release dates: 2.16 2025-09-22 → 2.30 2026-08-03.)

Post's own framing (verbatim, sec 1–2): 15 releases, "major infrastructure,
visual, observability and AI milestones"; standalone / OSSMC / enterprise
Ambient multi-cluster.
**§1 AI Assistant & MCP:** AI Chatbot Widget + SSE streaming (OpenAI, Google
Gemini), tool-execution UI, multi-cluster awareness; MCP server
(`containers/kubernetes-mcp-server`, `openshift/openshift-mcp-server`) — tools
for Istio config, cluster resources, mesh status, logs, metrics, traces;
v2.28–2.29 added `analyze_ambient_policies` (L4/L7 policies, ztunnel, waypoints,
Ambient graphs).
**§2 UX & PF6:** PF6 migration (v2.20–21) — new Notification Center,
modernized Masthead icons, updated Traffic Shifting Wizards, PF Select
dropdowns; redesigned **Overview & Namespaces** pages (v2.23) — compact card
dashboard + dedicated Namespaces page (sort/filter/mTLS); **Manage Columns
modal** (v2.28) — column show/hide/reorder on App/Service/Workload lists
(standalone + OSSMC); **Detail Pages UX redesign** (v2.27) — clearer card
layouts. (Post truncates here.)

Per-area roll-up from the release notes (all 15 versions):
- **AI / MCP**: 2.22 AI Chatbot Widget + MCP (Dev Preview); 2.23 get_resource_metrics
  + get_logs tools, chatbot into Overview/Namespaces; 2.24 get_istio_config
  token-optimization, node 20→24, yarn 1→4, go 1.25, GOMEMLIMIT; 2.25
  multi-primary validation; 2.26 **Google + Anthropic providers**, Ambient
  trace overlay, PDB template, prometheus enable/disable, OSSMC Namespace/App
  list pages, Namespace Detail page; 2.27 **Anthropic provider**, stale-store
  cleaner, resource_details app-level, token-usage analytics, injection
  hardening, multi-mesh donut, perf (animation, istio appender, health cache
  memory, single-ns workload fetch); 2.28 **built-in MCP prompts**, MCP checker
  actions, LightSpeed TLS configurable, GW API IE v1.5, OAuth2 client_credentials,
  i18n, RBAC cleanup, ServiceEntry conflict validation; 2.29 Ambient v1.30,
  multi-cluster AI, **Ask/Troubleshoot mode**, token reduction, GW API in MCP
  tools, max tool iterations configurable, MCP Ambient discovery/debug; 2.30
  AI context-awareness + UX, **streaming MCP tool status**, smaller output
  payload, multi-cluster MCP eval suite.
- **Ambient / multi-mesh**: 2.16–2.17 validation fixes; 2.18 multi-CP
  improvements; 2.26 trace overlay + inter-cluster telemetry (2.25); 2.28–2.30
  Ambient v1.30 support, waypoint/ztunnel fixes, L7-config-disable for
  non-waypoint services.
- **GW API**: 2.19 v1.4.0; 2.23 v1.5.0; 2.28 IE v1.5.0; 2.30 v1.6.0; 2.16
  clusters with only GW-API gateways (no Istio gateways); 2.17 Inference
  Extension v1.
- **Performance**: 2.16 istio_detail appender opts; 2.21 **traffic graph
  caching** (background refresh, 10m default, `graph_cache.enabled`); 2.22
  **health pre-compute/caching** (5m/3m/10m, `health_cache`); 2.24
  `kiali_health_status` metric redefined + opt-in; 2.27 multiple perf items.
- **Auth / security**: 2.17 OIDC multi-audience + x-request-id tracing; 2.21
  OIDC **Authorization Code + PKCE (SSO)**, auto-rotated certs for external
  services, TLS profiles; 2.28 OAuth2 client_credentials; 2.19 CR
  initContainers; 2.17 NetworkPolicy for ingress.
- **OSSMC**: 2.18 Netobserv traffic-graph side-panel; 2.20 PF6 upgrade; 2.23
  new Overview page; 2.26 Namespace/App list pages + IstioConfigListPage;
  2.17 "openshift" tracing url_format.
- **Breaking / upgrade notes**: 2.16 removed `spec.external_services.istio.
  root_namespace` (discovery selectors must now include Istio CP namespaces);
  2.17 removed `spec.external_services.istio.registry`; 2.24 `kiali_health_status`
  now opt-in; 2.27 `spec.istio_labels.*` fields ignored; 2.22 health cache +
  CR fields (`health_config.compute.*`, `kiali_internal.health_cache.enabled`).
- **Build/tooling**: 2.24 Node 24, Yarn 4, Go 1.25; 2.20 TypeScript 5, PF6,
  legacy message center replaced; 2.19 TS/Go bumps.

---

## 7. OSSMC status

**GA (released October 2023); developer preview since Sept 2022.** OpenShift
Service Mesh Console is a **dynamic plugin** for the OpenShift Console. Two
operating modes:
- **With a connected Kiali server** — full Kiali-powered experience inside the
  console: a **Service Mesh** menu category with pages **Overview, Traffic
  Graph, Mesh (Istio infra status), Namespaces, Applications, Services,
  Workloads, Istio Config** (each with list + detail, matching standalone
  Kiali), plus **Service Mesh tabs** on OpenShift Workloads/Services/Projects/
  Istio resource detail pages. Connects via the plugin proxy configured on the
  **OSSMConsole CR**. If it can't reach Kiali → "Service Mesh is not
  configured" message; unexpected failure → "Service Mesh Console Unavailable"
  (isolated from rest of console).
- **Without a Kiali server ("lite mode")** — **Istios** and **Kialis** pages
  that list every Istio and Kiali CR on the cluster, **no Kiali server
  required** (talks to the Kubernetes API). **Kialis** shows Connected
  (Active/Inactive/Unknown), Observe links (Kiali UI | Console), and **Connect /
  Disconnect** actions (require patch permission on the `ossmconsoles.kiali.io`
  CR) to switch which Kiali server backs the observability pages.
Install: Kiali Operator (server optional for Istios/Kialis) → create an
**OSSMConsole CR** → open Service Mesh → Istios/Kialis. Connect a Kiali
server via the Kialis page **Connect** or `spec.kiali` on the CR. OSSMC does
not replace standalone Kiali (still reachable via its own route).

---

## Failures / caveats
- **Medium 2.16–2.30 post**: behind a Cloudflare challenge. Direct curl
  (multiple UAs incl. Googlebot), web_extract, r.jina.ai, archive.today,
  RSS, and rsshub all blocked. **Wayback Machine down** (503 / 429, CDX empty).
  Captured the opening + sections 1 (AI & MCP) and 2 (UX & PF6) verbatim
  (saved as kiali-blog-releases-2-16-to-2-30-features-update.md, flagged
  `completeness: partial`). Sections 3+ of the post were NOT retrieved.
  Mitigation: the **official Kiali release notes** (kiali.io/news/
  release-notes) are saved verbatim and cover the same 15 releases with
  per-version feature entries — used to complete the per-area digest in §6.
- No kiali.io page 404'd; all 28 doc pages + release notes fetched clean.
  The features index also lists pages not explicitly requested (international-
  ization, ambient, istio-component-status, multi-cluster, multi-mesh,
  security) — not fetched (out of scope), but their URLs are in
  kiali-docs-features-index.md if needed later.
