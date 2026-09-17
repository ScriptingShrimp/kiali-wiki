---
source_url: https://kiali.io/docs/architecture/terminology/concepts/
ingested: 2026-09-17
sha256: 4c0ca0df24659b8abbc49150db37a9bc8034485a2c01c944168d42b7a9abbcfc
---

# Concepts

Shared vocabulary for Kubernetes, Istio and Kiali.

### Application

Is a logical grouping of Workloads defined by the application labels that users apply to an object. In Istio it is defined by the Label App. See [Istio Label Requirements](https://istio.io/docs/setup/kubernetes/spec-requirements/).

### Application Name

It’s the name of the Application deployed in your environment. This name is provided by the Label App on the Workload.

### Envoy

A proxy that Istio starts for each pod in the service mesh. For more information see the [Istio Envoy Documentation](https://istio.io/docs/ops/deployment/architecture/#envoy).

### Envoy Health

A health check performed by Envoy proxies, for inbound and outbound traffic: see membership_healthy and membership_total from [Envoy documentation](https://www.envoyproxy.io/docs/envoy/v1.7.1/configuration/cluster_manager/cluster_stats#general).

### Istio object/configuration Type

This is the type specified in the Istio Config. This could be any of the following types: Gateway, Virtual Service, DestinationRule, ServiceEntry, Rule, Quota or QuotaSpecBinding.

### Istio Sidecar

For more information see the Istio Sidecar definition in [Istio Sidecar Documentation](https://istio.io/v1.5/docs/reference/commands/sidecar-injector/).

### Label

It’s a user-created tag to identify a set of objects.

An empty [label selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) (that is, one with zero requirements) selects every object in the collection.

A null [label selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) (which is only possible for optional selector fields) selects no objects.

For example, Istio uses the Label App & Label Version on a Workload to specify the version and the application.

### Label App

This is the ‘app’ label on an object. For more information, see [Istio Label Requirements](https://istio.io/docs/setup/kubernetes/spec-requirements/).

### Label Version

This is the ‘version’ label on an object. For more information, see [Istio Label Requirements](https://istio.io/docs/setup/kubernetes/spec-requirements/).

### Namespace

Namespaces are intended for use in environments with many users spread across multiple teams, or projects.

Namespaces are a way to divide cluster resources between multiple users.

### Quota

A limited or fixed number or amount of resources.

### ReplicaSet

Ensures that a specified number of pod replicas are running at any one time.

### Service

A Service is an abstraction which defines a logical set of Pods and a policy by which to access them. A Service is determined by a Label.

### Service Entry

For more information see the Service Entry definition in [Istio Service Entry Documentation](https://istio.io/docs/reference/config/networking/service-entry).

### Virtual Service

For more information see the Virtual Service definition in [Istio VirtualService Documentation](https://istio.io/docs/reference/config/networking/virtual-service).

### Workload

For more information see the [Istio Workload definition](https://istio.io/help/glossary/#workload).

Last modified October 28, 2021: [Some final cleanup for Epic kiali#4118 (#464) (35a3587)](https://github.com/kiali/kiali.io/commit/35a3587e1800063c25c51b52f0cbc77a3bebf57d)
