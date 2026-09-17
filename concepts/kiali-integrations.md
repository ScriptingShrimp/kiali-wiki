---
title: Kiali Integrations
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, integration, istio, prometheus, jaeger, grafana, openshift, mcp, tool, reference]
sources: [raw/articles/kiali-docs-architecture.md, raw/articles/kiali-docs-integrations-index.md, raw/articles/kiali-docs-integrations-ossm-console.md, raw/articles/kiali-docs-integrations-kiali-backstage-plugin.md, raw/articles/kiali-docs-ai-kiali-mcp.md]
confidence: high
---

# Kiali Integrations

Kiali's integrations split into two categories: the **data-plane dependencies** it
reads to build its view of the mesh (Istio, Prometheus, Kubernetes, and optional
Jaeger/Tempo + Grafana/Perses), and the **platform/UI integrations** that embed or
extend Kiali (the OpenShift Service Mesh Console and the Backstage plugin), plus
the **AI/MCP** surface that exposes Kiali to LLM assistants. This page maps the
whole integration surface as of v2.32.0 (2026-09-14). The feature map is in
[[kiali-features]]; OSSMC has its own entity page ([[ossmc]]).
^[raw/articles/kiali-docs-architecture.md]

## Data-plane dependencies

Kiali is a **console for Istio**, so Istio is a requirement; the two are installed
separately. Kiali retrieves Istio data and configuration through **Prometheus**,
the **Kubernetes API**, and **istiod**.

| Component | Role | Required? |
|---|---|---|
| **Istio** | Provides and controls the service mesh; source of config (virtual services, destination rules, gateways, etc.) and mesh state. `istiod` communication can be disabled where istiod is inaccessible. | **Required** |
| **Prometheus** | Stores Istio telemetry metrics. Kiali queries it directly to build the mesh topology, show metrics, compute health, and surface problems. Assumes **Istio's default telemetry metric set** (customization allowed only if Kiali's required-metrics requirements are still met). | **Hard dependency** — many features break without it |
| **Kubernetes / OKD API** | Fetches namespaces, services, deployments, pods, and resolves relationships between cluster entities; also retrieves Istio configs. Known to work on OKD and Kubernetes (and derivatives). | **Required** |
| **Jaeger** | Optional distributed-tracing backend; Kiali deep-links the user to Jaeger's trace data (only when Istio's distributed tracing is enabled). | Optional |
| **Grafana Tempo** | Alternative tracing backend to Jaeger. | Optional |
| **Grafana** | Optional. Kiali's metric pages show a deep-link to the same metric in Grafana. Kiali itself has basic, non-customizable metric views (default Istio metrics, some groupings, time ranges, no custom queries) — Grafana is the tool for full custom dashboards. | Optional |
| **Perses** | Dashboard deep-links. | Optional |

The current list of **required Prometheus metrics** is documented in the kiali.io
FAQ. Customizing metrics is possible only as long as Kiali's required set remains
in place. ^[raw/articles/kiali-docs-architecture.md]

## Platform / UI integrations

The kiali.io "Integrations" section (kiali.io/docs/integrations) lists two
platform integrations: ^[raw/articles/kiali-docs-integrations-index.md]

- **OpenShift Service Mesh Console (OSSMC)** — a dynamic plugin for OpenShift
  Console. Full details in [[ossmc]]: it was first released as a developer
  preview in **September 2022**, went **GA in October 2023**, and now supports
  "lite mode" (installing the OSSM Console without a Kiali server present, for
  multi-mesh navigation via the **Istios** / **Kialis** pages).
  ^[raw/articles/kiali-docs-integrations-ossm-console.md]
- **Kiali Backstage Plugin** — integrates mesh information into
  [Backstage](https://backstage.io), a developer-portal framework. It can be
  embedded as **cards** (resource lists), as a **tab** (predefined Kiali cards),
  or as a **full page** (unfiltered Kiali view), and shows mesh objects related to
  a Backstage entity. It is released as a **technology preview** in Red Hat
  Developer Hub. Docs and development guide live under
  `backstage/community-plugins .../workspaces/kiali`.
  ^[raw/articles/kiali-docs-integrations-kiali-backstage-plugin.md]

## AI / MCP integration

**Kiali MCP** exposes Kiali's mesh data to MCP-capable AI assistants *outside* the
Kiali UI (e.g. inside an IDE). It is implemented by the **Kubernetes MCP Server**
(`containers/kubernetes-mcp-server`) and the **OpenShift MCP server**
(`openshift/openshift-mcp-server`), both of which expose a **`kiali` toolset**
(documented at `docs/KIALI.md` in the kubernetes-mcp-server repo). This is the
external counterpart to the in-UI **Kiali Chatbot** — see the full feature
treatment, provider configuration, and the 12 built-in MCP tools in
[[kiali-ai-chat-and-mcp]].
^[raw/articles/kiali-docs-ai-kiali-mcp.md]

## Related

- [[kiali-features]] — the feature map these integrations power.
- [[ossmc]] — the OpenShift Console plugin (entity page).
- [[kiali-ai-chat-and-mcp]] — the in-UI chatbot and external MCP toolset.
- [[kiali-installation]] — how to deploy Kiali and wire these backends.
- [[kiali-governance-community]] — how the project and these integrations are
  maintained upstream.
