---
title: Kiali Tests, Local Clusters, and CI
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, testing, ci-cd, runbook, howto]
sources: [raw/articles/kiali-repo-agents.md, raw/articles/kiali-doc-build-and-dev-conventions.md, raw/articles/kiali-repo-readme.md, raw/articles/kiali-cithub-workflows-raw.json]
confidence: high
---

## Clusters for local development

Set the env vars first: `CLUSTER_TYPE` (minikube/kind/openshift),
`MINIKUBE_PROFILE` (minikube), `KIND_NAME` (kind), `DORP` (docker/podman),
`CLIENT_EXE` (`kubectl` for minikube/kind, `oc` for OpenShift). The `hack/`
directory holds the cluster-provisioning scripts — all support `--help`.
^[raw/articles/kiali-repo-agents.md] ^[raw/articles/kiali-doc-build-and-dev-conventions.md]

- **Minikube** (most common): `./hack/k8s-minikube.sh -mp $PROFILE start`
  (add `--hydra-enabled true` for auth testing, required by some molecule
  tests); then `./hack/istio/install-istio-via-istioctl.sh --client-exe
  $CLIENT_EXE`. Bookinfo via `./hack/istio/install-bookinfo-demo.sh`. Port
  forward via `./hack/k8s-minikube.sh -mp $PROFILE port-forward`.
- **KinD** (lightweight/disposable; docker only, podman not fully supported):
  `./hack/start-kind.sh -n $KIND_NAME` (MetalLB, `--enable-hydra true`,
  `--enable-image-registry true` as needed); then Istio via istioctl.
- **OpenShift (CRC)**: `./hack/crc-openshift.sh start`; log in with the
  `kubeadmin` creds from `./hack/crc-openshift.sh status`; deploy the operator
  via OLM with `make CLUSTER_TYPE=openshift olm-operator-create` (or
  `operator-create` without OLM).

The `hack/run-integration-tests.sh` script is the **canonical entry point** for
both CI and local end-to-end runs — it can provision a cluster, install Istio,
deploy demos, deploy Kiali, and run a test suite in one command. ^[raw/articles/kiali-repo-agents.md]

## Test infrastructure

- **Unit tests** — `make test` runs `go test` across all packages except
  `vendor/`, `frontend/`, and `tests/integration/`, using the
  `exclude_frontend` build tag to gate files that import Node/browser
  dependencies. Requires `setup-envtest` for controller tests (envtest binaries
  land in `${OUTDIR}/k8s`). ^[raw/articles/kiali-doc-build-and-dev-conventions.md]
- **Backend integration tests** — `make test-integration` (full E2E API tests
  against a live cluster, 30-min timeout, JUnit XML via `go-junit-report`).
  `make test-integration-controller` uses envtest (no live cluster) and needs
  Istio CRD YAMLs (`make download-istio-crds`). ^[raw/articles/kiali-doc-build-and-dev-conventions.md]
- **Frontend (Cypress)** — Gherkin BDD `.feature` files in
  `frontend/cypress/integration/featureFiles/` with TypeScript step
  definitions in `frontend/cypress/integration/common/`. Steps are **global** —
  any `.ts` under `cypress/integration/` loads for every feature file. `cy.getBySel('x')`
  selects `[data-test="x"]`; `linkSelector()` matches both `<a href>` and
  `<button data-href>` (the latter is how OSSMC kiosk mode renders links).
  ^[raw/articles/kiali-repo-agents.md]
- **Molecule tests** — `./hack/run-molecule-tests.sh --client-exe ... 
  --cluster-type minikube -udi true -hcrp false`. `-udi true` pulls the dev
  images you pushed (from `cluster-push`); `-udi false` uses quay.io. Scenarios
  live in `kiali-operator/molecule/` (e.g. `config-values-test`, `token-test`).
  ^[raw/articles/kiali-repo-agents.md] ^[raw/articles/kiali-doc-build-and-dev-conventions.md]

### The `local` suite (recommended for local dev)

The `local` suite in `run-integration-tests.sh` tests local code changes
**without** building container images: it creates a KinD+Istio cluster (via
Sail), installs demo apps, runs the `kiali` binary directly from
`$GOPATH/bin/kiali`, and runs the `cypress:run:smoke` suite against it. ^[raw/articles/kiali-repo-agents.md]

