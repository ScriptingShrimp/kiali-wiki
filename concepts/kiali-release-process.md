---
title: Kiali Release Process
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, release, versioning, ci-cd, timeline, runbook, reference]
sources: [raw/articles/kiali-docs-news-release-notes.md, raw/articles/kiali-repo-releases-recent.json, raw/articles/kiali-repo-agents.md, raw/articles/kiali-doc-build-and-dev-conventions.md, raw/articles/kiali-cithub-workflows-raw.json, raw/articles/DIGEST-kiali-2026-09-17.md, raw/articles/kiali-repo-readme.md]
confidence: high
---

# Kiali Release Process

How Kiali versions are planned, built, tagged, and shipped — the cadence, the
supported-branch model, the release automation, and the per-version record for
the recent 2.16→2.32 window. The repo's `RELEASING.adoc` is the authoritative
runbook for cutting a release (the repo `README.adoc` points to it); this page
covers the observable mechanics and the released history.
^[raw/articles/kiali-repo-readme.md]

## Cadence and versioning

- Kiali ships **sprint releases**: the kiali.io release notes open every
  version block with either a `Release: <date>` or, for the newest block,
  `Sprint Release: <date>` header. In practice the cycle is roughly
  **bi-weekly** — e.g. 2.16.0 Sep 22 2025, 2.17.0 Oct 13 2025, 2.18.0
  Nov 03 2025, 2.19.0 Nov 24 2025, 2.20.0 Dec 22 2025, 2.21.0 Jan 26 2026,
  2.22.0 Feb 16 2026, 2.23.0 Mar 09 2026, 2.24.0 Mar 30 2026, 2.25.0 Apr 20
  2026, 2.26.0 May 29 2026, 2.27.0 Jun 01 2026, 2.28.0 Jun 22 2026, 2.29.0
  Jul 13 2026, 2.30.0 Aug 03 2026, 2.31.0 Aug 21 2026, 2.32.0 Sep 14 2026
  ("Sprint Release"). The full history in the release notes runs back to
  2.0.0 (the notes also document the old 1.x/0.x line down to the 1.74.0
  era and earlier). ^[raw/articles/kiali-docs-news-release-notes.md]
- **Versioning:** `MAJOR.MINOR.PATCH` (v2.x.x). The version string is
  `v2.x.x-SNAPSHOT` on development branches and is injected into the Go binary
  at link time via `ldflags -X` (see [[kiali-build-and-dev]]). Point releases
  exist when needed: **v2.26.1** (2026-05-27) is the only patch release in the
  recent window — published as a GitHub release tagged `v2.26.1` even though it
  is not a separate block in the kiali.io release notes.
  ^[raw/articles/kiali-repo-releases-recent.json] ^[raw/articles/kiali-docs-news-release-notes.md]
