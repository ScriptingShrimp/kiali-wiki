---
title: Kiali
created: 2026-09-17
updated: 2026-09-17
type: entity
tags: [kiali, istio, service-mesh, kubernetes, release, reference, security, caching]
sources:
  - raw/articles/kiali-repo-readme.md
  - raw/articles/kiali-docs-architecture.md
  - raw/articles/kiali-repo-governance.md
  - raw/articles/kiali-docs-news-release-notes.md
  - raw/articles/kiali-repo-releases-recent.json
confidence: high
---

# Kiali

Kiali is an open-source observability and management console for the Istio service
mesh. It gives operators a view of their mesh — traffic topology, health,
validations, configuration, tracing, and (in developer preview) AI-assisted
troubleshooting — and is installed as an Istio add-on on Kubernetes/OKD or as a
trusted component inside a production environment.^[raw/articles/kiali-repo-readme.md]

## Key facts (as of 2026-09-17)

| Field | Value |
|---|---|
| Main repo | `github.com/kiali/kiali` (Go backend + React frontend in one repo) |
| License | Apache 2.0 |
| Latest release | **v2.32.0** — "Sprint Release", published 2026-09-13 |
| Release notes | https://kiali.io/news/release-notes/ (upstream is authoritative) |
| Documentation | https://kiali.io/docs |
| Companion repos | `kiali/kiali-operator` (operator), `kiali/helm-charts` (Helm) |
| Scribe scan for architecture docs | see per-page frontmatter; upstream moves fast, claims here are dated |

Release cadence is roughly **biweekly** (a "sprint release" every ~2 weeks, with
occasional longer gaps): 2.27.0 (2026-06-01), 2.28.0 (2026-06-22), 2.29.0
(2026-07-13), 2.30.0 (2026-08-03), 2.31.0 (2026-08-21), 2.32.0 (2026-09-14
sprint release date in the kiali.io notes). Releases are cut by
`github-actions[bot]` and ship binary assets (e.g. `kiali-linux-amd64`).
^[raw/articles/kiali-docs-news-release-notes.md]^[raw/articles/kiali-repo-releases-recent.json]

> Upstream moves fast: treat every "current" claim on this page as true only as
> of 2026-09-17 (ingestion date) and re-verify against the release notes before
> relying on it.

## Components

- **Backend** — a single Go binary. It serves a JSON REST API under `/api/`
  (authenticated by default) and the React SPA embedded via `//go:embed` for all
  other paths. No storage of its own; configuration comes from the Kiali CR
  (operator install) or a ConfigMap (Helm install).
  ^[raw/articles/kiali-docs-architecture.md]^[raw/articles/kiali-repo-readme.md]
  Details: [[kiali-architecture]]
- **Frontend** — a React 17 + TypeScript SPA (PatternFly 6, Redux with
  redux-persist, i18next), in `frontend/` of the main repo. Served by the
  backend in standard deployments; mostly stateless, with session credentials
  kept client-side in the browser. ^[raw/articles/kiali-docs-architecture.md]
- **Kiali Operator** — separate repo `kiali/kiali-operator`; manages Kiali
  lifecycle in-cluster. Developer workflow symlinks it into `kiali/operator`.
  ^[raw/articles/kiali-repo-readme.md]
- **Helm charts** — `kiali/helm-charts` for plain-Kubernetes installs.
  ^[raw/articles/kiali-repo-readme.md]

## Feature areas

- **Topology / traffic graph** — the central feature: real-time mesh traffic
  graphs (workload/app/service views), health coloring, find/hide, replay.
  Engine details: [[kiali-graph-engine]] ^[raw/articles/kiali-docs-features-topology.md]
- **Authentication & security** — five auth strategies (anonymous, token,
  OpenID, OpenShift OAuth, header), encrypted-cookie sessions, credential/CA
  rotation. Details: [[kiali-auth-and-caching]] ^[raw/articles/kiali-doc-auth-and-security.md]
- **Health** — workload/app/namespace/service health from Prometheus;
  custom health status configuration.