```bash
make build-ui build
hack/run-integration-tests.sh --test-suite local --setup-only true   # ~5 min
make build   # after code changes
hack/run-integration-tests.sh --test-suite local --tests-only true
```

Then run Kiali locally and a single tagged scenario:

```bash
$(go env GOPATH)/bin/kiali -c hack/ci-yaml/ci-test-config-no-cache.yaml run \
  --cluster-name-overrides kind-ci=cluster-default \
  --port-forward-tracing --enable-tracing \
  --port-forward-prom --port-forward-grafana --no-browser
# Kiali at http://localhost:20001

cd frontend
yarn cypress run -e TAGS="@smoke"
# debug one scenario: tag it @selected, then `make cypress-selected`
```

Available `--test-suite` values include `backend`, `frontend`,
`frontend-core-1/-2/-optional`, `frontend-ambient`, `frontend-primary-remote`,
`frontend-multi-primary`, `frontend-multi-mesh`, `frontend-external-kiali`,
`frontend-tempo`, `local`, `offline`, `backend-external-controlplane`. Each maps
to a `@tag` in the Gherkin files (see the tag table in `AGENTS.md`). ^[raw/articles/kiali-repo-agents.md]

**Debugging Cypress with Playwright MCP:** the repo ships a `.mcp.json` with a
`cypress-debugger` server connecting to the Cypress Chrome on port 9222. Run
Cypress with `CYPRESS_REMOTE_DEBUGGING_PORT=9222 --browser chrome --headed
--no-exit`, then the MCP `browser_snapshot`/`browser_evaluate` tools inspect the
runner and the Kiali UI inside the iframe. **`Ctrl+R` re-runs but does NOT pick
up code changes** (Cypress caches compiled specs) — you must kill and restart
Cypress after editing a `.ts` step or `.feature` file. ^[raw/articles/kiali-repo-agents.md]

## CI/CD pipeline (GitHub Actions)

Workflows live in `.github/workflows/` (35 files ingested as
`kiali-cithub-workflows-raw.json`). The architecture **separates the backend
and frontend builds into reusable called workflows** (`workflow_call`), then
fans them out into many parallel integration-test jobs, so the binary and the
frontend artifact are built once and reused. ^[raw/articles/kiali-doc-build-and-dev-conventions.md] ^[raw/articles/kiali-cithub-workflows-raw.json]

- `build-backend.yml` — Go from `go.mod`, downloads the frontend build
  artifact, `make clean build`, uploads the binary; **PR builds add `-race`
  and `CGO_ENABLED=1`**.
- `build-frontend.yml` — builds the React app, uploads `frontend/build/`.
- `integration-tests-*.yml` — one per suite from `run-integration-tests.sh`
  (backend, frontend-core-1/-2/-optional, ambient, multi-cluster, multi-mesh,
  tempo, local-offline, external-kiali, chat, mcp, etc.).
- Release/publishing: `release.yml`, `tag-release-creator.yml`,
  `bump-release-version.yml`, `test-images-creator.yml`, `test-images-update-latest.yml`,
  `release-mcp.yml`, `notify-ossmc-sync.yml`.
- Quality/ops: `test-lint-backend.yml` (golangci-lint, config at
  `.github/workflows/config/.golangci.yml`, binary version pinned in
  `Makefile.build.mk`), `molecules.yml`, `nightly.yml`, `version-checker.yml`,
  `test-istio-version.yml`, `report-to-reportportal.yml`, `mcpchecker.yml`.

**Reproducing a CI failure locally:** `gh run list --repo kiali/kiali
--status failure` → `gh run view <RUN_ID> --log --job <JOB_ID>` → map the job
name to a suite (e.g. `Run frontend core 1 integration tests` → `frontend-core-1`)
→ `gh run download` for Cypress screenshots → checkout the branch, `make
build-ui build`, set up the matching suite, and re-run the single failing
feature with the debug browser. ^[raw/articles/kiali-repo-agents.md]

## Related

- [[kiali-build-and-dev]] — build system, toolchain, and quick-reference commands (parent page)
- [[kiali-architecture]] — what the test matrix is testing
- [[kiali-keps]] — in-flight design work the suites exercise
