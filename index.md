# Wiki Index

> Content catalog. Every wiki page listed under its type with a one-line summary.
> Read this first to find relevant pages for any query.
> Last updated: 2026-09-17 | Total pages: 22
> Domain: Kiali upstream development (observability console for the Istio service mesh) + the service-mesh tooling I use daily. Secondary scope (other daily tools) to be defined later — see SCHEMA.md.

## Entities

- [[kiali]] — The Kiali project: what it is, components, releases, governance, and where to go next (entry point for everything in this wiki).
- [[kiali-operator]] — The separate kiali/kiali-operator repo: watches the Kiali CR, manages lifecycle, and reconciles OSSMConsole.
- [[ossmc]] — OpenShift Service Mesh Console: the dynamic OpenShift Console plugin (GA Oct 2023), connected-Kiali vs lite mode, multi-mesh navigation.

## Concepts & Runbooks

- [[kiali-ai-chat-and-mcp]] — Kiali Chatbot (in-UI) and Kiali MCP (external) over the shared internal MCP tool surface; 12-tool table, provider config, endpoints.
- [[kiali-ai-contributions]] — AI-assisted contribution policy: human accountability, mandatory Assisted-by/Generated-by trailers, prohibited practices.
- [[kiali-architecture]] — Two-component architecture overview (Go backend + embedded React SPA) with data-flow diagram; points to the deep-dive pages below.
- [[kiali-auth-and-caching]] — Authentication: five strategies (anonymous/token/header/openshift/openid), session cookies, JWT, TLS, CredentialManager.
- [[kiali-backend-stack]] — Module-by-module Go backend: Cobra CLI, RunServer startup, HTTP middleware chain, business.Layer, kubernetes.ClientFactory.
- [[kiali-build-and-dev]] — Developer runbook: 3-repo layout, toolchain, decomposed Makefile, Dockerfiles, quick-reference; points to the test/CI and conventions pages.
- [[kiali-caching]] — The five caching layers (Kiali, controller-runtime K8s, Prometheus, Tempo, per-session graph) and the never-cached list.
- [[kiali-code-conventions]] — Go + TypeScript style, file-protection rules, and operator development workflow.
- [[kiali-contribution]] — How to contribute: discuss-first, commit signing, fork-based PR workflow, backport checklist, governance roles summary.
- [[kiali-features]] — Standalone Kiali feature map as of v2.32.0: topology/graph, health, details, tracing, wizards, config, validations, ambient/multi-cluster.
- [[kiali-governance-community]] — Roles (contributor→maintainer→tester→leader), promotion thresholds, voting, inactivity, release cadence.
- [[kiali-graph-cache]] — Per-session graph cache: LRU, RefreshJob lifecycle, historical queries, cache KEP (shipped) vs open controller-model KEP.
- [[kiali-graph-engine]] — Graph engine pipeline: Options → Prometheus → TrafficMap → appender order → per-session cache; 4-query telemetry scheme.
- [[kiali-installation]] — Two deployment models (operator vs Helm), quick start, production operator flow, full Kiali CR spec surface, dependency prerequisites.
- [[kiali-integrations]] — Integration surface: data-plane deps (Istio required, Prometheus hard) and platform/UI integrations (OSSMC, Backstage, AI/MCP).
- [[kiali-keps]] — KEP process, template, and a status table for all 9 KEP directories (status inferred; no formal Status field upstream).
- [[kiali-release-history]] — Verified per-version record for 2.16.0 through 2.32.0: dates, headline features, breaking changes (all 17 versions, provenance-marked).
- [[kiali-release-process]] — Release cadence, versioning, supported-branch/backport table, release automation (workflows), and the six delivery surfaces.
- [[kiali-tests-and-ci]] — Local clusters, the full test matrix (unit, backend e2e, envtest, Cypress Gherkin, Molecule), and the GitHub Actions CI fan-out.

## Comparisons

<!-- One line per comparison: [[page-slug]] — one-line summary. Alphabetical. (none yet) -->

## Queries

<!-- Filed query results worth keeping: [[page-slug]] — one-line summary. Alphabetical. (none yet) -->

## Raw Sources

<!-- raw/ is not indexed the same way, but notable ingests are noted here. -->

- raw/articles/ — 81 provenance-verified upstream sources: kiali/kiali repo docs (README, ARCHITECTURE, CONTRIBUTING, AGENTS, AI_POLICY, GOVERNANCE, the docs/agents/ set, all 9 KEPS), the full kiali.io docs (features, installation, integrations, OSSMC, terminology, AI), release notes 2.16→2.32, and GitHub metadata (releases JSON, workflows JSON, design/KEPS JSON). Every file carries sha256 provenance in frontmatter that matches its body.
- raw/articles/DIGEST-kiali-2026-09-17.md — the dense cross-repo digest from the research pass; the primary reference for release/feature/version attributions used by the release-history and features pages.
