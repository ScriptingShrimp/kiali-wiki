# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-09-17] create | Wiki initialized
- Domain: personal work (IT/systems/self-hosting, software development, business/operations)
- Structure created: SCHEMA.md, index.md, log.md
- Directories: raw/{articles,papers,transcripts,assets}, entities/, concepts/, comparisons/, queries/, _archive/
- Total pages: 0

## [2026-09-17] update | Scope rewritten to Kiali focus
- User directive: wiki is primarily for work-related Kiali (observability console for Istio) upstream development; secondary scope (other service-mesh tools used daily) to be defined later
- SCHEMA.md: domain, tag taxonomy, page-type guidance (KEP pages, Kiali entity scope), and update policy rewritten for the Kiali/Istio domain
- Started: bulk ingest of Kiali upstream (repo docs + kiali.io docs) via parallel research; wiki pages to be filed after
- Total pages: 0

## [2026-09-17] ingest | Kiali upstream corpus (raw layer)
- 3-way parallel research fan-out (kiali/kiali repo docs, kiali.io official docs, release/GitHub metadata)
- 81 verbatim sources saved to raw/articles/, each with sha256 frontmatter provenance (verified to match body)
- Fetched the one missing upstream doc (GOVERNANCE.md)
- Removed 7 byte-identical duplicate copies (archived), repaired 29 frontmatter hashes that didn't match, added the provenance block to 30 files that were missing it
- Digest written: raw/articles/DIGEST-kiali-2026-09-17.md
- Total pages: 0 (raw layer only)

## [2026-09-17] create | First wiki page set (Kiali)
- 3-way parallel writing fan-out over the raw layer; all pages provenance-marked, schema-valid, wikilink-verified
- Entities: kiali, kiali-operator, ossmc
- Concepts: architecture, backend-stack, graph-engine, graph-cache, auth-and-caching, caching, features, ai-chat-and-mcp, installation, integrations, governance-community, keps, release-process, build-and-dev, contribution, code-conventions, tests-and-ci, ai-contributions, release-history
- 6 oversized pages split into hub + deep-dive per the 200-line schema rule (backend-stack, caching, graph-cache, tests-and-ci, code-conventions, ai-contributions, release-history)
- Final verification: 22 pages, all under 200 lines, all frontmatter valid, all tags in taxonomy, all wikilinks resolve, all raw provenance markers resolve to existing files
- index.md rebuilt with full catalog; log.md appended
- Total pages: 22

## [2026-09-18] create | README.md + raw/SOURCE-INVENTORY.md
- Added README.md at repo root: overview, layout, provenance model, usage, sensitive-data policy
- Added raw/SOURCE-INVENTORY.md: complete file→source_url map for all 81 raw sources (grouped by origin: kiali.io / raw.githubusercontent / api.github.com / medium / derived)
- No wiki page changes; no content edits to raw sources
- Total pages: 22

## [2026-09-18] update | Merged source inventory into README.md
- Consolidated raw/SOURCE-INVENTORY.md into README.md as the "Source inventory" appendix (headings demoted to H2/H3); deleted the standalone file
- Updated README cross-references to point at the in-README appendix; dropped the inventory from the layout tree
- Total pages: 22

## [2026-09-18] update | .obsidian excluded from version control
- User reversed the earlier decision: `.obsidian/` no longer tracked
- `.gitignore` now ignores `.obsidian/` (full folder); files removed from index via `git rm --cached -r .obsidian/`
- Files remain on disk, just untracked
- Total pages: 22
