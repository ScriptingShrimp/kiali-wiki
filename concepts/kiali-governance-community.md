---
title: Kiali Governance and Community
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, contribution, maintainer, team, role, release, versioning, timeline, reference]
sources: [raw/articles/kiali-repo-governance.md, raw/articles/kiali-docs-news-release-notes.md, raw/articles/kiali-repo-readme.md]
confidence: high
---

# Kiali Governance and Community

How the Kiali project is governed, who maintains it, and how to be promoted into
the maintainer / tester / leader roles. The canonical source is
`GOVERNANCE.md` in the `kiali/kiali` repo. As of 2026-09-17 (the ingestion
date). Release cadence and community activity cross-reference [[kiali]] and
[[kiali-features]].

## Role model

Kiali defines four contributor tiers. The ladder (lowest → highest):
**Contributor → Maintainer / Tester → Leader**, with an **Emeritus** status for
those who step away. ^[raw/articles/kiali-repo-governance.md]

- **Maintainers** — have **write access to the Kiali GitHub org**
  (`github.com/kiali`); can merge their own and others' patches; collectively
  manage project resources and contributors; may be elevated to admin of
  specific repos or owner of the org. The bar is demonstrated collaboration,
  code review quality, high-quality contributions, and timeliness.
- **Testers** — dedicate time to quality: actively trying PRs to find bugs,
  performance issues, and other defects; may write manual or automated tests.
  Focus is **system** and **integration** testing (sanity/smoke/regression and
  running existing automated tests are also in scope). Testers are granted the
  same privileges as Maintainers and invited into the org — **in good faith that
  they are not performing maintainer duties**. Tester and Maintainer roles are
  **not mutually exclusive**.
- **Leaders** — maintainers with broad knowledge of the project's goals and
  vision, who can guide/mentor maintainers, give direction, and set priorities.

## Current lists (2026-09-17)

**Maintainers** (alphabetical): `aljesusg`, `ferhoyos`, `hhovsepy`, `jmazzitelli`,
`josunect`, `leandroberetta`, `nrfox`, `xunzhuo`.
**Leaders** (alphabetical): `jshaughn`.
**Testers** (alphabetical): `FilipB`, `matejnesuta`, `mkralik3`, `pbajjuri20`,
`prachiyadav`, `ScriptingShrimp`.
^[raw/articles/kiali-repo-governance.md]

## Becoming a Maintainer

Requirements (demonstrated, not aspirational):
^[raw/articles/kiali-repo-governance.md]

- **Commitment** — ≥ **3 months** of participation in discussions, contributions,
  and code reviews; **≥ 10 non-trivial PRs reviewed** and **≥ 10 non-trivial PRs
  authored and merged**.
- **Quality** — demonstrated ability to write high-quality code and/or docs.
- **Collaboration** — works well with the team, understands team policies/processes,
  and understands the code base, coding style, and documentation style.

**Process**: an existing maintainer **nominates** the candidate by opening a PR that
adds them to the maintainers list, or via a **GitHub Discussion** in the
**Governance** category. The proposal must include: the nominee's GitHub username,
a rationale, and links to the top-10 non-trivial PRs they authored. **Two other
maintainers must second** the nomination. If **no one objects within 5 working days
(US)**, the nomination is accepted; otherwise the maintainers discuss and usually
reach consensus within the window, and if that fails it goes to a **simple majority
vote** of current maintainers.

## Becoming a Tester

Requirements:
^[raw/articles/kiali-repo-governance.md]

- **≥ 3 months** of active PR testing; **≥ 5 non-trivial defects found** in Kiali;
  occasional testing of `master` to find broken features.
- Ability to collaborate, document testing procedures, and update docs as features
  change; understanding of team policies.

**Process**: self-nomination or maintainer nomination via a PR or a **Governance**
GitHub Discussion, providing the username, top-5 PRs tested, and any documented
test cases. **Formalization requires a simple majority vote of current maintainers.**

