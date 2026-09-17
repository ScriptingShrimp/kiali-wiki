---
title: Kiali Build and Development Workflow
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, ci-cd, testing, operator, helm, container, kubernetes, istio, reference, howto, runbook]
sources: [raw/articles/kiali-repo-agents.md, raw/articles/kiali-doc-build-and-dev-conventions.md, raw/articles/kiali-repo-readme.md, raw/articles/kiali-cithub-workflows-raw.json]
confidence: high
---

# Kiali Build and Development Workflow

How to build, test, deploy, and debug Kiali from source. This is the developer
runbook for the `kiali/kiali` repo and its sibling `kiali-operator` and
`helm-charts` repos. It complements [[kiali-contribution]] (how to land
changes) and [[kiali-release-process]] (how releases are cut). The canonical
upstream references are `AGENTS.md` (AI/developer guide), `RELEASING.adoc`,
`STYLE_GUIDE.adoc`, and the repo `README.adoc`.
^[raw/articles/kiali-repo-agents.md] ^[raw/articles/kiali-repo-readme.md]

## Repository layout

The Kiali project spans **three repositories** that must be cloned together and
linked with a symlink. The operator is a **filesystem symlink** to a sibling
clone, not a git submodule — the repos version and release independently, and
the symlink lets each dev point `operator/` at any local checkout (a feature
branch, a fork, a pinned version) without touching a tracked file. ^[raw/articles/kiali-doc-build-and-dev-conventions.md]

```
kiali_sources/
├── kiali/              # Main server + UI (this wiki's primary focus)
├── kiali-operator/     # Operator repo
└── helm-charts/        # Helm charts repo
```

```bash
mkdir kiali_sources && cd kiali_sources
git clone https://github.com/kiali/kiali.git
git clone https://github.com/kiali/kiali-operator.git
git clone https://github.com/kiali/helm-charts.git
ln -s $PWD/kiali-operator kiali/operator
```

The symlink is load-bearing: `Makefile.helm.mk` resolves
`readlink operator/` to find the *physical* operator dir, then looks for
`helm-charts` as a sibling of that physical path — so `helm-charts` must sit
next to `kiali-operator`, not next to the symlink. ^[raw/articles/kiali-doc-build-and-dev-conventions.md]

## Toolchain prerequisites

- **Go** — at the minimum version pinned in the `Makefile` (verify with `make go-check`; Kiali v2.24+ tracks Go 1.25). ^[raw/articles/kiali-docs-news-release-notes.md]
- **git**, **gcc**, **make** (GNU make or compatible)
- **Docker or Podman** — set `DORP=podman` if using podman
- **Node.js >= 20** — **Yarn is managed via corepack**. Run `corepack enable` once; the exact Yarn 4 version is pinned in `frontend/package.json` via the `packageManager` field. ^[raw/articles/kiali-repo-readme.md]

## The build system: a decomposed Makefile

Everything is driven by `make`. The root `Makefile` sets global variables and
includes nine topic-specific `.mk` files from `make/`: ^[raw/articles/kiali-doc-build-and-dev-conventions.md]

| File | Concern |
|---|---|
| `Makefile.build.mk` | go build, yarn build, test targets |
| `Makefile.cluster.mk` | cluster-type registry configuration |
| `Makefile.container.mk` | docker/podman build + push to quay.io |
| `Makefile.helm.mk` | helm chart targets (needs helm-charts sibling) |
| `Makefile.mcp.mk` | MCP (Model Context Protocol) server targets |
| `Makefile.molecule.mk` | Ansible Molecule operator tests |
| `Makefile.olm.mk` | OLM (Operator Lifecycle Manager) packaging |
| `Makefile.operator.mk` | operator deploy/undeploy to live clusters |
| `Makefile.ui.mk` | frontend dev server + Cypress targets |

Key global variables: `VERSION` (the `v2.x.x-SNAPSHOT` string, injected at
link time), `TARGET_ARCHS` = `amd64 arm64 s390x ppc64le`, `DORP`
(docker/podman), `CLUSTER_TYPE` (openshift/minikube/kind/local),
`KIALI_DOCKER_FILE` (defaults `Dockerfile-distroless`), `CGO_ENABLED` (0 by
default, 1 only with `-race`). ^[raw/articles/kiali-doc-build-and-dev-conventions.md]

`make help` lists every target. The **build order matters**: the UI must be
built *before* the backend because `//go:embed all:build` in
`frontend/frontend.go` embeds the React build into the Go binary at compile
time. `make build` runs a `check-ui` step that aborts with a clear error if
`frontend/build/` is absent. ^[raw/articles/kiali-doc-build-and-dev-conventions.md]

