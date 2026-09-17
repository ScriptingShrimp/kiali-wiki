---
source_url: https://kiali.io/docs/ai/kiali-chatbot-tools/
ingested: 2026-09-17
sha256: 83c643f6330d6bc58eeb86f554b5de92af34f112f689022582ec5bd81c8afdf0
---

# Kiali Chatbot tools (schemas)

Input/output schemas for the built-in Kiali AI tools.

Kiali Chatbot uses **internal MCP-style tools** (implemented inside Kiali) to fetch live data and perform safe actions. These are **not** external MCP server tools.

Administrators can control which of these tools are exposed to the AI by using `ai.chat.tools` for global filtering and `ai.chat.providers[].tools` for provider-specific filtering. Use the exact tool names below in `enabled_tools` and `disabled_tools`.

The tool **input schemas** are defined in Kiali under `kiali/ai/mcp/tools/*.yaml`. The tool **outputs** are JSON structures returned by the Kiali backend and consumed by the model and/or UI.

### Tool list

  * `get_action_ui`: returns UI navigation actions (buttons/links).
  * `get_logs`: returns workload or pod logs with optional filtering.
  * `get_mesh_status`: returns high-level mesh health, control plane, observability stack, and connectivity status.
  * `get_mesh_traffic_graph`: returns a compact service-to-service traffic topology with metrics such as throughput, response time, and mTLS.
  * `get_metrics`: returns Istio or Envoy metrics for services, workloads, or apps.
  * `get_pod_performance`: returns current pod CPU and memory usage versus requests and limits.
  * `get_referenced_docs`: returns relevant Istio and Kiali documentation links.
  * `get_trace_details`: returns the hierarchy and span details for a specific trace.
  * `list_or_get_resources`: lists resources or returns details for services, workloads, apps, and namespaces.
  * `list_traces`: returns a compact list of distributed traces for a service.
  * `manage_istio_config_read`: lists or gets Istio config in read-only mode.
  * `manage_istio_config`: creates, patches, or deletes Istio config with a confirmation flow for sensitive actions.

Last modified September 9, 2026: [Update AI docs with the new configuration (#1009) (56f7160)](https://github.com/kiali/kiali.io/commit/56f716098cac8c15d9f1b6fb8460ce8cd2e5cc2f)
