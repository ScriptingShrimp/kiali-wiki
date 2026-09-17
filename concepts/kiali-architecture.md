---
title: Kiali Architecture
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, architecture, backend, frontend, api, kubernetes, service-mesh, reference]
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

# Kiali Architecture

> **Confidence note:** the backend deep-dive source
> (`raw/articles/kiali-doc-backend-architecture.md`, repo
> `docs/agents/backend-architecture.md`) is flagged **drifted** in the scribe
> status table (freshness 60, last scribe run 2026-05-26). Details attributed
> to that source are best-effort as of its 2026-05-26 scan and may not match
> current master; everything else below is from higher-confidence or
> kiali.io sources. All claims dated 2026-09-17 (ingestion).

## What it is

Kiali is a two-component system: a **Go backend** running in the cluster and a
**React SPA frontend**. The backend talks to Istio (istiod), the Kubernetes
API, Prometheus, and optional Jaeger/Tempo/Grafana, then exposes a JSON REST
API that the frontend consumes. The backend is stateless — configuration comes
from the Kiali CR (operator) or a ConfigMap (Helm), and the frontend's only
server-side state is the client-side encrypted session cookie.
^[raw/articles/kiali-docs-architecture.md]

High-level data flow:

```
Browser (React SPA, embedded in the binary)
   │  /api/... (JSON, per-route auth)
   ▼
Go backend (gorilla/mux, middleware stack, handlers/)
   ├── business/ Layer (per-request service objects)
   │      ├── kubernetes/ ClientFactory (per-user + SA clients)
   │      ├── cache/ (KialiCache + controller-runtime informer caches)
   │      ├── istio/ Discovery, business.ControlPlaneMonitor
   │      └── prometheus/ ClientInterface (Istio telemetry queries)
   ├── graph/ (traffic graph engine — see [[kiali-graph-engine]])
   ├── handlers/authentication/ (auth — see [[kiali-auth-and-caching]])
   └── tracing/, grafana/, perses/ (optional integrations)
   ▼
Kubernetes/OKD API · istiod · Prometheus · Jaeger/Tempo · Grafana/Perses
```

## Backend (Go binary)

One Go binary serves the JSON REST API under `/api/` (all routes
authenticated by default) plus the React SPA embedded via `//go:embed`.
Handlers build a per-request `business.Layer` (domain service objects scoped
to the user's tokens); all Kubernetes/Istio access goes through a
`ClientFactory` (short-lived per-user clients, 15-min TTL, plus long-lived
Kiali SA clients); the per-route middleware chain (outer → inner) is
`httpHandlerLogger` → `authHandler` → `metricHandler` → handler. The full
module-by-module breakdown (startup, HTTP server & security headers, client
layer, API surface) lives in [[kiali-backend-stack]].

## Frontend

A React 17 + TypeScript SPA: React Router v5 (plus `react-router-dom-v5-compat`
for v6 APIs), Redux with redux-persist, PatternFly 6, typestyle scoped CSS,
i18next for translations. The build output is embedded into the Go binary
(`//go:embed`) and served by the backend; the router rewrites `<base href>`
and `env.js` to match the configured web root, and `/console/...` routes fall
through to `index.html` for client-side navigation. The app is largely
stateless; only session credentials (in the encrypted cookies) and UI
preferences persist, and only inside one browser.
^[raw/articles/kiali-docs-architecture.md]^[raw/articles/kiali-doc-frontend-architecture.md]

## Build & toolchain

Decomposed Makefile (root + nine `.mk` files). The Go binary is built
CGO-disabled with version ldflags, embedding the pre-built frontend (build UI
first: `make build-ui`, then `make build`). Container images push to OpenShift,
Minikube, or KinD registries through a unified `cluster-push` target
(`container-build`/`container-push*` with `CLUSTER_TYPE=local` for local
registries). Node.js ≥ 20, Yarn pinned via the `packageManager` field and
corepack. `kiali gather` recordings feed the graph test suite.
^[raw/articles/kiali-doc-build-and-dev-conventions.md]^[raw/articles/kiali-repo-readme.md]

## Observability of Kiali itself

- Prometheus `/metrics` endpoint (optional separate port) — API duration,
  failure, graph generation/appender timers, graph cache hit/miss/eviction
  counters.
- OpenTelemetry: Kiali exports its own spans when
  `conf.Server.Observability.Tracing.Enabled`.
- `kiali gather` mode records all graph Prometheus queries for replay.
- `server.audit_log` gates credential-rotation audit events
  (see [[kiali-auth-and-caching]]).

## Related pages

- [[kiali]] — the project entity (releases, governance, repos)
- [[kiali-graph-engine]] — the traffic graph engine, appenders, graph cache
- [[kiali-auth-and-caching]] — auth strategies, session cookies, CredentialManager

## Open questions / watch items

- Backend-architecture source is drifted (2026-05-26 scan); re-scan
  `docs/agents/backend-architecture.md` before relying on fine detail
  (handler names, startup step ordering). ^[raw/articles/kiali-doc-STATUS.md]
- The per-user client TTL (15 min) and the SA-token-dominant read model are
  load-bearing security assumptions; verify against current `kubernetes/`
  code before writing docs or patches.
