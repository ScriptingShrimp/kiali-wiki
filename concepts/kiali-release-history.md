---
title: Kiali Release History (2.16.0 to 2.32.0)
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, release, timeline, versioning, roadmap]
sources: [raw/articles/kiali-docs-news-release-notes.md, raw/articles/kiali-repo-releases-recent.json, raw/articles/kiali-repo-agents.md, raw/articles/kiali-doc-build-and-dev-conventions.md, raw/articles/kiali-cithub-workflows-raw.json, raw/articles/DIGEST-kiali-2026-09-17.md, raw/articles/kiali-repo-readme.md]
confidence: high
---

# Kiali Release History (2.16.0 through 2.32.0)

## Per-version record: 2.16.0 → 2.32.0

The kiali.io release notes (saved verbatim as
`raw/articles/kiali-docs-news-release-notes.md`) are the authoritative
per-version record. The 15-release window 2.16→2.30 was also summarized in a
Medium post, which was partially Cloudflare-walled at ingestion; where the two
sources could be compared, the release notes were treated as authoritative.
Highlights per area (version attributions verified against the release-notes
text): ^[raw/articles/kiali-docs-news-release-notes.md] ^[raw/articles/DIGEST-kiali-2026-09-17.md]

### AI Assistant & MCP (the dominant feature arc)

- **2.22.0** (2026-02-16) — **AI Chatbot Widget + MCP integration (Dev
  Preview)**: SSE streaming (OpenAI, Google Gemini), tool-execution UI. Also
  **health status pre-compute** (see below).
- **2.23.0** (2026-03-09) — `get_resource_metrics` (CPU/mem) and `get_logs` tools; chatbot
  integrated into the new Overview/Namespaces pages.
- **2.24.0** (2026-03-30) — `get_istio_config` tool token optimization.
- **2.25.0** (2026-04-20) — multi-primary validation for AI backend API tests.
- **2.26.0** (2026-05-29) — **Google + Anthropic providers**; MCP error-type
  handling.
- **2.27.0** (2026-06-01) — Anthropic support continued, stale-store cleaner background
  job, `resource_details` app-level, **token-usage analytics**, system-prompt
  injection hardening.
- **2.28.0** (2026-06-22) — **built-in MCP prompts**, MCP Checker actions, LightSpeed TLS
  verification configurable, OAuth2 `client_credentials`.
- **2.29.0** (2026-07-13) — multi-cluster AI, **Ask/Troubleshooting mode selection** with
  provider-specific prompts, Gateway API in MCP tools, max tool iterations
  configurable, MCP Ambient discovery/debugging.
- **2.30.0** (2026-08-03) — context-awareness & UX, **streaming MCP tool-execution status**,
  smaller output payloads, **multi-cluster MCP eval suite**.
- **2.31.0** (2026-08-21) — **automated MCP pin-compatibility validation** (replacing
  manual contract tests).
- **2.32.0** (2026-09-14) — mesh traffic graph health uses the cached health status (the
  `kiali_health_status` metric story continues).

### Performance (graph & health caching arc)

- **2.21.0** (2026-01-26) — **traffic graph caching**: background graph
  refresh + caching (10m default, `graph_cache.enabled`), plus client-side
  rendering improvements for many service nodes.
- **2.22.0** — **health pre-compute & caching** (enabled by default):
  `spec.health_config.compute.{duration:5m, refresh_interval:3m, timeout:10m}`,
  `spec.kiali_internal.health_cache.enabled`. Overview/List pages moved from
  on-demand to cached health; Duration dropdown removed from those pages;
  backend resource utilization rises because Kiali now refreshes health
  independent of user sessions.
- **2.24.0** — `kiali_health_status` metric **redefined** (lower cardinality,
  single gauge per entity) and made **opt-in** via
  `spec.server.observability.metrics.health_status.enabled` (off by default).
- **2.27.0** — health-cache memory utilization, single-namespace workload
  fetch, istio appender and traffic-animation perf.
- **2.32.0** — graph uses cached health status; "Scale: Guidance for
  Pre-Aggregated, federated metrics" (ties into the [[kiali-keps|metric-rules KEP]]).

### Auth & security

- **2.17.0** (2025-10-13) — OIDC **multiple audiences**; `x-request-id` forwarded to
  prometheus calls for tracing.
- **2.19.0** (2025-11-24) — custom `initContainers` on the Kiali deployment.
- **2.21.0** — **OIDC Authorization Code + PKCE (SSO)**, explicit OIDC config
  when `.well-known` is locked down, **auto-rotated certificates** for
  external-service connectivity, platform TLS profiles.
- **2.28.0** — **OAuth2 client_credentials** across kiali, operator, and
  helm-charts.
- **2.30.0** — OpenShift Impersonation for multi-cluster auth.

### Multi-cluster / OSSMC

- **2.18.0** (2025-11-03) — Netobserv navigation + traffic-graph side-panel in OSSMC;
  NetworkPolicy for OLM-installed operator; multi-control-plane Mesh page
  improvements.
- **2.20.0** (2025-12-22) — OSSMC **PatternFly 6** upgrade (standalone UI to PF6 also;
  legacy message center replaced; TypeScript 5).
- **2.23.0** — new **Overview page** in OSSMC; new Overview & Namespaces pages
  in standalone (sort/filter/mTLS).
- **2.26.0** — OSSMC Namespace/Application list pages, Kiali's
  IstioConfigListPage replaces native page, Namespace Detail page.
- **2.31.0** — OSSMC **fleet mesh and multi-mesh capabilities**; glass and
  high-contrast themes for OpenShift 5.0.

### Gateway API

- **2.16.0** (2025-09-22) — clusters with **only** Gateway API gateways (no Istio
  gateways). **2.17.0** — Inference Extension v1. **2.19.0** — GW API
  **v1.4.0**. **2.23.0** — GW API **v1.5.0**. **2.28.0** — GW API Inference
  Extension v1.5.0. **2.30.0** — GW API **v1.6.0**.

### Build/tooling bumps

- **2.17.0** — Go 1.24.4. **2.20.0** — TypeScript 5, PF6. **2.23.0** — Go
  1.24.13. **2.24.0** — **Node 20→24, Yarn 1→4, Go 1.24→1.25**, automatic
  `GOMEMLIMIT` from cgroups.

### Breaking / upgrade notes worth calling out

- **2.16.0** — `spec.external_services.istio.root_namespace` removed; CRD now
  auto-detects the root namespace and discovery selectors must include all
  Istio control-plane namespaces.
- **2.17.0** — `spec.external_services.istio.registry` removed (MUST be
  removed from existing CRs).
- **2.22.0** — health pre-compute defaults (above).
- **2.24.0** — `kiali_health_status` opt-in (above).
- **2.27.0** — `spec.istio_labels.*` fields ignored (standard constants now
  used).
- **2.30.0** — custom health configs: a failure threshold of `0` now actually
  triggers Failure status (previously a no-op) — re-check custom health
  configs on upgrade.

## Related

- [[kiali-release-process]] — the release cadence, automation, and notes conventions this page records
- [[kiali]] — the Kiali project itself
- [[kiali-governance-community]] — maintainers and community behind the releases
- [[kiali-keps]] — design proposals (KEPs) that shaped released features
