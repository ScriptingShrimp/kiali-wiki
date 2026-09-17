---
title: Kiali Code Conventions and Operator Development
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, howto, contribution, reference]
sources: [raw/articles/kiali-repo-agents.md, raw/articles/kiali-doc-build-and-dev-conventions.md, raw/articles/kiali-repo-readme.md, raw/articles/kiali-cithub-workflows-raw.json]
confidence: high
---

## Operator development

- Symlink the operator (see layout). Never clone into `kiali/operator`
  directly — checking out old Kiali branches can delete your operator work.
- **Playbook-only (fast):** `make run-operator-playbook-kiali` or
  `run-operator-playbook-ossmconsole` (needs python3 + Ansible collections from
  `operator/requirements.yml`).
- **Full operator:** `make run-operator` (runs `ansible-operator` locally,
  watching for Kiali/OSSMConsole CRs).
- **Build/deploy:** `make cluster-push-operator` / `operator-create` /
  `olm-operator-create` (OpenShift) / `operator-delete`.
- **Molecule:** see test section above. ^[raw/articles/kiali-repo-agents.md]

## Code conventions (summary)

Full rules in `STYLE_GUIDE.adoc` and `AGENTS.md`. The load-bearing ones: ^[raw/articles/kiali-repo-agents.md] ^[raw/articles/kiali-doc-build-and-dev-conventions.md]

**Go backend**
- Use `any`, not `interface{}`; no trailing whitespace.
- Sort struct fields **and** YAML keys **alphabetically**.
- 3-group imports (stdlib / third-party / Kiali) separated by blank lines —
  enforced by `hack/fix_imports.sh` + `goimports`.
- Comments explain *why*, not *what*.
- `gofmt` (via `make format`), `golangci-lint` (via `make lint`,
  `make lint-install` to set up). Go version enforced by `make go-check`.
- `AuthenticationFailureError` (with `HttpStatus`) for expected auth failures
  vs. plain `error` for internal failures; implementers end with a
  compile-time interface guard (`var _ AuthController = &tokenAuthController{}`).

**TypeScript frontend**
- `PascalCase` files (general-purpose files `camelCase`); `camelCase`
  vars/functions; `PascalCase` Redux actions; `UPPER_SNAKE_CASE` global
  constants. Event handlers `handleX`, props `onX`, present tense.
- Prefer arrow functions and functional components with hooks — **do not
  introduce class components** (legacy; refactor only when making large changes).
- Add `data-test` attributes to interactive elements for Cypress
  (`cy.getBySel('name')`).
- Styling via `kialiStyle` (`styles/StyleUtils.ts`), `className` over inline
  `style`, PF design-token enums (`PFSpacer`, `PFFontSize`, `PFColors`),
  `rem` over `px` (except fixed large layout dimensions).
- i18n: always `import { t } from 'utils/I18nUtils'` (not `i18next` directly);
  add `language` to Redux props for components that don't re-render on change.

## File protection rules

Never modify these without understanding their role — they are protected
across the org and CI: ^[raw/articles/kiali-repo-agents.md] ^[raw/articles/kiali-doc-build-and-dev-conventions.md]

- **Versioned operator roles** — only edit `kiali-operator/roles/default/`;
  `roles/v2.4/`, `roles/v2.11/`, etc. are frozen for older supported versions.
- **Old CSV versions** — `kiali-operator/manifests/*/[version]/`; only modify
  the LATEST version.
- **CRD copies** — only the **golden copies** in `kiali-operator/crd-docs/crd/`
  are the source of truth. All other CRD files are synced copies. Run
  `make sync-crds` (in kiali-operator) to propagate, and `make validate-crd-sync`
  to verify. This can also modify your helm-charts repo.
- **Generated docs** — `kiali.io/content/en/docs/Configuration/*.md`.
- **`_output/`** directories and subdirs — build artifacts, never hand-edit.
- `frontend/package.json` — the `proxy` field is written by `make run-frontend`
  and cleaned on exit; don't add a persistent one.
- `go.mod`/`go.sum` — run `go mod tidy`; never hand-edit.
- `make/*.mk` — changes affect all devs + CI; test across all `CLUSTER_TYPE`s.

**CRD change workflow:** edit the golden copy → `make validate-cr` → `make
sync-crds` → `make validate-crd-sync` → PR to kiali-operator → separate PR to
helm-charts with the synced files. ^[raw/articles/kiali-repo-agents.md]

**Multi-location resource checklists** (altering operator resources, server
resources, RBAC, config settings, dashboard templates, backports) are in
`AGENTS.md` — when you change one, every install method (Helm, OLM, operator
templates) must be updated in lockstep, sorted alphabetically.

## Related

- [[kiali-build-and-dev]] — build system, Makefile layout, and cluster deployment (parent page)
- [[kiali-contribution]] — how changes are landed: discussion, PRs, review
- [[kiali-operator]] — the operator entity: what it is and where it fits
- [[kiali-features]] — the product the conventions serve
