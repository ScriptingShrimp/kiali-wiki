# kiali-wiki

A structured, cross-referenced personal knowledge base for the **Kiali** project —
the observability console for the [Istio service mesh](https://github.com/kiali/kiali).

It is a durable, provable memory of how Kiali works upstream: its architecture,
release history, design process (KEPs), contribution and CI workflow, and the
ecosystem it plugs into. The goal is that any future task — writing a patch,
triaging an issue, drafting a release note, explaining a feature — is grounded
in this wiki instead of re-derived from scratch.

> **Status:** 22 schema-valid wiki pages + 81 provenance-verified raw sources.
> Content reflects upstream as of the 2026-09-17 ingest. Kiali moves fast —
> treat specific version/feature claims as time-stamped, and check `log.md` /
> source ingestion dates before relying on them.

## Start here

1. **[index.md](index.md)** — the catalog. Every page listed under its type
   with a one-line summary. *Read this first to find the right page.*
2. **[SCHEMA.md](SCHEMA.md)** — the rules: domain scope, frontmatter format,
   tag taxonomy, page thresholds, provenance markers, and the sensitive-data
   policy.
3. **[log.md](log.md)** — append-only action log. Every ingest/create/update
   is recorded here.

Do **not** start in `raw/` — that is the source layer, not the narrative.

## Repository layout

```
.
├── index.md              # Catalog of all wiki pages (the entry point)
├── SCHEMA.md             # Conventions, frontmatter, tag taxonomy, thresholds
├── log.md                # Append-only action log (rotate at 500 entries)
├── entities/             # One page per project/tool/org (kiali, kiali-operator, ossmc)
├── concepts/             # Process, pattern, runbook, and topic pages (19 pages)
├── raw/                  # VERBATIM upstream sources — provenance layer
│   ├── articles/         #   81 captured sources (each carries a sha256)
│   └── fetch_kiali.py    #   fetcher for kiali.io docs (HTML → verbatim markdown)
├── comparisons/          # Side-by-side analyses (none yet)
├── queries/              # Filed query results worth keeping (none yet)
├── _archive/             # Superseded / deduplicated content
└── .obsidian/            # Editor config (open this folder as an Obsidian vault)
```

## The provenance model

This is the load-bearing feature. Two layers, with a hard contract between them:

- **Raw layer (`raw/articles/`)** — verbatim captures of upstream documents
  (the `kiali/kiali` repo: README, ARCHITECTURE, CONTRIBUTING, AGENTS,
  AI_POLICY, GOVERNANCE, the `docs/agents/` set, all 9 KEPs; the kiali.io
  docs: features, installation, integrations, OSSMC, terminology, AI; release
  notes 2.16 → 2.32; GitHub metadata). **Every file carries frontmatter:**

  ```yaml
  ---
  source_url: https://raw.githubusercontent.com/kiali/kiali/master/README.adoc
  ingested: 2026-09-17
  sha256: <hex digest of the body only, i.e. everything after the closing --->
  ---
  ```

  The `sha256` must match the body. On re-ingest of the same URL: skip if
  identical, flag drift and update if it changed. This makes every capture
  tamper-evident and re-verifiable.

- **Wiki layer (`entities/`, `concepts/`)** — synthesis and explanation. Pages
  that draw on 3+ sources carry inline **provenance markers** of the form
  `^[raw/articles/source-file.md]` so any claim can be traced to its source
  without re-reading the raw file.

The complete file → `source_url` map for the raw layer lives in the
[Source inventory](#source-inventory) appendix below.

## Content inventory

**Entities (3):** `[[kiali]]` (entry point for everything), `[[kiali-operator]]`,
`[[ossmc]]`.

**Concepts & runbooks (19):** architecture, backend-stack, graph-engine,
graph-cache, auth-and-caching, caching, features, ai-chat-and-mcp,
ai-contributions, installation, integrations, governance-community, keps,
release-process, release-history, build-and-dev, contribution,
code-conventions, tests-and-ci.

Oversized topics are split into a hub page + focused deep-dives per the 200-line
page threshold in `SCHEMA.md`.

## Working with the wiki

- **Adding a page:** write it, add YAML frontmatter, register it in
  `index.md`, and append an entry to `log.md`. Tags must exist in the
  `SCHEMA.md` taxonomy before use.
- **Ingesting a new source:** capture it verbatim into `raw/articles/` with
  `source_url` + `sha256` frontmatter, add it to the [Source inventory](#source-inventory)
  section below, then let the wiki pages reference it.
- **Re-checking a claim:** open the raw source, verify the frontmatter hash
  still matches the body, and note the ingestion date. If the hash no longer
  matches, the upstream has drifted — re-ingest and update.
- **Contradictions:** newer sources generally supersede older ones. If they
  genuinely conflict, record both with dates + sources and flag
  `contradictions:` in the frontmatter for review.

## Sensitive-data policy

Per `SCHEMA.md`: no passwords, API keys, tokens, or other people's personal
data in wiki pages — store a pointer (e.g. "credentials in 1Password /
`.env` at `<path>`"). Own work handles are fine to name; their tokens are not.

*The raw layer is a verbatim mirror of public upstream content. If you notice
any embedded credential, flag it for re-capture rather than editing the hash in
place — the hash is the integrity contract.*

## Source inventory

All files under `raw/` with the URL each was fetched from (from the `source_url` in
frontmatter). Files marked **DERIVED** were generated by the agent (no upstream URL).

### 1. kiali.io (official docs) — 29

| File | source_url |
|---|---|
| `kiali-docs-ai-index.md` | https://kiali.io/docs/ai/ |
| `kiali-docs-ai-kiali-chatbot-tools.md` | https://kiali.io/docs/ai/kiali-chatbot-tools/ |
| `kiali-docs-ai-kiali-chatbot.md` | https://kiali.io/docs/ai/kiali-chatbot/ |
| `kiali-docs-ai-kiali-mcp.md` | https://kiali.io/docs/ai/kiali-mcp/ |
| `kiali-docs-architecture-index.md` | https://kiali.io/docs/architecture/ |
| `kiali-docs-architecture.md` | https://kiali.io/docs/architecture/architecture/ |
| `kiali-docs-features-configuration.md` | https://kiali.io/docs/features/configuration |
| `kiali-docs-features-details.md` | https://kiali.io/docs/features/details |
| `kiali-docs-features-health.md` | https://kiali.io/docs/features/health |
| `kiali-docs-features-index.md` | https://kiali.io/docs/features/ |
| `kiali-docs-features-topology.md` | https://kiali.io/docs/features/topology |
| `kiali-docs-features-tracing.md` | https://kiali.io/docs/features/tracing |
| `kiali-docs-features-validations.md` | https://kiali.io/docs/features/validations |
| `kiali-docs-features-wizards.md` | https://kiali.io/docs/features/wizards |
| `kiali-docs-installation-deployment-options.md` | https://kiali.io/docs/installation/deployment-options/ |
| `kiali-docs-installation-guide.md` | https://kiali.io/docs/installation/installation-guide/ |
| `kiali-docs-installation-index.md` | https://kiali.io/docs/installation/ |
| `kiali-docs-installation-quick-start.md` | https://kiali.io/docs/installation/quick-start/ |
| `kiali-docs-integrations-index.md` | https://kiali.io/docs/integrations/ |
| `kiali-docs-integrations-kiali-backstage-plugin.md` | https://kiali.io/docs/integrations/kiali-backstage-plugin/ |
| `kiali-docs-integrations-ossm-console.md` | https://kiali.io/docs/integrations/ossm-console/ |
| `kiali-docs-news-release-notes.md` | https://kiali.io/news/release-notes |
| `kiali-docs-ossmc-index.md` | https://kiali.io/docs/ossmc/ |
| `kiali-docs-ossmc-navigating-multiple-meshes.md` | https://kiali.io/docs/ossmc/navigating-multiple-meshes/ |
| `kiali-docs-ossmc-users-guide.md` | https://kiali.io/docs/ossmc/users-guide/ |
| `kiali-docs-terminology-concepts.md` | https://kiali.io/docs/architecture/terminology/concepts/ |
| `kiali-docs-terminology-index.md` | https://kiali.io/docs/architecture/terminology/ |
| `kiali-docs-terminology-networking.md` | https://kiali.io/docs/architecture/terminology/networking/ |
| `kiali-io-release-notes.md` | https://kiali.io/news/release-notes/ |

### 2. raw.githubusercontent.com/kiali/kiali/master/ — 34 (repo path under the prefix)

| File | Repo path |
|---|---|
| `COMMIT-SIGNING-SETUP.md` | `COMMIT-SIGNING-SETUP.md` |
| `frontend-README.adoc` | `frontend/README.adoc` |
| `go.mod` | `go.mod` |
| `kiali-doc-STATUS.md` | `docs/agents/STATUS.md` |
| `kiali-kep-ai-store.md` | `design/KEPS/ai-store/proposal.md` |
| `kiali-kep-controller-model.md` | `design/KEPS/controller-model/proposal.md` |
| `kiali-kep-extensions.md` | `design/KEPS/extensions/proposal.md` |
| `kiali-kep-graph-cache.md` | `design/KEPS/graph-cache/proposal.md` |
| `kiali-kep-health-precompute.md` | `design/KEPS/health-precompute/proposal.md` |
| `kiali-kep-metric-rules.md` | `design/KEPS/metric-rules/proposal.md` |
| `kiali-kep-multi-session-auth.md` | `design/KEPS/multi-session-auth/proposal.md` |
| `kiali-kep-multicluster.md` | `design/KEPS/multicluster/proposal.md` |
| `kiali-kep-namespace-discovery.md` | `design/KEPS/namespace-discovery/proposal.md` |
| `kiali-kep-proposal.md` | `design/KEPS/kiali-enhancement-proposal/proposal.md` |
| `kiali-repo-agents.md` | `AGENTS.md` |
| `kiali-repo-ai-policy.md` | `AI_POLICY.md` |
| `kiali-repo-architecture.md` | `ARCHITECTURE.md` |
| `kiali-repo-cache.md` | `CACHE.md` |
| `kiali-repo-code-of-conduct.md` | `CODE_OF_CONDUCT.md` |
| `kiali-repo-contributing.md` | `CONTRIBUTING.md` |
| `kiali-repo-docs-agents-auth-and-security.md` | `docs/agents/auth-and-security.md` |
| `kiali-repo-docs-agents-backend-architecture.md` | `docs/agents/backend-architecture.md` |
| `kiali-repo-docs-agents-build-and-dev-conventions.md` | `docs/agents/build-and-dev-conventions.md` |
| `kiali-repo-docs-agents-business-logic.md` | `docs/agents/business-logic.md` |
| `kiali-repo-docs-agents-claims.yml.md` | `docs/agents/.claims.yml` |
| `kiali-repo-docs-agents-frontend-architecture.md` | `docs/agents/frontend-architecture.md` |
| `kiali-repo-docs-agents-graph-engine.md` | `docs/agents/graph-engine.md` |
| `kiali-repo-docs-agents-kubernetes-client.md` | `docs/agents/kubernetes-client.md` |
| `kiali-repo-docs-agents-observability-and-ai.md` | `docs/agents/observability-and-ai.md` |
| `kiali-repo-docs-agents-status.md` | `docs/agents/STATUS.md` |
| `kiali-repo-governance.md` | `GOVERNANCE.md` |
| `kiali-repo-i18n-agents.md` | `I18N-AGENTS.md` |
| `kiali-repo-internal-api.md` | `kiali_internal_api.md` |
| `kiali-repo-readme.md` | `README.adoc` |

### 3. api.github.com (GitHub API) — 7

| File | source_url |
|---|---|
| `kiali-cithub-workflows-raw.json` | https://api.github.com/repos/kiali/kiali/contents/.github/workflows |
| `kiali-design-toplevel-raw.json` | https://api.github.com/repos/kiali/kiali/contents/design |
| `kiali-docs-agents-raw.json` | https://api.github.com/repos/kiali/kiali/contents/docs/agents |
| `kiali-keps-enhancement-proposal-raw.json` | https://api.github.com/repos/kiali/kiali/contents/design/KEPS/kiali-enhancement-proposal |
| `kiali-repo-keps-index-raw.json` | https://api.github.com/repos/kiali/kiali/contents/design/KEPS |
| `kiali-repo-release-v2.32.0.md` | https://api.github.com/repos/kiali/kiali/releases/tags/v2.32.0 |
| `kiali-repo-releases-recent.json` | https://api.github.com/repos/kiali/kiali/releases?per_page=10 |

### 4. medium.com — 1

| File | source_url |
|---|---|
| `kiali-blog-releases-2-16-to-2-30-features-update.md` | https://medium.com/kialiproject/kiali-releases-2-16-to-2-30-features-update-5451d32b1b68 |

### 5. DERIVED (no upstream URL) — 10

| File | Note |
|---|---|
| `DIGEST-kiali-2026-09-17.md` | Agent-compiled digest of the kiali.io docs fetch; per-file source refs in the file |
| `kiali-repo-keps-index.md` | Derived index over the `design/KEPS` listing (raw JSON: `kiali-repo-keps-index-raw.json`) |
| `kiali-doc-auth-and-security.md` | Agent-generated from a repo scan (`docs/agents/` watch paths; git hash in frontmatter) |
| `kiali-doc-backend-architecture.md` | Agent-generated from a repo scan |
| `kiali-doc-build-and-dev-conventions.md` | Agent-generated from a repo scan |
| `kiali-doc-business-logic.md` | Agent-generated from a repo scan |
| `kiali-doc-frontend-architecture.md` | Agent-generated from a repo scan |
| `kiali-doc-graph-engine.md` | Agent-generated from a repo scan |
| `kiali-doc-kubernetes-client.md` | Agent-generated from a repo scan |
| `kiali-doc-observability-and-ai.md` | Agent-generated from a repo scan |

---

*Local knowledge base. Not an official Kiali artifact; the project home is
[kiali/kiali](https://github.com/kiali/kiali) and
[kiali.io](https://kiali.io).*