### Core commands

```bash
# Build everything (UI first, then backend), then unit tests
make build-ui build test

# Local hot-reload development (no cluster needed)
make build-ui          # terminal 1 — only when UI changes
make run-backend       # terminal 1 (air auto-recompiles on Go changes)
make run-frontend      # terminal 2 — opens http://localhost:3001

# Format + lint before committing
make format lint

# Container image build + push to quay.io (dev tag)
make container-build-kiali
make container-push-kiali-quay
make container-multi-arch-push-kiali-quay   # docker buildx, all TARGET_ARCHS

# Frontend integration tests
make cypress-gui        # interactive
make cypress-run        # headless
```

Pass extra Go test flags via the environment:
`make -e GO_TEST_FLAGS="-race -v -run=\"TestName\"" test`. ^[raw/articles/kiali-repo-agents.md]

### The Go binary

`make build` compiles a **single static, CGO-disabled Go executable** with
version, commit hash, and Go version injected via `ldflags -X` into
package-level variables in `github.com/kiali/kiali/cmd`. `CGO_ENABLED=0` is
what makes the distroless container image possible (no C runtime dependency).
`make build-linux-multi-arch` loops `TARGET_ARCHS` producing one
`-<arch>`-suffixed binary each; `Dockerfile-multi-arch` copies
`kiali-${TARGETARCH}`. `make run-backend` uses the `air` hot-reload tool
(`.air.toml`). ^[raw/articles/kiali-doc-build-and-dev-conventions.md]

### Container image variants

Four Dockerfiles live in `deploy/docker/`: ^[raw/articles/kiali-doc-build-and-dev-conventions.md]

| Dockerfile | Base | Use |
|---|---|---|
| `Dockerfile-distroless` | `scratch` (UBI rootfs via multi-stage) | **Default** production image; openssl+certs, no shell |
| `Dockerfile-multi-arch` | `ubi9-minimal` (per-arch) | multi-arch manifest publishing |
| `Dockerfile-multi-arch-distroless` | scratch, multi-arch | distroless multi-arch |
| `Dockerfile-cypress` | — | Cypress test-execution container |

All images run as UID 1000 (`kiali` user); `ENTRYPOINT` is always
`["/opt/kiali/kiali"]` — no CMD, all config via env or a mounted config file.
The distroless two-stage build installs `bash coreutils-single
glibc-minimal-langpack openssl` from a UBI 9 base into `/mnt/rootfs`, then
`FROM scratch` copies only that rootfs. ^[raw/articles/kiali-doc-build-and-dev-conventions.md]

### `cluster-push`: one target, every cluster type

`Makefile.cluster.mk` abstracts over the supported cluster types so a single
`make cluster-push` (which is just `cluster-push-operator cluster-push-kiali`
in sequence) works everywhere. `CLUSTER_TYPE` selects the registry path: ^[raw/articles/kiali-doc-build-and-dev-conventions.md]

| `CLUSTER_TYPE` | Registry resolution | Push |
|---|---|---|
| `openshift` | external hostname from `oc get image.config.openshift.io/cluster`; patches the registry operator to enable the external route first | docker/podman push |
| `minikube` | `minikube ip`:5000 (registry addon required) | docker/podman push |
| `kind` | `kind-registry` container's exposed port | docker/podman push to `localhost:<port>` |
| `local` | no push; image stays in local daemon | — |

A typical cluster deploy chain: `make build-ui build test cluster-push` →
`make operator-create` → `make kiali-create`. Quick iteration on an existing
deploy is `make build cluster-push-kiali kiali-reload-image` (server) or
`make cluster-push-operator operator-reload-image` (operator). ^[raw/articles/kiali-repo-agents.md]

## Testing and CI

The test matrix spans unit tests, backend E2E, envtest controller tests,
Cypress Gherkin frontend suites, Molecule operator scenarios, and a GitHub
Actions fan-out of parallel integration jobs. Full matrix, suites, and
local-reproduction steps: [[kiali-tests-and-ci]].

## Code conventions

Go (any, sorted fields/keys, 3-group imports, golangci-lint) and TypeScript
(PascalCase components, functional + hooks, kialiStyle, data-test attrs).
Full rules, protected files, and operator dev workflow: [[kiali-code-conventions]].

## Related

- [[kiali-tests-and-ci]] — clusters, test matrix, CI/CD pipeline detail
- [[kiali-code-conventions]] — style rules, file protection, operator development
- [[kiali-architecture]] — what the build is building
- [[kiali-contribution]] — how changes are landed: discussion, PRs, review
