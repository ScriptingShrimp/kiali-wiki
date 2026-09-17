---
source_url: https://kiali.io/docs/features/wizards
ingested: 2026-09-17
sha256: 1afb099051e3edad80b1981843956124c1a5d83537ef2686469786fa9e69d7da
---

# Application Wizards

Using Kiali wizards to generate application and request routing configuration.

## Istio Application Wizards

Kiali provides _Actions_ to create, update and delete Istio configuration, driven by wizards.

Actions can be applied to a _Service_

![Service Detail Actions](/images/documentation/features/actions-service.png)

Actions can also be applied to a _Workload_

![Workload Detail Actions](/images/documentation/features/actions-workload.png)

And, actions are available for an entire _Namespace_

![Namespace Actions](/images/documentation/features/actions-namespace.png)

## Service Actions

Kiali offers a robust set of service actions, with accompanying wizards.

### Traffic Management: Request Routing

The Request Routing Wizard allows creating multiple routing rules.

  * Every rule is composed of a _Request Matching_ and a _Routes To_ section.
  * The Request Matching section can add multiple filters using HEADERS, URI, SCHEME, METHOD or AUTHORITY HTTP parameters.
  * The Request Matching section can be empty, in this case any HTTP request received is matched against this rule.
  * The Routes To section can specify the percentage of traffic that is routed to a specific workload.

![Request Routing](/images/documentation/features/actions-service-request-routing.png)

Istio applies routing rules in order, meaning that the first rule matching an HTTP request (top-down) performs the routing. The Matching Routing Wizard allows changing the rule order.

### Traffic Management: Fault Injection

The Fault Injection Wizard allows injecting faults to test the resiliency of a Service.

  * HTTP Delay specification is used to inject latency into the request forwarding path.
  * HTTP Abort specification is used to immediately abort a request and return a pre-specified status code.

![Fault Injection](/images/documentation/features/actions-service-fault-injection.png)

### Traffic Management: Traffic Shifting

The Traffic Shifting Wizard allows selecting the percentage of traffic that is routed to a specific workload.

![Traffic Shifting](/images/documentation/features/actions-service-traffic-shifting.png)

### Traffic Management: Request Timeouts

The Request Timeouts Wizard sets up request timeouts in Envoy, using Istio.

  * HTTP Timeout defines the timeout for a request.
  * HTTP Retry describes the retry policy to use when an HTTP request fails.

![Request Timeouts](/images/documentation/features/actions-service-request-timeout.png)

### Traffic Management: Gateways

Traffic Management Wizards have an Advanced Options section that can be used to extend the scenario.

One available Advanced Option is to expose a Service to external traffic through an existing Gateway or to create a new Gateway for this Service.

![Gateway](/images/documentation/features/actions-service-advanced-gateway.png)

### Traffic Management: Circuit Breaker

Traffic Management Wizards allows defining Circuit Breakers on Services as part of the available Advanced Options.

  * Connection Pool defines the connection limits for an upstream host.
  * Outlier Detection implements the Circuit Breaker based on the consecutive errors reported.

![Circuit Breaker](/images/documentation/features/actions-service-advanced-circuit-breaker.png)

### Routing Rules Preview

Kiali provides a safe preview environment where users can review the complete YAML definition of the routing configuration and edit the configuration inline before creating.

![Preview Configuration](/images/documentation/features/actions-service-preview.png)

### Security: Traffic Policy

Traffic Management Advanced Options allows defining Security and Load Balancing settings.

  * TLS related settings for connections to the upstream service.
  * Automatically generate a PeerAuthentication resource for this Service.
  * Load balancing policies to apply for a specific destination.

![Traffic Policy](/images/documentation/features/actions-service-advanced-traffic-policy.png)

## Workload Actions

### Automatic Sidecar Injection

A _Workload_ can be individually managed to control the Sidecar Injection.

A default scenario is to indicate this at _Namespace_ level but there can be cases where a _Workload_ shouldn’t be part of the Mesh or vice versa.

Kiali allows users to alter the Deployment template and propagate this configuration into the Pods.

![Workload-specific Disable Sidecar Injection](/images/documentation/features/actions-workload-disable-injection.png)

## Namespace Actions

The Kiali Namespaces page (Kiali >= 2.23) offers several _Namespace_ actions.

![Namespace Actions](/images/documentation/features/actions-namespace.png)

### Show

Show actions navigate from a _Namespace_ to its specific Graph, Applications, Workloads, Services or Istio Config pages.

### Automatic Sidecar Injection

When [Automatic Sidecar Injection](https://istio.io/latest/docs/setup/additional-setup/sidecar-injection) is enabled in the cluster, a _Namespace_ can be labeled to enable/disable the injection webhook, controlling whether new deployments will automatically have a sidecar.

### Canary Istio upgrade

When [Istio Canary revision](https://istio.io/latest/docs/setup/upgrade/canary) is installed, a _Namespace_ can be labeled to that canary revision, so the sidecar of canary revision will be injected into workloads of the namespace.

### Security: Traffic Policies

Kiali can generate Traffic Policies based on the traffic for a namespace.

For example, at some point a namespace presents a traffic graph like this:

![Traffic Policies: Graph](/images/documentation/features/actions-namespace-trafficpolicies-graph.png)

And a user may want to add Traffic Policies to secure that communication. In other words, to prevent traffic other than that currently reflected in the Graph’s Services and Workloads.

Using the _Create Traffic Policies_ action on a namespace, Kiali will generate AuthorizationPolicy resources per every _Workload_ in the _Namespace_.

![Traffic Policies: Sidecars and Authorization Policies](/images/documentation/features/actions-namespace-trafficpolicies-config.png)

Last modified March 4, 2026: [Changes related to the new overview page (#956) (9014c0c)](https://github.com/kiali/kiali.io/commit/9014c0cc44260ecca7b14d23c4e4939f22c9e14d)