- GitHub Releases are published **automatically**: recent release records show
  the author as `github-actions[bot]` and the description body is a pointer to
  the kiali.io release notes page — e.g. the v2.32.0 release body is just
  "https://kiali.io/news/release-notes/ plus a pointer to the local-mode docs".
  So: the human-facing release notes are maintained in the `kiali/kiali.io`
  docs repo (the release notes file itself is updated there — e.g. "Release
  Notes v2.32.0 (#1012)"), and the GitHub tag/release is an automated artifact
  that carries download assets (local-mode binaries). ^[raw/articles/kiali-repo-release-v2.32.0.md]

## Supported branches and backports

`master` is the active development branch for the next release. Currently
supported release branches (which receive backports and security fixes), and
their corresponding OpenShift Service Mesh (OSSM) versions:
^[raw/articles/kiali-repo-agents.md]

| OSSM | Branch | Kiali version |
|------|--------|---------------|
| 3.4 | `v2.27` | 2.27 |
| 3.3 | `v2.22` | 2.22 |
| 3.2 | `v2.17` | 2.17 |
| 3.1 | `v2.11` | 2.11 |
| 3.0 | `v2.4` | 2.4 |

Backporting a fix to an older version follows the `AGENTS.md` checklist:
duplicate operator role changes from `kiali-operator/roles/default/` into the
versioned roles as appropriate, then **cherry-pick the changes to the
appropriate release branch**. ^[raw/articles/kiali-repo-agents.md]

## Release automation (GitHub Actions)

The kiali/kiali repo's `.github/workflows/` contains 35 workflow files
(ingested as `kiali-cithub-workflows-raw.json`). The release-relevant ones:
^[raw/articles/kiali-cithub-workflows-raw.json]

- **`tag-release-creator.yml`** — creates the release tag on the branch/commit
  being released (the automation behind the `github-actions[bot]` release
  records).
- **`release.yml`** — the release pipeline: builds the backend (Go) and
  frontend, produces the container images, and publishes them.
- **`bump-release-version.yml`** — bumps the `v2.x.x-SNAPSHOT` version string
  in the `Makefile` as a release is cut / the next cycle starts.
- **`test-images-creator.yml` / `test-images-update-latest.yml`** — build and
  rotate `latest`-tagged test images used by the integration-test suite and
  (for OSSMC) the plugin build.
- **`release-mcp.yml`** — publishes the Kiali MCP server artifacts (the MCP
  server ships as a separate component — see below).
- **`notify-ossmc-sync.yml`** — notifies the OpenShift Service Mesh Console
  (OSSMC) plugin repo when Kiali changes land, since OSSMC syncs Kiali code.
  ^[raw/articles/kiali-cithub-workflows-raw.json]

Supporting quality gates that run on PRs and protect what a release will
contain: `kiali-ci.yml` (the main CI orchestrator, which calls the reusable
`build-backend.yml` / `build-frontend.yml` workflows), the 21
`integration-tests-*.yml` workflows (backend, frontend core 1/2/optional,
ambient, multi-mesh, multicluster, tempo, chat, MCP, local-offline, etc.),
`test-lint-backend.yml`, `molecules.yml` (operator Ansible scenarios),
`nightly.yml`, `version-checker.yml`, `test-istio-version.yml`,
`codecov-master-baseline.yml`, `mcpchecker.yml`, `report-to-reportportal.yml`.
Build and test mechanics are detailed in [[kiali-build-and-dev]].
^[raw/articles/kiali-doc-build-and-dev-conventions.md]

## What a release contains (delivery surfaces)

A Kiali release ships to several surfaces at once, which is why the release
touches more than one repo: ^[raw/articles/kiali-doc-build-and-dev-conventions.md] ^[raw/articles/kiali-repo-agents.md]

1. **Container images** — published to **quay.io** (`quay.io/kiali/kiali`),
   multi-arch across `amd64 arm64 s390x ppc64le` via `docker buildx`
   (`make container-multi-arch-push-kiali-quay`); the distroless image is the
   default production variant.
2. **GitHub releases** — tagged releases with local-mode binaries (the
   "how to run Kiali in local mode" quick-start assets), built by the release
   workflow.
3. **Operator & Helm** — `kiali-operator` (including OLM/OLM-bundle CSVs and
   molecule-tested Ansible roles) and `helm-charts` version in lockstep; the
   operator is a *symlinked sibling repo* that releases independently.
4. **OSSMC** — the OpenShift Service Mesh Console plugin tracks Kiali via the
   `notify-ossmc-sync.yml` notification; OSSM 3.x bundles specific Kiali
   versions (the branch table above).
5. **MCP server** — separate artifact (kubernetes/openshift MCP server
   containers) with its own `release-mcp.yml`.
6. **Release notes** — written into the `kiali/kiali.io` docs site
   (`kiali.io/news/release-notes`), the canonical per-version record.

## Per-version record

The kiali.io release notes (ingested as `raw/articles/kiali-docs-news-release-notes.md`) are the
authoritative per-version record for 2.16.0 → 2.32.0; full detail with provenance: [[kiali-release-history]].
The dominant arc was the AI assistant: 2.22.0 chatbot + MCP dev preview, multi-provider backends through
2.30.0, MCP pin-compat validation (2.31.0), graph reusing cached health (2.32.0). Platform shifts: the
2.24.0 toolchain jump (Node 20→24, Yarn 1→4, Go 1.25), 2.20.0 PatternFly 6, and 2.31.0 OSSMC multi-mesh.

## Release notes conventions

Each kiali.io release-notes block contains: the version header, a `Release:`/
`Sprint Release:` date, `Features:` and `Fixes:` bullet lists (each item
linked to its originating GitHub issue/PR, prefixed with a component tag such
as `AI:`, `Ambient:`, `Perf:`, `Auth:`, `OSSMC:`, `UI:`, `Validation:`), and
optional `Upgrade Change Notes:` sections documenting breaking or
behavior-changing items. The notes are maintained in the `kiali/kiali.io`
docs repository and cross-link to sprint demo videos (YouTube) and the
Medium/blog. ^[raw/articles/kiali-docs-news-release-notes.md]

## Related

- [[kiali-build-and-dev]] — the build system the release pipeline drives
- [[kiali-contribution]] — how changes reach `master`
- [[kiali-keps]] — design proposals that shape released features
- [[kiali-architecture]] — the system being released
- [[kiali-release-history]] — the full version-by-version record (2.16.0 → 2.32.0)
