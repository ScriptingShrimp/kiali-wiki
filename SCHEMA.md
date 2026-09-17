# Wiki Schema

## Domain
Kiali upstream development and the software projects I work with daily.

**Primary focus: the Kiali project** — the observability console for the Istio
service mesh (github.com/kiali/kiali). Everything about its upstream: the
codebase and architecture, release history and cadence, design proposals (KEPs),
contribution and CI workflow, maintainers and community, and the ecosystem it
integrates with (Istio, Jaeger, Grafana, Prometheus, OpenShift Service Mesh
Console, Kubernetes).

**Secondary (to be defined as needed):** other service-mesh and Kubernetes
tooling I use daily. Add pages here only when a tool becomes central to work;
the tag taxonomy below already anticipates common ones.

Goal: a durable, cross-referenced memory of how Kiali works upstream, how to
contribute to it, what is in flight, and why decisions were made — so any
future task (writing a patch, triaging an issue, writing a release note,
explaining a feature) can be grounded in the wiki instead of re-derived.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `kiali-graph-module.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page where possible)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **Provenance markers:** On pages that synthesize 3+ sources, append
  `^[raw/articles/source-file.md]` at the end of paragraphs whose claims come
  from a specific source, so claims trace back without re-reading the raw file.

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
# Optional quality signals:
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

### raw/ Frontmatter
```yaml
---
source_url: https://example.com/article   # or github raw URL
ingested: YYYY-MM-DD
sha256: <hex digest of the raw content below the frontmatter>
---
```
The sha256 covers the body only (everything after the closing `---`). On
re-ingest of the same URL: skip if identical, flag drift and update if
different.

## Tag Taxonomy
Add new tags here BEFORE using them.

### Kiali & Service Mesh Ecosystem
- kiali, istio, sidecar, ambient, service-mesh, ossmc, openshift, kubernetes, red-hat

### Kiali Codebase
- architecture, backend, frontend, api, graph, operator, helm, configuration, caching,
- testing, ci-cd, tracing, jaeger, grafana, prometheus, mcp, ai

### Development & Process
- runbook, howto, contribution, release, versioning, kep, design, decision,
- incident, postmortem, timeline, roadmap

### Tools & Services
- tool, service, integration, container, networking, security, monitoring

### People & Orgs
- person, company, team, maintainer, role, contact

### Meta
- comparison, reference, draft, deprecated

Rule: every tag on a page must appear in this taxonomy.

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **Don't create a page** for passing mentions, minor details, or one-off throwaway notes
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable system, service, project, tool, person, or org. For Kiali
this means: the Kiali project itself, its major modules (graph, business,
istio client, operator, frontend), the Kiali operator, OSSMC, and ecosystem
projects (Istio, Jaeger, Grafana, Prometheus) at integration-depth. Include:
- Overview / what it is and where it fits
- Key facts: versions, endpoints, owners, repo layout
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages
One page per process, pattern, runbook, or topic. For Kiali upstream this
includes: build and test workflow, CI pipeline, release process, KEP process,
AI-assisted contribution policy, commit signing. Include:
- Definition / explanation
- Current state (as of the `updated` date) and how it is done
- Open questions or known issues
- Related pages ([[wikilinks]])

## Design & KEP Pages
Kiali design proposals (KEPs) live in `design/KEPS` in the repo. A KEP that is
accepted, implemented, or central to current work gets a concept page tagged
`kep`, with: status, summary, link to the upstream file, and links to the
modules it touches. Do not copy the full KEP text into the wiki — link and
summarize.

## Comparison Pages
Side-by-side analyses (Kiali version A vs B, Kiali vs other mesh consoles,
sidecar vs ambient observability). Include:
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Decision Log
Significant work decisions (adopting a tool, choosing an approach for a
contribution, upgrading a local Kiali install) get a page in `concepts/` typed
`summary` and tagged `decision`. Include: context, options considered, the
decision, why, and date.

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report

Kiali-specific note: the upstream moves fast (sprint demos every few weeks,
regular minor releases). When in doubt about whether a wiki claim is current,
check the raw source's ingestion date and the repo's recent activity before
repeating the claim.

## Sensitive Data
- Never store passwords, API keys, tokens, or personal data of other people in wiki pages.
  Store a pointer: "credentials in 1Password / .env at <path> / in the password manager".
- My own work GitHub/GitLab handles: fine to name. Their tokens: not.
