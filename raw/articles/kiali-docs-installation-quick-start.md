---
source_url: https://kiali.io/docs/installation/quick-start/
ingested: 2026-09-17
sha256: 73a31096575d7800c548e663d29fe39c1f7fc510891096b13629283f282456b4
---

# Quick Start

Installing Kiali for demo or evaluation.

## Run Kiali locally

Kiali can be run directly on your machine without being installed into a Kubernetes cluster. It uses your kubeconfig to connect to your cluster(s). If needed, it can port-forward into the cluster to connect to your external services (prometheus, tracing, istio, grafana).

Download the Kiali binary from the [Kiali GitHub releases page](https://github.com/kiali/kiali/releases/latest) for your OS and Arch.

Start Kiali which runs the backend server on localhost and opens your default browser to the Kiali UI.


    kiali run


To see the full list of options


    kiali run --help


If you want to run Kiali locally without a Prometheus instance, use the `--disable-prometheus` flag:


    kiali run --disable-prometheus


This is useful for quickly exploring Kiali’s non-metrics features (workloads, services, Istio configuration, mesh topology) without needing a Prometheus deployment. See [Disabling Prometheus](/docs/configuration/p8s-jaeger-grafana/prometheus/#disabling-prometheus) for more details.

## Install Kiali

You can quickly install Kiali into your cluster via one of the following two methods.

### Install via Istio Addons

If you [downloaded Istio](https://istio.io/latest/docs/setup/getting-started/#download), the easiest way to install and try Kiali is by running:


    kubectl apply -f ${ISTIO_HOME}/samples/addons/kiali.yaml


To uninstall:


    kubectl delete -f ${ISTIO_HOME}/samples/addons/kiali.yaml --ignore-not-found


### Install via Helm

To install the latest version of Kiali Server using [Helm](https://helm.sh/), run the following command:


    helm install \
      --namespace istio-system \
      --set auth.strategy="anonymous" \
      --repo https://kiali.org/helm-charts \
      kiali-server \
      kiali-server


To uninstall:


    helm uninstall --namespace istio-system kiali-server


## Access to the UI

Run the following command:


    kubectl port-forward svc/kiali 20001:20001 -n istio-system


Then, access Kiali by visiting https://localhost:20001/ in your preferred web browser.

Last modified May 5, 2026: [Add ability to enable/disable Prometheus via external_services.prometheus.enabled (#967) (4a48f26)](https://github.com/kiali/kiali.io/commit/4a48f267476d991f8a3445c645442fc078d8b5f9)
