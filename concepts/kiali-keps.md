---
title: Kiali Enhancement Proposals (KEPs)
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, kep, design, roadmap, reference]
sources: [raw/articles/kiali-kep-proposal.md, raw/articles/kiali-repo-keps-index.md, raw/articles/kiali-kep-graph-cache.md, raw/articles/kiali-kep-health-precompute.md, raw/articles/kiali-kep-metric-rules.md, raw/articles/kiali-kep-multicluster.md, raw/articles/kiali-kep-extensions.md, raw/articles/kiali-kep-ai-store.md, raw/articles/kiali-kep-controller-model.md, raw/articles/kiali-kep-multi-session-auth.md, raw/articles/kiali-kep-namespace-discovery.md, raw/articles/kiali-docs-news-release-notes.md]
confidence: high
---

# Kiali Enhancement Proposals (KEPs)

How large, cross-cutting design changes get proposed, reviewed, accepted, and
tracked in the Kiali project. Kiali KEPS (Kiali Enhancement Proposals) live in
the `design/KEPS/` directory of the `kiali/kiali` repository, and the process
is defined by the **meta-KEP** `design/KEPS/kiali-enhancement-proposal/` (the
proposal template itself, originating from
[kiali/kiali discussion #4208](https://github.com/kiali/kiali/discussions/4208)).
^[raw/articles/kiali-kep-proposal.md]

## Why the KEP process exists

Kiali historically relied on GitHub discussions and Slack to discuss large
enhancements. That works informally, but it has three problems the KEP process
addresses: it is unclear **when a discussion becomes an implementation
commitment**; understanding and agreeing to a proposal spread across many
discussion threads is hard; and there is **no versioned, searchable, durable
record** of how a proposal evolved as feedback was addressed. ^[raw/articles/kiali-kep-proposal.md]

**Goals:** give features a natural path from discussion to implementable
proposal; make it easy to formally present a large enhancement, get feedback,
and reach consensus; keep proposals versioned and searchable; keep the process
public; and establish **owners and a roadmap** for each proposal.

**Non-goals:** the KEP process does *not* impose a strict process on all
changes, large or small — its purpose is to speed up and refine *large*
features by making pre-implementation design collaboration easier, not to add
burden. It also does *not* replace GitHub discussions: most large features are
expected to start as informal discussions that graduate into formal proposals.
^[raw/articles/kiali-kep-proposal.md]

## The process (seven steps)

As defined in the meta-KEP: ^[raw/articles/kiali-kep-proposal.md]

1. **Submit** — the proposal owner opens a PR to the kiali/kiali repo
   containing a **single markdown file** describing the proposal (using the
   meta-KEP as a template), plus any supporting material (diagrams, pictures,
   videos), all organized under **one directory** in `design/KEPS/` (e.g.
   `design/KEPS/<feature>/proposal.md`).
2. **Assign** — the owner assigns `kiali/maintainers` as **reviewers** on the
   PR and assigns themself (and any co-owners) as **assignees**.
3. **Feedback** — maintainers provide timely feedback via GitHub PR reviews.
4. **Iterate** — the owner responds and updates the proposal by adding commits
   to the PR.
5. **Present (optional)** — pending proposals may be discussed and presented
   at the end-of-sprint meetings.
6. **Decide** — after feedback is sufficiently addressed, maintainers **accept
   or reject** the proposal.
7. **Implement** — the accepted proposal is broken down into **epics/issues**
   and implemented; **the roadmap is updated along the way**.

Both owners and maintainers are expected to be active participants on any open
proposal. Because maintainer review time is finite and the point of the process
is faster progress, **existing open proposals take priority over new
submissions** — new KEPS compete behind the queue of live ones.
^[raw/articles/kiali-kep-proposal.md]

## The proposal template

Every KEP follows the meta-KEP's section structure: ^[raw/articles/kiali-kep-proposal.md]

1. **Summary** — one-paragraph statement of the change.
2. **Motivation** — *Goals* and *Non-Goals* (subsections).
3. **Solution** — the design, including an *Other solutions* subsection
   covering alternatives considered and rejected.
4. **Roadmap** — a **checkbox list** of milestones.

The **Roadmap checkboxes are the de-facto status mechanism.** Unlike
kubernetes KEPs, **Kiali KEPS carry no formal `Status:` field** — there is no
lifecycle state machine (no Accepted/Implemented labels). Any status you see
listed for a Kiali KEP (including the "Inferred status" column in
`raw/articles/kiali-repo-keps-index.md`, which is an agent-derived best-effort
index, *not* an authoritative label) is **inferred** from (a) the proposal's
own Roadmap checkboxes and (b) whether the feature appears shipped in the
release notes. When the two disagree, the **proposal file is the source of
truth for intent** and the **release notes**
(`raw/articles/kiali-docs-news-release-notes.md`) are the source of truth for
what actually shipped.

## The KEPs that exist (as of 2026-09-17)

Nine proposal directories exist under `design/KEPS/` (one is the meta-KEP
itself). Summaries below are taken from each proposal's Summary section;
statuses from the proposal's own roadmap, cross-checked against release notes.
^[raw/articles/kiali-repo-keps-index.md] ^[raw/articles/kiali-kep-graph-cache.md]

| KEP (directory) | What it proposes | Roadmap state (from the proposal file) | Shipped? (per release notes) |
|---|---|---|---|
| `kiali-enhancement-proposal` | **The meta-KEP / template** — the process definition itself | `[ ] KEP process proposed and accepted` (stale — see note below) | N/A — it is the process, not a feature |
| `graph-cache` | Cache traffic-graph data (pre-computed or recently computed) to cut graph response times, given Kiali's large config/permission surface | no roadmap section | **Yes — v2.21.0** (2026-01-26): background graph refresh + caching, `graph_cache.enabled`, 10m default |
| `health-precompute` | Move health-status computation to pre-computed/cached backend values (single configurable duration), with the `kiali_health_status` metric and backend-derived status strings consumed by the UI | no roadmap section | **Yes — v2.22.0** (2026-02-16): health pre-compute/caching enabled by default; v2.24 redefined + made the metric opt-in |
| `metric-rules` | Prometheus **recording rules + federation** to pre-aggregate Istio mesh metrics (sum away per-proxy labels) per the Istio observability best-practices: edge Prometheus (short retention, `workload:*` rules) → federated Prometheus (relabels back to `istio_*`, long retention) → Kiali queries it unchanged; no new Kiali config (`globalScrapeInterval` auto-detection already floors correctly) | no roadmap section | **Design/draft** — "not yet bundled; Istio tiers are implemented first"; a v2.32.0 feature ("Guidance for Pre-Aggregated, federated metrics") began shipping the guidance |
| `multicluster` | "Single pane of glass" multi-cluster support: multi-cluster cache & client config, cross-cluster resource queries, CI testing strategy, multi-cluster demos, UI/UX changes | 0 of 7 checkboxes done (5 top-level + 2 sub-items, all unchecked) | **Shipped in practice** — see discrepancy note below |
| `extensions` | Extend the Kiali graph with traffic metrics from **non-Istio sources** (POC built on Skupper) | 1 of 2 done: `[x] POC (using Skupper)`, `[ ] Add support for Kiali_ext_response_time_seconds` | POC merged; metric-mapping item still open |
| `ai-store` | **Conversation store for the AI Chat feature**: session-isolated chat history, memory-bounded storage, LRU eviction | no roadmap section | **Yes — rolled into AI Chat, shipped v2.22.0** (AI Chatbot Widget + MCP, Dev Preview), with continued work in 2.26–2.31 |
| `controller-model` | Move long-running operations (e.g. mtls) out of the request lifecycle into background "controllers" that read the Kubernetes cache and write the Kiali cache | 0 of 3 done: accept KEP, merge POC, build controllers for slow endpoints | Not shipped — proposal still open at all three gates |
| `multi-session-auth` | Multiple concurrent login sessions, one per cluster, so users without centralized auth can use Kiali across clusters; per-session tokens, cluster-picker login, per-session timeouts, OIDC/token-auth variants | 2 of 6 done: `[x]` openshift multi-session login, `[x]` token-per-cluster; `[ ]` cluster picker, `[ ]` session timeout per session, `[ ]` OIDC, `[ ]` token auth | Partially shipped (the two checked items landed); four items open |
| `namespace-discovery` | A better mechanism for namespace discovery in server and operator (discovery selectors) | 0 of 3 done: add selector support, remove deprecated mechanisms, document | Not shipped |

### Discrepancy notes (index vs. proposal files vs. release notes)

- **`multicluster` is the notable one.** The derived index labels it "OPEN /
  in-progress" and the proposal's own roadmap is 0/7 — but the release notes
  show multi-cluster (OSSMC) functionality shipping continuously from v2.16.0
  through v2.32.0 (multi-control-plane Mesh page, ambient multi-cluster,
  netobserv side-panel, impersonation for multi-cluster auth in 2.30.0, fleet
  mesh in OSSMC 2.31.0, etc.). The KEP predates the actual implementation,
  which proceeded through the OSSMC/plugin workstream, and **the roadmap
  checkboxes were never updated**. The proposal file (ground truth for intent)
  therefore overstates how open this area is; the release notes are ground
  truth for what exists.
- **`kiali-enhancement-proposal` (the meta-KEP) has a stale unchecked
  checkbox** — `[ ] KEP process proposed and accepted` — even though the
  process is manifestly in active use (9 KEPs exist under `design/KEPS/`).
  The checkbox was simply never ticked after acceptance.
- `raw/articles/kiali-repo-keps-index.md` explicitly disclaims its Status
  column as "best-effort inference, not an authoritative label"; where its
  rows disagree with a proposal's roadmap (e.g. it lists multi-session-auth
  "2 done / 4 open" which matches the proposal, but labels multicluster
  "in-progress" which the release notes contradict), the proposal + release
  notes above take precedence.

## How KEPS relate to the rest of the project

- **Upstream of implementation:** an accepted KEP becomes epics/issues on the
  normal issue tracker and is implemented through the usual
  fork/PR workflow ([[kiali-contribution]]), reviewed on the GitHub project
  board, and gated by CI ([[kiali-build-and-dev]]).
- **Downstream of shipping:** the per-version record of what actually landed
  is the kiali.io release notes ([[kiali-release-process]]).
- **Governance:** maintainer review/acceptance is a governance act under
  Kiali's governance document (maintainers collectively manage project
  resources; the full roles/process description lives in the community
  governance page — raw source `kiali-repo-governance.md`).
- **AI policy intersection:** `AI_POLICY.md` explicitly covers design docs —
  AI tools may assist in drafting a KEP, but **the human author must
  thoroughly understand and support the proposed design**, decisions must
  reflect genuine technical reasoning, and community iteration is expected.
  ^[raw/articles/kiali-repo-ai-policy.md]

## Related

- [[kiali-release-process]] — what actually shipped per version
- [[kiali-contribution]] — issue/PR workflow KEPS feed into
- [[kiali-build-and-dev]] — CI gates implementation
- [[kiali-graph-engine]] — subsystem targeted by the graph-cache & health-precompute KEPS
- [[kiali-ai-chat-and-mcp]] — surface the ai-store KEP underpins
- [[kiali-architecture]] — overall system context
