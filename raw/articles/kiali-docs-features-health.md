---
source_url: https://kiali.io/docs/features/health
ingested: 2026-09-17
sha256: e2ada191eb2575395720a3647c861a7e374f6be65fdd417aec3f60f8b843de61
---

# Health

How Kiali reflects your Service Mesh Health.

Kiali help users know whether their service mesh is healthy. This includes the health of the mesh infrastructure itself, and the deployed application services.

## Service Mesh Infrastructure Health

Users can quickly confirm the health of their infrastructure by looking at the Kiali Masthead. If Kiali detects any health issues with the infrastructure of the mesh, including multi-cluster setups, it will show an indication in the masthead, severity will be reflected via color, and hovering will show the detail:

![Masthead Health](/images/documentation/features/health-masthead.png)

For more detail on how Kiali tracks the Istio infrastructure status, see the [Istio Status Feature](/docs/features/istio-component-status/).

## Overview Health

The default Kiali page is an Overview Dashboard. This view will quickly allow you to identify components with issues, including clusters, Istio configuration, control planes and data planes. It provides a chart showing all applications grouped by health, and Service Insights showing the services with the top error rates and p95 latencies.

![Overview Health](/images/documentation/features/health-overview.png)

## Graph Health

The Kiali Graph offers a rich visualization of your service mesh traffic. The health of Nodes and Edges is represented via a standard color system using shades of orange and red to reflect degraded and failure-level traffic health. Red or orange nodes or edges may need attention. The color of an edge represents the request health between the relevant nodes. Note that node shape indicates the type of component, such as service, workload, or app.

The health of nodes and edges is refreshed automatically based on the user’s desired refresh interval. The graph can also be paused to examine a particular state, or replayed to re-examine a particular time period.

![Graph Health](/images/documentation/features/health-graph.png)

## Health Configuration

Kiali calculates health by combining the individual health of several indicators, such as pods and request traffic. The _global health_ of a resource reflects the most severe health of its indicators.

### Health Indicators

The table below lists the current health indicators and whether the indicator supports custom configuration for its health calculation.

Indicator | Supports Configuration
---|---
Pod Status | No
Traffic Health | Yes


### Icons and colors

Kiali uses icons and colors to indicate the health of resources and associated request traffic.

  * ![](/images/documentation/health-configuration/no_health.png) No Health Information (NA)
  * ![](/images/documentation/health-configuration/healthy.png) Healthy
  * ![](/images/documentation/health-configuration/degraded.png) Degraded
  * ![](/images/documentation/health-configuration/failure.png) Failure

### Custom Request Health

There are times when Kiali’s default thresholds for traffic health do not work well for a particular situation. For example, at times 404 response codes are expected. Kiali has the ability to set powerful, fine-grained overrides for health configuration. For details, see [Traffic Health Configuration](https://kiali.io/docs/configuration/health/).

Last modified March 4, 2026: [Changes related to the new overview page (#956) (9014c0c)](https://github.com/kiali/kiali.io/commit/9014c0cc44260ecca7b14d23c4e4939f22c9e14d)
