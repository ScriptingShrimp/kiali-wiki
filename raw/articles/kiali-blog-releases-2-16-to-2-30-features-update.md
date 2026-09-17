---
source_url: https://medium.com/kialiproject/kiali-releases-2-16-to-2-30-features-update-5451d32b1b68
ingested: 2026-09-17
sha256: 37cde5fa42461d0d4ff4c5f71a985ce35f2f8dd439b6671daec5123730d5f377
completeness: partial (Cloudflare-walled; sections 1-2 captured verbatim, post continues beyond section 2)
author: Hayk Hovsepyan
published: 2026-08-04
---

# Kiali releases 2.16 to 2.30: Features update

> **Note on completeness:** This post is published on Medium, which is behind a
> Cloudflare challenge. The extraction below captured the opening and sections
> 1 (AI Assistant & MCP Integration) and 2 (UX & PatternFly 6 Migration)
> verbatim; the remainder of the post was not retrievable (extraction is
> truncated mid-sentence in section 2, and the Wayback Machine was returning
> 429/503 errors at ingest time). The full per-release feature list for
> v2.16–v2.30 is instead captured verbatim from the official Kiali release notes
> at kiali.io/news/release-notes (saved as kiali-docs-news-release-notes.md),
> which covers the same 15 releases with per-version feature entries.

Source: https://medium.com/kialiproject/kiali-releases-2-16-to-2-30-features-update-5451d32b1b68
Author: Hayk Hovsepyan — Kiali (Medium publication "Kiali")
Published: 2026-08-04

---

Hello Kiali community!

It has been an extraordinary sequence of 15 releases! From Kiali v2.16 through v2.30, the team has delivered major infrastructure, visual, observability, and AI milestones.

Whether you are running Kiali standalone, integrated into OpenShift Service Mesh Console (OSSMC), or managing enterprise Ambient meshes across multi-cluster environments, this cycle brings massive upgrades.

If you missed any of our live bi-weekly sprint demos, catch up on our recorded sessions on the Kiali YouTube Channel. Below is breakdown of major features introduced across these 15 releases!

## 1. AI Assistant & MCP Integration

Artificial Intelligence and Model Context Protocol (MCP) integrations were a central focus during past releases:

- Kiali AI Chatbot Widget & Streaming (SSE): Built-in chat drawer with support for OpenAI and Google Gemini providers, including Server-Sent Events (SSE) streaming for real-time responses, tool execution UI indicators, and multi-cluster awareness.
- Kiali MCP Server (Dev Preview & Ambient Tools): We introduced Kiali's Model Context Protocol (MCP) server integration (`containers/kubernetes-mcp-server` & `openshift/openshift-mcp-server`), allowing AI tools to retrieve Istio configs, cluster resources, mesh status, logs, metrics, and traces. In v2.28–v2.29, we added `analyze_ambient_policies` to expose L4/L7 policy details, ztunnel status, waypoint proxy data, and Ambient traffic graphs to LLM agents.

## 2. UX & PatternFly 6 Migration

We executed a major modernization of Kiali's user interface and frontend tooling:

- PatternFly 6 (PF6) Migration (v2.20–v2.21): Refreshed Kiali's visual layout with PatternFly 6 patterns, introducing a new Notification Center, modernized Masthead status icons, updated Traffic Shifting Wizards (easier request mirroring), and upgraded PF Select dropdowns.
- Redesigned Overview & Namespaces Pages (v2.23): Overhauled the main Overview page into a compact, card-based dashboard for instant health summaries. The multi-cluster namespace list was split into a dedicated Namespaces Page equipped with sorting, filtering, and mTLS indicators.
- Manage Columns Modal (v2.28): Added column customization (show, hide, and reorder) to the Applications, Services, and Workloads list pages in both standalone Kiali and OSSMC plugins.
- Detail Pages UX Redesign (v2.27): Updated Overview tabs for Applications, Services, and Workloads with clearer card layouts, easier [TRUNCATED — original post continues but was not retrievable]
