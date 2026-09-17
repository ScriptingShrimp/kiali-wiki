---
title: Kiali Operator
created: 2026-09-17
updated: 2026-09-17
type: entity
tags: [kiali, kubernetes, operator, helm, configuration, reference]
sources: [raw/articles/kiali-docs-installation-guide.md, raw/articles/kiali-repo-readme.md, raw/articles/kiali-kep-multicluster.md, raw/articles/kiali-docs-architecture.md, raw/articles/kiali-docs-ossmc-navigating-multiple-meshes.md]
confidence: high
---

# Kiali Operator

A **Kubernetes Operator** that manages the Kiali deployment lifecycle in-cluster.
It is the **recommended production install path** for Kiali. The operator is a
separate codebase in the **`kiali/kiali-operator`** GitHub repo (the main
`kiali/kiali` repo builds the server; the operator is a sibling repo, and the
`kiali/helm-charts` repo holds the plain-Kubernetes Helm charts).
^[raw/articles/kiali-repo-readme.md]

## What it is and where it fits

The operator is a [Kubernetes
Operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) that
**watches the Kiali Custom Resource (Kiali CR)** — a YAML file that holds the
deployment configuration — and reconciles the Kiali server deployment to match it.
It does not hold Kiali's own runtime data; the **back-end has no storage of its
own**, and Kiali's runtime configuration comes from the Kiali CR (operator install)
or a ConfigMap (Helm install).
^[raw/articles/kiali-docs-installation-guide.md]^[raw/articles/kiali-docs-architecture.md]

The operator manages the **Kiali Server**; it also reconciles the
**OSSMConsole CR** that installs the OpenShift Service Mesh Console plugin (see
[[ossmc]]).

## Install paths

The operator can be installed two ways (see [[kiali-installation]] for the full
guide): ^[raw/articles/kiali-docs-installation-guide.md]

- **Helm charts** — install the operator (or the standalone Kiali Server) via
  `kiali/helm-charts`. For a server-only eval install:
  `helm install --namespace istio-system --set auth.strategy="anonymous" --repo
  https://kiali.org/helm-charts kiali-server kiali-server`.
- **OperatorHub** — install the operator through OperatorHub (the OpenShift/OKD
  operator marketplace path).

Once the operator is installed, you **create a Kiali CR** to instruct it to
deploy a Kiali server, and **create an OSSMConsole CR** to install the OSSMC
plugin. Both CRs are declarative: editing them is how you update the deployment.

## The Kiali CR (deployment config surface)

The Kiali CR is the single source of truth for how a Kiali server is deployed.
The deployment-level `spec` surface (full detail in [[kiali-installation]])
covers:

- `spec.deployment.namespace` — install in a different namespace than the CR.
- `spec.deployment.instance_name` — prefix for multi-Kiali-on-one-cluster.
- `spec.deployment.logger.{log_level, log_format, time_field_format}` +
  `spec.server.audit_log` — logging and audit-log toggles.
- `spec.deployment.resources` — CPU/memory requests and limits.
- `spec.deployment.{pod_labels, pod_annotations, service_annotations}` —
  additional labels/annotations.
- `spec.deployment.{replicas, hpa, node_selector, affinity, tolerations,
  priority_class_name}` — scheduling, autoscaling, node placement.
- `spec.server.{address, port, gzip_enabled, cors_allow_all, metrics_enabled,
  metrics_port}` — HTTP and metrics servers.
- `spec.installation_tag` — browser title-bar text.

Complex settings (authentication, custom ingress, service type, namespace
management) have dedicated upstream pages and are not repeated here.

## Multi-cluster behavior

In a **multi-cluster** deployment the operator's role is deliberately narrow
(see the multicluster KEP, `design/KEPS/multicluster/proposal.md`):
^[raw/articles/kiali-kep-multicluster.md]

- The operator is used **only to configure the Kiali server itself**. It is
  assumed the operator does **not** have access to the other mesh clusters, so
  configuring multi-cluster access is a **manual operation** and **the operator is
  unchanged** in a multi-cluster deployment.
- Remote-cluster access is configured by **manually creating remote-cluster
  secrets** in the Kiali deployment namespace (normally `istio-system`). A hack
  script (`hack/istio/multicluster/kiali-prepare-remote-cluster.sh`) can generate
  the remote clusterrole/clusterrolebinding/serviceaccount/secret.
- **By default the operator auto-discovers all remote-cluster secrets** in the
  Kiali deployment namespace (label `kiali.io/multiCluster=true`) and **mounts
  them into the Kiali server pod at install time**; the server reads the
  connections from the mounted secrets at startup. The Helm chart does the same for
  server-only installs.
- Kiali **does not reuse istioctl-generated** remote-cluster secrets
  (`istioctl x create-remote-secret`): those bind to `istio-reader-service-account`
  (insufficient permissions), and the hardcoded `istio/multiCluster=true` label
  would cause Kiali to auto-discover both a working and a broken secret. Kiali
  uses its own `kiali.io/multiCluster=true` label instead.

## Developer workflow (building the operator)

From the repo README: clone `kiali/kiali`, `kiali/kiali-operator`, and
`kiali/helm-charts` side by side and **symlink the operator into the main repo**
(`ln -s $KIALI_SOURCES/kiali-operator kiali/operator`), then:
^[raw/articles/kiali-repo-readme.md]

```
make cluster-push          # build+push kiali-server AND kiali-operator images
# make cluster-push-kiali  # server image only
# make cluster-push-operator # operator image only
make operator-create       # deploy the operator to the cluster
make kiali-create          # create a Kiali CR so the operator deploys Kiali
```

`make kiali-reload-image` reloads the server image into the cluster. Dev
bring-up scripts (`hack/run-integration-tests.sh`, `hack/k8s-minikube.sh`,
`hack/start-kind.sh`, `hack/crc-openshift.sh`) install Istio + Bookinfo on
minikube/OKD/KinD for local testing.

## Key facts

| Field | Value |
|---|---|
| Repo | `github.com/kiali/kiali-operator` (separate from `kiali/kiali`) |
| Companion repos | `kiali/kiali` (server), `kiali/helm-charts` (Helm) |
| CRD | Kiali CR (`kiali.io` group) — the deployment spec; OSSMConsole CR for OSSMC |
| Install | Helm charts or OperatorHub |
| Multi-cluster | Unchanged; manual remote-cluster secrets, auto-discovered & mounted |
| Server config | No storage; CR (operator) or ConfigMap (Helm) |

## Related

- [[kiali]] — the project entity and repo map.
- [[kiali-installation]] — full install guide (Helm, OperatorHub, Kiali CR,
  OSSMConsole CR, exposing the UI).
- [[ossmc]] — the plugin the operator also installs via the OSSMConsole CR.
- [[kiali-governance-community]] — who maintains the operator upstream.
