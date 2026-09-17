---
source_url: https://kiali.io/docs/installation/installation-guide/
ingested: 2026-09-17
sha256: 17469614ff09120ffb687d61d9b6d639b82ba6fa3d60ed25a2fab1a754ff3e1a
---

# Installation Guide

Installing Kiali for production.

This section describes the production installation methods available for Kiali.

The recommended way to deploy Kiali is via the Kiali Operator, either using Helm Charts or OperatorHub.

The Kiali Operator is a [Kubernetes Operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) and manages your Kiali installation. It watches the _Kiali Custom Resource_ (Kiali CR), a YAML file that holds the deployment configuration.

* * *

#####  [Prerequisites](/docs/installation/installation-guide/prerequisites/)

Hardware and Software compatibility and requirements.

#####  [Install via Helm](/docs/installation/installation-guide/install-with-helm/)

Using Helm to install the Kiali Operator or Server.

#####  [Install via OperatorHub](/docs/installation/installation-guide/installing-with-operatorhub/)

Using OperatorHub to install the Kiali Operator.

#####  [The Kiali CR](/docs/installation/installation-guide/creating-updating-kiali-cr/)

Creating and updating the Kiali CR.

#####  [The OSSMConsole CR](/docs/installation/installation-guide/creating-updating-ossmconsole-cr/)

Creating and updating the OSSMConsole CR.

#####  [Accessing Kiali](/docs/installation/installation-guide/accessing-kiali/)

Accessing and exposing the Kiali UI.

#####  [Advanced Install](/docs/installation/installation-guide/advanced-install-options/)

Advanced installation options.

#####  [Example Install](/docs/installation/installation-guide/example-install/)

Installing two Kiali servers via the Kiali Operator.

Last modified November 3, 2023: [Fix LeftHand TOC issue (caused by readfile) (#714) (5af4989)](https://github.com/kiali/kiali.io/commit/5af49893a3874b0801aaecc71cfdebfe6b109607)