## Becoming a Leader

Must first be a **Maintainer**. A maintainer proposes the candidate via a PR
editing the leaders list or a **Governance** Discussion, with the username and a
rationale. **Leadership is granted by a simple majority vote of current
maintainers.** ^[raw/articles/kiali-repo-governance.md]

## Inactivity, removal, and stepping down

- **Inactivity** is measured by **> 4 months** of no contributions **or** no
  communication. Consequences: **involuntary removal/demotion**, or being asked to
  move to **Emeritus** status.
- **Involuntary removal/demotion** happens when role requirements aren't met
  (repeated inactivity, failing to meet role requirements, or a Code of Conduct
  violation). It's handled by a **simple majority vote of current maintainers** —
  protecting the community while opening space for new contributors.
- **Stepping down / Emeritus** — contributors whose commitment changes can step
  down the ladder or move fully to **Emeritus**. Contact the maintainers. A long
  list of emeritus contributors is kept in `GOVERNANCE.md` (e.g. `abonas`,
  `beaumorley`, `jpkrohling`, `lucasponce`, etc.).
  ^[raw/articles/kiali-repo-governance.md]

## Voting

Most business runs by **lazy consensus**, but maintainers may vote on specific
actions. Votes can be taken on PRs or via a **Governance** GitHub Discussion
(private meetings for security/conduct matters). Any maintainer or tester may
demand a vote.
^[raw/articles/kiali-repo-governance.md]

| Change type | Threshold |
|---|---|
| Most project changes | **Simple majority** of all maintainers |
| **Governance changes** | **2/3** of all maintainers |
| **All other unspecified changes** | **2/3** (any maintainer/tester may demand 2/3) |

Tests have a voice in voting but it is **not** mandatory. Once a vote starts,
maintainers (and testers) must cast within **7 working days (US)** unless a process
specifies otherwise.

## Release cadence (community output)

Kiali ships **biweekly "sprint releases"** — 2.27.0 (2026-06-01), 2.28.0
(2026-06-22), 2.29.0 (2026-07-13), 2.30.0 (2026-08-03), 2.31.0 (2026-08-21),
**2.32.0 (2026-09-14, latest as of 2026-09-17)** — cut by `github-actions[bot]`
with binary assets. Recent releases concentrate on AI/MCP (see
[[kiali-ai-chat-and-mcp]]), OSSMC multi-mesh/fleet capabilities (see [[ossmc]]),
and ambient/gateway-API support (see [[kiali-features]]).
^[raw/articles/kiali-docs-news-release-notes.md]

## Contributing (short form)

- Toolchain: Go (version pinned in the Makefile), git, gcc, Docker/Podman
  (`DORP=podman`), Node.js ≥ 20 (Yarn via corepack), GNU make.
- Local dev: `make build-ui && make run-backend` (hot reload via `air`) +
  `make run-frontend`; `kiali run` connects from your kubeconfig (multi-cluster via
  `--remote-cluster-contexts`).
- Cluster bring-up: `hack/run-integration-tests.sh` (minikube/OKD/KinD, installs
  Istio + Bookinfo), `hack/k8s-minikube.sh`, `hack/start-kind.sh`,
  `hack/crc-openshift.sh`.
- Deploy dev builds: `make cluster-push` (or `container-push*` with
  `CLUSTER_TYPE=local`), `make operator-create`, `make kiali-create`; reload the
  server image with `make kiali-reload-image`.
- Contribute via the repo's `CONTRIBUTING.md` and the kiali.io community page.
  ^[raw/articles/kiali-repo-readme.md]

## Related

- [[kiali]] — the project entity (repo layout, components, key facts).
- [[kiali-features]] / [[kiali-ai-chat-and-mcp]] / [[ossmc]] — the workstreams
  this community is shipping.
- [[kiali-installation]] — how to run a local dev cluster.
