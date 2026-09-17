---
source_url: https://kiali.io/docs/ai/kiali-mcp/
ingested: 2026-09-17
sha256: 33369273e0863f81023d6d7123553a363c8b37b630cbc92d588d8ebc671ce04b
---

# Kiali MCP

Expose Kiali capabilities to AI assistants using the Model Context Protocol (MCP).

Kiali MCP is an integration that allows MCP-capable AI assistants to query (and optionally manage) Kiali-related data by calling tools exposed by an MCP server.

The implementation is provided as part of the [Kubernetes MCP Server](https://github.com/containers/kubernetes-mcp-server) upstream and also for [Openshift MCP server](https://github.com/openshift/openshift-mcp-server). It exposes a **`kiali` toolset** (see upstream guide: [docs/KIALI.md](https://github.com/containers/kubernetes-mcp-server/blob/main/docs/KIALI.md)).

### Prerequisites

  * A reachable Kiali endpoint (Route/Ingress/Service URL).
  * Kubernetes credentials available to the MCP server (kubeconfig or in-cluster config).

### Enable the `kiali` toolset

Create a TOML config file and enable `kiali` in `toolsets`.


    toolsets = ["core", "kiali"]

    [toolset_configs.kiali]
    url = "https://kiali.example" # Endpoint/route to reach the Kiali console
    # insecure = true  # optional: allow insecure TLS (not recommended in production)
    # certificate_authority = "/path/to/ca.crt"  # CA bundle for Kiali's TLS cert


Notes:

  * If `url` is `https://` and `insecure = false`, you must provide `certificate_authority`.
  * Authentication to Kiali is performed using the server’s Kubernetes credentials (it obtains/uses a bearer token for Kiali calls).

### Connect from an MCP client

How you wire this into a specific client depends on the client, but the core idea is the same: start the MCP server with your kubeconfig and your TOML config.

Example (conceptual) command:


    kubernetes-mcp-server --config /path/to/config.toml --read-only


Once connected, your assistant can use the Kiali tools (for example: mesh graph, metrics, traces, workload logs) to power a chatbot-like experience outside the Kiali UI (for example, in an IDE).

Last modified March 3, 2026: [[AI] Add AI section (#955) (962121c)](https://github.com/kiali/kiali.io/commit/962121cfea4dd6d33b085525903562560e1a31e0)
