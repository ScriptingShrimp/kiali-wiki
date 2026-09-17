---
title: OpenShift Service Mesh Console (OSSMC)
created: 2026-09-17
updated: 2026-09-17
type: entity
tags: [kiali, ossmc, openshift, service-mesh, istio, kubernetes, integration, red-hat, reference]
sources: [raw/articles/kiali-docs-integrations-ossm-console.md, raw/articles/kiali-docs-ossmc-index.md, raw/articles/kiali-docs-ossmc-users-guide.md, raw/articles/kiali-docs-ossmc-navigating-multiple-meshes.md, raw/articles/kiali-docs-news-release-notes.md, raw/articles/kiali-docs-ai-kiali-chatbot.md]
confidence: high
---

# OpenShift Service Mesh Console (OSSMC)

**OSSMC** is a **dynamic plugin for the OpenShift Console** built on OpenShift's
**dynamic plugins** technology, built by the Kiali project. It gives OpenShift
users service-mesh visibility **inside the OpenShift Console** — either by
embedding the full Kiali-powered experience when a Kiali server is connected, or by
providing **multi-mesh navigation** on its own without any Kiali server.
^[raw/articles/kiali-docs-integrations-ossm-console.md]

## Key facts (as of 2026-09-17)

| Field | Value |
|---|---|
| Repo | `github.com/kiali/openshift-servicemesh-plugin` |
| What it is | OpenShift Console **dynamic plugin** (not a standalone console) |
| First release | **September 2022** — as a **developer preview** |
| **GA** | **October 2023** |
| Install | Via the **OSSMConsole CR** (reconciled by the Kiali Operator — see [[kiali-operator]]) |
| Backing Kiali | **Optional** — the plugin works in "lite mode" without a Kiali server |
| Latest plugin doc update | Aug 2026 (added "lite mode" install support, commit #1002) |

> The GA date (Oct 2023) is the authoritative milestone; do not overstate
> capabilities beyond what the docs describe. Upstream moves fast — re-verify
> feature claims against the release notes before relying on them.
> ^[raw/articles/kiali-docs-integrations-ossm-console.md]

## Two operating modes

What you see in the OpenShift Console **Service Mesh** menu depends on whether a
Kiali server is **connected and reachable** to the plugin:
^[raw/articles/kiali-docs-ossmc-users-guide.md]

- **With a connected Kiali server** — OSSMC delivers the **full Kiali-powered
  experience**: dedicated list/detail pages for mesh components, plus **Service
  Mesh** tabs on OpenShift **Workloads**, **Services**, **Projects**, and **Istio
  configuration** detail pages. The features match the standalone Kiali Console,
  re-organized to integrate with the OpenShift Console. Pages available:
  **Overview** (namespace summary with health/metric cards), **Traffic Graph**
  (full mesh topology), **Mesh** (Istio infrastructure status), **Namespaces**,
  **Applications**, **Services**, **Workloads**, and **Istio Config** (with
  validation status and full Kiali filtering). OSSMC talks to the connected Kiali
  instance **through the plugin proxy** configured on the OSSMConsole CR.
- **Without a connected Kiali server** — OSSMC still provides the **Istios** and
  **Kialis** pages, which list every Istio and Kiali **CR** on the cluster. These
  do **not** require a Kiali server and are the key to navigating many mesh
  instances from one console (see "Navigating multiple meshes" below).

If OSSMC is configured to use a Kiali server but can't reach it, the
Kiali-dependent pages show a **Service Mesh is not configured** message (pointing
you to install/configure Kiali via the Kiali Operator) while **Istios** and
**Kialis** keep working. A page-level Kiali failure shows **Service Mesh Console
Unavailable** without affecting the rest of the OpenShift Console.

The OSSMC plugin **does not replace** the standalone Kiali Console — when a Kiali
server is deployed you can still reach it through its own route.

## Navigating multiple meshes (Istios / Kialis)

**Istios** and **Kialis** are always available in the Service Mesh menu
(when a Kiali server is also connected, they sit at the bottom below a separator).
They let platform teams that run **dozens or hundreds of Istio control planes**
browse that inventory in one place instead of jumping between CLI, operator UIs, or
separate Kiali routes:
^[raw/articles/kiali-docs-ossmc-navigating-multiple-meshes.md]

- **Istios** — lists every **cluster-scoped Istio CR** managed by the OSSM/Sail
  Operator; open a row for details of that control plane.
- **Kialis** — lists every **Kiali CR** on the cluster. Each row shows:
  - **Connected** — **Active** (this Kiali is the OSSMC backend), **Inactive**, or
    **Unknown** (if OSSMConsole resources can't be read).
  - **Observe** — when route hosts are available, links to the Kiali UI and the
    OpenShift Console (**Kiali** | **Console**).
  - **Actions** — **Connect** / **Disconnect** to switch which Kiali server the
    plugin uses. **Connect** makes the Kiali-powered pages (Overview, Traffic
    Graph, Mesh, …) available for that instance; **Disconnect** stops using it,
    leaving Istios/Kialis intact so you can connect a different instance.
  - Connect/Disconnect **requires permission to patch the OSSMConsole CR**
    (`ossmconsoles.kiali.io`).

You can connect a Kiali server either via **Connect** on the Kialis page or by
setting `spec.kiali` on the OSSMConsole CR.

## Kiali-powered detail pages (when a server is connected)

The same detail sub-tabs exist as in standalone Kiali, integrated into OpenShift
pages: ^[raw/articles/kiali-docs-ossmc-users-guide.md]

- **Workload detail** (from OpenShift Deployments/Pods/ReplicaSets/StatefulSets/
  DaemonSets) — a **Service Mesh** tab with sub-tabs **Overview** (localized
  topology graph), **Traffic** (inbound/outbound), **Logs** (container logs,
  unified or individual, with trace-span correlation), **Inbound/Outbound
  Metrics** (with trace-span overlays — click a span marker to jump to the spans),
  **Traces** (drill into spans; heatmaps comparing a span against the timeframe),
  and **Envoy** (deep sidecar config for connectivity debugging). When the OpenShift
  tracing UI plugin is enabled, Kiali auto-discovers its settings (Kiali ≥ 2.8.0)
  so a **View in Tracing** link redirects to the plugin.
- **Application / Service detail** — Overview, Traffic, Inbound Metrics, Traces
  (same shape as workload, for apps/services).
- **Project detail** — a Service Mesh tab with project attributes, resource links,
  health, and a namespace-scoped traffic minigraph.
- **Istio config detail** — for VirtualService, DestinationRule, Gateway,
  AuthorizationPolicy, etc., a Service Mesh tab showing overview and validation.

## AI / chatbot in OSSMC

The **Kiali Chatbot** and MCP surface from [[kiali-ai-chat-and-mcp]] is the same
backend Kiali exposes; in OSSMC it is surfaced within the OpenShift Console.
Recent OSSMC releases (2.31/2.32) include glass/high-contrast theme support for
OpenShift 5.0, and **OSSMC: Add fleet mesh and multi-mesh capabilities**
(2.32.0) extended the multi-mesh navigation. The chatbot is **off by default**
and must be enabled via the Kiali CR (`ai.enabled` / `ai.chat.enabled`) — see
[[kiali-ai-chat-and-mcp]].
^[raw/articles/kiali-docs-news-release-notes.md]^[raw/articles/kiali-docs-ai-kiali-chatbot.md]

## Getting started (minimal)

1. Install the **Kiali Operator** (a Kiali server is *optional* for Istios/Kialis).
2. Create an **OSSMConsole CR** to install the plugin (see [[kiali-operator]] and
   the kiali.io "The OSSMConsole CR" page).
3. Open **Service Mesh → Istios / Kialis** in the OpenShift Console; connect a
   Kiali instance when you want full observability on one.

## Development

The plugin is developed in `github.com/kiali/openshift-servicemesh-plugin`
(README, issues, releases all live there). Recent work (2026) includes a
**PatternFly 6** upgrade, i18n, a Netobserv navigation side-panel, a new
"openshift" `url_format` for tracing, and the **lite-mode** install (no Kiali
server required). ^[raw/articles/kiali-docs-integrations-ossm-console.md]

## Related

- [[kiali]] — the project entity; OSSMC ships Kiali as an embedded console.
- [[kiali-operator]] — installs OSSMC via the OSSMConsole CR.
- [[kiali-features]] — the feature set OSSMC re-organizes for the OpenShift Console.
- [[kiali-ai-chat-and-mcp]] — the chatbot/MCP surface available in OSSMC.
- [[kiali-integrations]] — OSSMC in the broader integration map.
