---
title: Kiali Installation
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, kubernetes, operator, helm, configuration, reference, howto]
sources: [raw/articles/kiali-docs-installation-guide.md, raw/articles/kiali-docs-installation-quick-start.md, raw/articles/kiali-docs-installation-deployment-options.md, raw/articles/kiali-docs-architecture.md, raw/articles/kiali-docs-ai-kiali-chatbot.md]
confidence: high
---

# Kiali Installation

How to run and deploy Kiali — from a local quick-start to a production
operator-managed install. This page covers the deployment options and the
deployment-level configuration surface. The Kiali CR and the OSSMConsole CR
schemas live in the operator; see [[kiali-operator]] and the feature map in
[[kiali-features]]. As of Kiali v2.32.0 (2026-09-14).
^[raw/articles/kiali-docs-installation-guide.md]

## The two deployment models

Kiali is installed one of two ways, and the recommended path for production is
the **Kiali Operator**:

- **Kiali Operator (recommended for production)** — a Kubernetes Operator that
  watches the **Kiali Custom Resource (Kiali CR)** (a YAML holding the deployment
  configuration) and manages the Kiali lifecycle in-cluster. The operator can be
  installed via **Helm charts** or **OperatorHub**. ^[raw/articles/kiali-docs-installation-guide.md]
- **Kiali Server (Helm)** — a plain-Kubernetes install of just the Kiali server
  (no operator), configured via a Helm values file / ConfigMap. Useful for
  demos, evals, and environments without an operator. ^[raw/articles/kiali-docs-architecture.md]

> The **back-end has no storage of its own**. Its configuration comes from the
> Kiali CR (operator install) or a ConfigMap (Helm install). In a standard
> deployment the Go back-end serves the React front-end.
> ^[raw/articles/kiali-docs-architecture.md]

## Quick start (demo / evaluation)

**Run locally (no cluster install).** Kiali can run on your machine without being
installed into a cluster — it uses your kubeconfig to reach your cluster(s) and
can port-forward to external services (Prometheus, tracing, istiod, Grafana):
^[raw/articles/kiali-docs-installation-quick-start.md]

```
# download the binary from the GitHub releases page, then:
kiali run            # runs the backend on localhost, opens the browser to the UI
kiali run --help     # full option list
kiali run --disable-prometheus   # explore non-metrics features (workloads, services,
                                 # Istio config, topology) without a Prometheus
```

**Install into a cluster — two quick methods.**

Istio Addons (if you downloaded Istio):
^[raw/articles/kiali-docs-installation-quick-start.md]

```
kubectl apply -f ${ISTIO_HOME}/samples/addons/kiali.yaml
kubectl delete -f ${ISTIO_HOME}/samples/addons/kiali.yaml --ignore-not-found   # uninstall
```

Helm (Kiali Server):
^[raw/articles/kiali-docs-installation-quick-start.md]

```
helm install \
  --namespace istio-system \
  --set auth.strategy="anonymous" \
  --repo https://kiali.org/helm-charts \
  kiali-server kiali-server
helm uninstall --namespace istio-system kiali-server
```

**Access the UI** via port-forward:
^[raw/articles/kiali-docs-installation-quick-start.md]

```
kubectl port-forward svc/kiali 20001:20001 -n istio-system
# then visit https://localhost:20001/
```

## Production install (operator)

The installation guide (kiali.io/docs/installation/installation-guide) is organized
around these steps; each has its own upstream page:
^[raw/articles/kiali-docs-installation-guide.md]

1. **Prerequisites** — hardware/software compatibility and requirements.
2. **Install the operator** — via Helm charts or OperatorHub.
3. **Create/update the Kiali CR** — the deployment configuration.
4. **Create/update the OSSMConsole CR** — only if embedding Kiali in the OpenShift
   Console (see [[ossmc]]).
5. **Accessing Kiali** — expose the UI (Route/Ingress, LoadBalancer/NodePort,
   custom ingress, route `web_root` settings).
6. **Advanced install** — multi-Kiali and other advanced options; an **example
   install** of two Kiali servers via the operator is provided.

## Deployment-level configuration (Kiali CR)

The following `spec` knobs live in the Kiali CR. Complex settings (auth, ingress,
service type, namespace management) have dedicated upstream pages.
^[raw/articles/kiali-docs-installation-deployment-options.md]

- **Install namespace** — by default the operator installs Kiali where the CR is
  created; override with `spec.deployment.namespace: "custom-namespace"`.
- **Instance name** — for multiple Kiali instances on one cluster, set
  `spec.deployment.instance_name: "secondary"`; it prefixes created resources
  (the `kiali-signing-key` secret is shared per namespace unless renamed).
- **Logging** — `spec.deployment.logger.{log_level, log_format, time_field_format}`
  (levels trace..fatal; formats text/json). **Audit logs** (INFO-level, emitted on
  every create/update/delete through Kiali) are on by default; disable with
  `spec.server.audit_log: false` without lowering the global level.
- **Resources** — `spec.deployment.resources.{requests,limits}` for CPU/memory.
- **Pod/service labels & annotations** — `spec.deployment.pod_labels`,
  `spec.deployment.pod_annotations`, `spec.deployment.service_annotations`.
- **Page title** — `spec.installation_tag: "Kiali West"` sets the browser
  title-bar text (useful with multiple installs).
- **Scheduling** — replicas (`spec.deployment.replicas`), `HorizontalPodAutoscaler`
  (`spec.deployment.hpa`), `node_selector`, `affinity` (node/pod/pod_anti),
  `tolerations`, and `priority_class_name`.
- **Host aliases** — static `/etc/hosts` entries via `spec.deployment.host_aliases`.
- **HTTP server** — `spec.server.{address, port (20001 default), gzip_enabled,
  cors_allow_all}`; `spec.server.web_root` is covered under route settings.
- **Metrics server** — enabled by default on port 9090
  (`spec.server.{metrics_enabled, metrics_port}`); must not share a port with the
  HTTP server.

## Prerequisites (summary)

Kiali's hard/soft dependencies (see [[kiali-features]] for the feature map and
[[kiali-integrations]] for the ecosystem): **Istio is required**; **Prometheus**
is a hard dependency for topology/metrics/health (Kiali assumes Istio's default
telemetry metrics); the **Kubernetes/OKD API** is required; **Jaeger/Tempo**,
**Grafana/Perses** are optional. When `istiod` is inaccessible, Kiali's
communication with it can be disabled.
^[raw/articles/kiali-docs-architecture.md]

## Enabling the AI chatbot on a deploy

When deploying, the AI chatbot is **off by default**; to turn it on you must set
`ai.enabled: true` and `ai.chat.enabled: true` and configure at least one provider
+ model in the Kiali CR. Full details in [[kiali-ai-chat-and-mcp]].
^[raw/articles/kiali-docs-ai-kiali-chatbot.md]

## Open questions / watch items

- Upstream moves fast; the exact `spec` field names and defaults here are as of
  2026-09-17 and should be re-checked against the operator CRD and the
  kiali.io installation guide before relying on them.
- The OSSMConsole CR is a separate surface (OpenShift Console embedding) and is
  documented on its own upstream page — see [[ossmc]].