- **Validations** — Istio config validation (KIA#### rules), with ignore
  annotations; a validations controller re-checks configs on a reconcile
  interval.
- **Tracing** — proxies distributed traces from Jaeger or Tempo.
- **Dashboards** — deep-links to Grafana and Perses.
- **AI (developer preview)** — Chat AI over OpenAI-compatible or Google Gemini
  providers, backed by MCP tools that query live mesh data; APIs and config
  are explicitly still evolving. ^[raw/articles/kiali-repo-readme.md]
  ^[raw/articles/kiali-doc-observability-and-ai.md]

## Ecosystem dependencies

| Dependency | Relationship |
|---|---|
| Istio | **Required** — Kiali is a console for Istio meshes; reads istiod, configmaps, etc. `istiod` communication can be disabled for inaccessible environments |
| Prometheus | **Hard dependency** for topology/metrics/health; Kiali assumes Istio's default telemetry metrics |
| Kubernetes / OKD API | Fetches workloads, services, namespaces, Istio CRDs, Gateway API objects |
| Jaeger / Tempo | Optional — distributed tracing data source |
| Grafana / Perses | Optional — dashboard deep-links |
| OpenShift | Optional — native OAuth strategy, multi-cluster OSSMC scenarios |
| OSSMC | OpenShift Service Mesh Console ships Kiali as an embedded console |

^[raw/articles/kiali-docs-architecture.md]

Recent releases in the AI/multi-cluster/ambient space (2.30.0–2.32.0, as of
2026-09-17): K8s Gateway API v1.6.0 support, OpenShift impersonation for
multi-cluster auth, MCP tooling for Ambient/Gateway API, fleet mesh + multi-mesh
OSSMC capabilities, and the graph-cache health integration in 2.32.0.
^[raw/articles/kiali-docs-news-release-notes.md]

## Governance (as of 2026-09-17)

Maintainers (write access to the `kiali` GitHub org; collectively manage project
resources): aljesusg, ferhoyos, hhovsepy, jmazzitelli, josunect,
leandroberetta, nrfox, xunzhuo. Becoming a maintainer requires ~3 months of
participation, 10 non-trivial PRs authored + 10 non-trivial PRs reviewed, a
nomination by an existing maintainer, two seconds, and 5 working days without
objection (else majority vote). A separate **Testers** tier exists for quality
work. ^[raw/articles/kiali-repo-governance.md]

## Developer workflow (short form)

- Toolchain: Go (version pinned in the Makefile), git, gcc, Docker/Podman
  (`DORP=podman`), Node.js ≥ 20 (Yarn pinned via corepack), GNU make.
- Local dev: `make build-ui && make run-backend` (hot reload via `air`) plus
  `make run-frontend`; `kiali run` connects from your kubeconfig, including
  multi-cluster contexts via `--remote-cluster-contexts`.
- Cluster bring-up helpers: `hack/run-integration-tests.sh` (minikube/OKD/KinD,
  installs Istio + Bookinfo; also runs in CI), `hack/k8s-minikube.sh`,
  `hack/start-kind.sh`, `hack/crc-openshift.sh`.
- Deploy dev builds: `make cluster-push` (or `container-push*` with
  `CLUSTER_TYPE=local`), `make operator-create`, `make kiali-create`; reload
  the server image with `make kiali-reload-image`.
- Contributing: see the repo's `CONTRIBUTING.md` and the kiali.io community page.

^[raw/articles/kiali-repo-readme.md]

## Repository map (high level)

`cmd/` (Cobra entry, `run`/`gather` subcommands) · `server/` (HTTP listener) ·
`routing/` (gorilla/mux, per-route auth wrapping) · `handlers/` (REST handlers,
incl. `handlers/authentication/`) · `business/` (per-request `Layer`) ·
`graph/` (traffic graph engine, `graph/telemetry/istio/`) · `prometheus/`
(client + query recording) · `kubernetes/` (ClientFactory, per-user clients) ·
`cache/` (KialiCache, controller-runtime informers) · `config/`
(`CredentialManager`, TLS policy, security types) · `istio/` (discovery,
constants) · `jwt/`, `tlspolicy/` · `frontend/` (React SPA) · `design/KEPS/`
(enhancement proposals — see the KEP index in the wiki raw sources) ·
`docs/agents/` (machine-verified codebase documentation, scribe-maintained).
^[raw/articles/kiali-repo-architecture.md]^[raw/articles/kiali-repo-docs-agents-status.md]

## Related

- [[kiali-architecture]] — backend/frontend architecture, middleware, caching
- [[kiali-graph-engine]] — traffic graph computation, appenders, graph cache
- [[kiali-auth-and-caching]] — auth strategies, session cookies, credential rotation

## Open questions / watch items

- The AI Chat / MCP feature is explicitly a **developer preview** with
  breaking-change expectations; pin claims about it to a dated release.
- Architecture docs under `docs/agents/` are scribe-generated and carry
  freshness scores; `backend-architecture.md` was flagged **drifted** (last
  scribe run 2026-05-26) — re-scan before trusting fine detail.
  ^[raw/articles/kiali-doc-STATUS.md]
