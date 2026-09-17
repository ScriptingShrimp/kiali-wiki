---
title: Kiali Backend Stack
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, architecture, backend, api]
sources:
  - raw/articles/kiali-doc-backend-architecture.md
  - raw/articles/kiali-repo-architecture.md
  - raw/articles/kiali-docs-architecture.md
  - raw/articles/kiali-doc-business-logic.md
  - raw/articles/kiali-doc-kubernetes-client.md
  - raw/articles/kiali-doc-frontend-architecture.md
  - raw/articles/kiali-doc-STATUS.md
confidence: medium
---

# Kiali Backend Stack

### Single binary, two concerns

One Go binary serves (1) the JSON REST API under `/api/` (all routes
authenticated by default) and (2) the React SPA embedded via `//go:embed`.
`main()` in `kiali.go` just calls `cmd.Execute()` (Cobra). The `!exclude_frontend`
build tag guards `main()`; the tag is used by `make test` to skip frontend
files in unit tests, **not** to build an API-only server.
^[raw/articles/kiali-doc-backend-architecture.md]

### CLI surface

`cmd/root.go` builds the root command (`-config`/`--config` path quirk: the
helm chart historically passed single-dash `-config`, which `Execute()`
rewrites to `--config`). The default `RunE` (no subcommand) starts the server:
`maxprocs.Set()` and `memlimit` (cgroup-aware GOMAXPROCS/GOMEMLIMIT tuning),
`config.Validate`, home-cluster resolution, `kubernetes.NewClientFactory`,
`RunServer`. Subcommands:

- `kiali run` — local mode against a kubeconfig; port-forwards to
  Prometheus/Tempo/Grafana; `kiali run offline` runs against static YAML dirs.
- `kiali gather` — wraps the Prometheus client in a `QueryRecorder` that dumps
  all graph queries to `prom-graph-gather.log` for offline test replay.

^[raw/articles/kiali-doc-backend-architecture.md]

### Startup sequence (from `cmd/server.go:RunServer`)

1. Resolve TLS policy (`tlspolicy.Resolve`).
2. Build the controller-runtime manager — per-cluster informer caches (home
   cluster via `ctrl.NewManager`, remote clusters via `cluster.New`); cache
   transforms strip managed-fields and prune Pod/Service to the fields Kiali
   uses.
3. Create `cache.KialiCache`; set build info.
4. Create `istio.Discovery` + `business.ControlPlaneMonitor`.
5. Wire the Kiali SA token credential (file-watched for kubelet rotation).
6. Init the Prometheus client — probes `/-/healthy`; on failure injects a
   `NoopClient` with a `DisabledReason` (Kiali keeps serving, degraded).
7. Init the tracing client **asynchronously** (loader closure so handlers can
   start before the backend is reachable).
8. Init Grafana; create `business.Layer`.
9. Start the validations controller (if reconcile interval > 0) in a goroutine.
10. `cache.WaitForCacheSync` across all clusters; prime istiod proxy status
    (or prime the cluster cache if the Istio API is disabled); start
    `business.HealthMonitor` if enabled.
11. Start `server.Server`.

Shutdown on SIGINT/SIGTERM stops server, metrics server, and controller in
reverse order.
^[raw/articles/kiali-doc-backend-architecture.md]

### HTTP server & middleware

`server/server.go`: a `Server` struct wraps `http.Server` + gorilla/mux router
+ optional OTel tracer. `NewServer` builds the router, applies middleware
(`securityHeaders` always; `corsAllowed` if `CORSAllowAll`; `otelmux.Middleware`
if tracing enabled), wraps in gzip for JSON/JS/HTML/CSS/SVG when
`GzipEnabled`, and sets security headers on every response
(`X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`,
`X-XSS-Protection: 1; mode=block`). A separate metrics server can expose
`/metrics` (Prometheus) on another port.

Per-route middleware chain (outermost → innermost):
`httpHandlerLogger` (zerolog, `X-Request-Id` passthrough-or-generate) →
`authHandler` (the configured `AuthController.ValidateSession`; injects
`map[string]*api.AuthInfo` into context) → `metricHandler` (Prometheus timer,
`APIFailureMetric` on 5xx) → handler.
^[raw/articles/kiali-doc-backend-architecture.md]

### Handlers & the business layer

Handlers in `handlers/` follow a closure pattern: dependencies are closed over
at router construction; each request calls `getLayer(r, ...)`
(`handlers/utils.go`) which reads the per-cluster auth info from context and
builds a **`business.Layer`** — the per-request bundle of service objects
(health, istio config, mesh, topology, validations, etc.) scoped to that
user's tokens. `handlers/base.go` provides the JSON response helpers; request
bodies are capped at 10 MB.

The `business/` package is where all domain logic lives: fetching/aggregating
apps, workloads, services, health, Istio config, mesh topology, and
validations — one per-request `Layer` per request, never shared across users.
^[raw/articles/kiali-docs-architecture.md]^[raw/articles/kiali-doc-business-logic.md]

### Kubernetes client layer

All Kubernetes/Istio/Gateway-API/OpenShift access goes through a
**`ClientFactory`** (`kubernetes/`) that vends:

- short-lived **per-user `UserClientInterface`** clients (15-minute TTL) built
  from the user's bearer token (impersonation-aware for the header strategy),
  used for reads on the user's behalf and all writes;
- long-lived **Kiali SA `ClientInterface`** clients, used for the informer
  caches and most read paths (the Kiali SA is broadly privileged; per-user
  access is enforced by namespace-scope checks against the user's allowed
  namespace list, not by the token on every read).

Multi-cluster is handled by reading remote-cluster secrets at startup; the
`UserSessions`/`AuthInfo` maps are keyed by cluster name, so a single Kiali
instance can hold per-cluster user sessions.
^[raw/articles/kiali-doc-kubernetes-client.md]^[raw/articles/kiali-doc-auth-and-security.md]

### API

Routes are `/api/...` with **no version segment** — the API is explicitly
internal and may change without backward-compatibility guarantees (swagger
`BasePath: /api`). A configured `Server.WebRoot` (e.g. `/kiali`) shifts
everything to `/kiali/api` via a mux `PathPrefix` subrouter. Representative
routes: `GET /api/namespaces/graph`, `GET /api/mesh/graph`,
`GET/POST/PATCH/DELETE /api/namespaces/{ns}/istio/{group}/{version}/{kind}/{object}`,
`GET /api/clusters/health`, `POST /api/chat/{provider}/{model}/ai`,
`GET /api/auth/info` + `/api/logout`, `GET /healthz`.
^[raw/articles/kiali-doc-backend-architecture.md]

## Related

- [[kiali-architecture]] — the full system: data flow, frontend, build, observability
- [[kiali-graph-engine]] — the traffic graph engine the backend serves
- [[kiali-auth-and-caching]] — auth strategies, sessions, credential rotation
- [[kiali-features]] — user-facing feature map
