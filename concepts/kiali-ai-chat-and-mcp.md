---
title: Kiali AI Chatbot and MCP
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, ai, mcp, configuration, architecture, reference]
sources: [raw/articles/kiali-docs-ai-index.md, raw/articles/kiali-docs-ai-kiali-chatbot.md, raw/articles/kiali-docs-ai-kiali-chatbot-tools.md, raw/articles/kiali-docs-ai-kiali-mcp.md, raw/articles/kiali-repo-docs-agents-observability-and-ai.md, raw/articles/kiali-docs-news-release-notes.md]
confidence: high
---

# Kiali AI Chatbot and MCP

Kiali exposes its live mesh data to LLM-based AI assistants through two
surfaces: the **Kiali Chatbot** (a built-in AI assistant in the Kiali UI) and
**Kiali MCP** (an external Model Context Protocol integration for use outside
the UI, e.g. in an IDE). Both are built on the same set of **internal MCP-style
tools** that run inside the Kiali backend. This page summarizes both as of
Kiali v2.32.0 (2026-09-14). The feature set is the AI portion of the overall
feature map in [[kiali-features]] and is embedded in [[ossmc]].
^[raw/articles/kiali-docs-ai-index.md]

## Status and history

- The **Kiali Chatbot first released in Kiali v2.22.0** and is in **Dev
  Preview**; the AI section of the kiali.io docs was added in March 2026
  (commit #955). ^[raw/articles/kiali-docs-ai-kiali-chatbot.md]
- v2.22–v2.32 additions: SSE streaming of tool execution (v2.30), context
  awareness (v2.30), Ask/Troubleshoot mode selection with provider-specific
  prompts (v2.29), Gateway API support in MCP tools (v2.29), configurable max
  tool iterations (v2.29), MCP ambient-mesh discovery tools (v2.29), a
  multi-cluster MCP eval suite (v2.30), and automated MCP pin-compatibility
  validation (v2.31). ^[raw/articles/kiali-docs-news-release-notes.md]
- **`analyze_ambient_policies`** was added (v2.28–v2.29) to expose L4/L7 policy
  details, ztunnel status, waypoint proxy data, and ambient traffic graphs.
  ^[raw/articles/kiali-blog-releases-2-16-to-2-30-features-update.md]

## How the Chatbot works

High level: the UI sends the chat request (prompt + context + model) to the
backend; Kiali selects the configured provider/model from the `ai.chat` CR
section; the provider calls the LLM with the set of **internal MCP tools**
defined under `kiali/ai/mcp`; the LLM may request tool calls (graph, traces,
resources, logs, Istio config ops), which Kiali executes against
Kiali/Kubernetes/Prometheus/tracing backends; and the final answer — including
optional UI navigation actions and doc citations — is delivered as **streaming
events** (`start`, `token`, `tool_call`, `tool_result`, `end`, `error`) so the
UI progressively renders tokens and tool activity. The Chatbot does **not**
require an external MCP server — Kiali's own MCP-style tools are internal.
^[raw/articles/kiali-docs-ai-kiali-chatbot.md]

## Enabling and restricting access

The Chatbot is **disabled by default**. To enable: set `ai.enabled: true` and
`ai.chat.enabled: true`, configure at least one provider + model (with an API
key) and a default provider/model; a chatbot icon then appears in the UI.
Access is open to all users by default; to restrict, set `allowed_users` under
`ai.chat` (empty list = everyone, non-empty = allowlist).
^[raw/articles/kiali-docs-ai-kiali-chatbot.md]

## Configuring providers and models

Providers and models are configured under `ai.chat` in the Kiali CR.
Supported provider **types**: **OpenAI** (`type: openai`), **Google**
(`type: google`), **Anthropic** (`type: anthropic`), and **LightSpeed**
(`type: lightspeed`, the OpenShift-native provider). ^[raw/articles/kiali-docs-ai-kiali-chatbot.md]

- Models are selected by name (per provider) and can be enabled/disabled.
- API keys can be set inline (not recommended) or via
  `secret:<secret-name>:<key-in-secret>`.
- **Tool exposure is filterable globally** via `ai.chat.tools` and
  **further restricted per provider** via `ai.chat.providers[].tools`.
  `enabled_tools` is an allowlist; `disabled_tools` is a denylist applied
  after. Provider-level filters can only further restrict the global allowlist.
- TLS verification is on by default (using the `kiali-cabundle` ConfigMap and
  the platform TLS policy). For self-signed provider certs, set
  `insecure_skip_verify: true` per provider.
- The LightSpeed provider uses `endpoint` and is OpenShift-native (e.g.
  `https://lightspeed-app-server.openshift-lightspeed.svc:8443`).

The internal code implements three provider types (OpenAI, Anthropic, Google)
under `ai/providers/`, with the OpenAI provider additionally supporting
OpenAI-compatible `gemini` (Google's OpenAI endpoint) and `azure` backends.
All three propagate tool-execution errors and share conversation-reduction
helpers. The Anthropic provider caps tool-call rounds at 5
(`maxToolIterations = 5`), and the AI store rejects conversations that alone
exceed `MaxCacheMemoryMB` (default 1024 MB). ^[raw/articles/kiali-repo-docs-agents-observability-and-ai.md]

## What you can ask & mode

The chatbot shows **suggested prompts tailored to the page you are viewing**
(Overview, Graph, Mesh, Namespaces, Applications, Services, Workloads, Istio
Config) via `GET /api/chat/prompts` (optional `?category=<page>`, static
fallback if unavailable); they prefill the input for review/edit before sending.
Working examples: "Show me the mesh graph for namespace `bookinfo`"; "Which
workloads in `istio-system` look unhealthy and why?"; "Get traces for service
`productpage` in `bookinfo` for the last 30m."

The input has a **mode selector**: **Ask mode** (conversational, free-form) and
**Troubleshoot mode** (structured diagnostic — accepts a problem description,
auto-selects a relevant tool set (logs, traces, metrics, Istio config checks),
follows a systematic diagnostic workflow, and summarizes findings with a
recommended course of action). For LightSpeed the modes are handled natively by
the provider; for other models the system prompt is adapted per mode.
^[raw/articles/kiali-docs-ai-kiali-chatbot.md]

## The 12 built-in MCP tools

The Chatbot uses **internal MCP-style tools** implemented inside Kiali — not
external MCP server tools. Input schemas live in `kiali/ai/mcp/tools/*.yaml`
(embedded via `//go:embed tools`); outputs are JSON returned by the backend and
consumed by the model and/or UI. Administrators control exposure with
`ai.chat.tools` (global) and `ai.chat.providers[].tools` (per provider), using
the exact tool names below. ^[raw/articles/kiali-docs-ai-kiali-chatbot-tools.md]

| # | Tool name | Purpose |
|---|---|---|
| 1 | `get_action_ui` | Returns UI navigation actions (buttons/links) — **UI-only**. |
| 2 | `get_logs` | Workload/pod logs with optional filtering. |
| 3 | `get_mesh_status` | High-level mesh health, control plane, observability stack, connectivity. |
| 4 | `get_mesh_traffic_graph` | Compact service-to-service topology with throughput, RT, mTLS. |
| 5 | `get_metrics` | Istio/Envoy metrics for services, workloads, or apps. |
| 6 | `get_pod_performance` | Current pod CPU/memory vs requests and limits. |
| 7 | `get_referenced_docs` | Relevant Istio/Kiali doc links — **UI-only**. |
| 8 | `get_trace_details` | Hierarchy and span details for a specific trace. |
| 9 | `list_or_get_resources` | List or get services, workloads, apps, namespaces. |
| 10 | `list_traces` | Compact list of distributed traces for a service. |
| 11 | `manage_istio_config_read` | List or get Istio config (read-only). |
| 12 | `manage_istio_config` | Create/patch/delete Istio config, with a confirmation flow for sensitive actions. |

Two special exclusions: `get_referenced_docs` and `get_action_ui` are kept in
`ExcludedToolNames` and are **excluded from the external MCP server tool
listing** because they are UI-specific. Tools requiring Prometheus are tracked in
`MetricToolNames`; tools requiring a tracing backend in `TraceToolNames`; the
handler checks the relevant `config` flags before running and returns a helpful
error when the dependency is disabled. ^[raw/articles/kiali-repo-docs-agents-observability-and-ai.md]

The internal MCP tool system is declarative: each YAML file defines a
`ToolDef` (name, description, input JSON Schema, toolset `"default"` / `"mcp"`
/ both). On first use, `LoadTools()` populates two maps — `MCPToolHandlers`
(tools in the `"mcp"` toolset, used when Kiali acts as an MCP server) and
`DefaultToolHandlers` (tools in the `"default"` toolset, used by the built-in
chat UI); the `Kiali-UI` HTTP header tells the backend the caller is the
internal UI client and selects the `default` handler set. The **AI conversation
store** (`ai/store.go`) keeps conversations in memory with LRU eviction against
`MaxCacheMemoryMB`, inactivity-based session purging (default 30 m), optional
AI-based conversation reduction at a 15-message threshold, and a system-prompt
section telling the LLM to treat tool output as untrusted data (prompt-injection
defense). ^[raw/articles/kiali-repo-docs-agents-observability-and-ai.md]

## Kiali MCP (external, Model Context Protocol)

**Kiali MCP** exposes Kiali capabilities to MCP-capable AI assistants *outside*
the Kiali UI (e.g. in an IDE). It is implemented by the **Kubernetes MCP Server**
(`containers/kubernetes-mcp-server`) and the **OpenShift MCP server**
(`openshift/openshift-mcp-server`); both expose a **`kiali` toolset**
documented at `docs/KIALI.md` in the kubernetes-mcp-server repo.
^[raw/articles/kiali-docs-ai-kiali-mcp.md]

Prerequisites: a reachable Kiali endpoint (Route/Ingress/Service URL) and
Kubernetes credentials available to the MCP server (kubeconfig or in-cluster).
Enable the `kiali` toolset in a TOML config:

```toml
toolsets = ["core", "kiali"]

[toolset_configs.kiali]
url = "https://kiali.example"   # endpoint/route to reach the Kiali console
# insecure = true              # optional, allow insecure TLS (not recommended)
# certificate_authority = "/path/to/ca.crt"  # required if https and not insecure
```

If `url` is `https://` and `insecure = false`, you **must** provide
`certificate_authority`. Auth to Kiali uses the server's Kubernetes credentials
(it obtains/uses a bearer token for Kiali calls). To connect, start the MCP
server with your kubeconfig and TOML config, e.g.
`kubernetes-mcp-server --config /path/to/config.toml --read-only` (wiring is
client-specific); once connected the assistant can use the Kiali tools (mesh
graph, metrics, traces, workload logs) for a chatbot-like experience outside
the UI. ^[raw/articles/kiali-docs-ai-kiali-mcp.md]

## Internal API surface (backend)

Endpoints (gated by `conf.ChatAI.Enabled`): `POST /api/chat/{provider}/{model}/ai`
(send a query, get an AI response); `POST /api/chat/mcp/{tool_name}` (call a
single MCP tool, used by the UI); `GET /api/chat/conversations` (list the
session's conversation IDs);
`DELETE /api/chat/conversations?conversationIDs=<id1,id2,...>` (delete
conversations); `GET /api/chat/prompts` (suggested prompts, optional
`?category=<page>`).
^[raw/articles/kiali-repo-docs-agents-observability-and-ai.md]

## Related

- [[kiali-features]] — the AI surface in the broader feature map.
- [[ossmc]] — the same chatbot/MCP surface embedded in the OpenShift Console.
- [[kiali-installation]] — how to deploy Kiali with AI enabled.
- [[kiali-governance-community]] — how these features are built and released.
