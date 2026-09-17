---
title: Contributing to Kiali
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, contribution, howto, runbook, reference]
sources: [raw/articles/kiali-repo-contributing.md, raw/articles/kiali-repo-ai-policy.md, raw/articles/COMMIT-SIGNING-SETUP.md, raw/articles/kiali-repo-agents.md, raw/articles/kiali-repo-governance.md]
confidence: high
---

# Contributing to Kiali

How to contribute to Kiali: the pre-work discussion process, development
conventions, commit signing, the AI-assisted contribution policy, and how
pull requests are created, tracked, and reviewed. Kiali is Apache 2.0 licensed
and accepts contributions via GitHub pull requests; **no contributor agreement
is required** to submit patches, and by contributing you agree to license your
work under the Apache License. Improvements to documentation are welcomed as
much as code changes. ^[raw/articles/kiali-repo-contributing.md]

Practical build/test/cluster instructions live in [[kiali-build-and-dev]];
how versions get cut is in [[kiali-release-process]]; how large designs get
approved is in [[kiali-keps]].

## Before you change anything

The project explicitly asks contributors to get the idea agreed *before*
writing code: ^[raw/articles/kiali-repo-contributing.md]

1. **Open a discussion or issue** in the **main `kiali/kiali` repo** describing
   the motivation in detail. This holds regardless of where the work actually
   lands — server, UI, operator, or helm charts all use the same links
   (GitHub Discussions / Issues on `kiali/kiali`).
2. **Let maintainers comment** — they may refine the issue or change direction.
3. **Wait for agreement.** Before starting work, make sure maintainers have
   agreed the work should be done and have added the issue to the backlog.
4. Only when the design/approach is settled, **prepare a pull request** with
   the changes.

**Good first issues:** newcomers should start with issues labeled
`good first issue` in the kiali/kiali repo to get accustomed to the code
base. ^[raw/articles/kiali-repo-contributing.md]

## Development conventions

- **Building and running** — the server `README.adoc` (Building section) and
  `frontend/README.adoc` cover building server and UI; the wiki's
  [[kiali-build-and-dev]] page summarizes the Makefile, cluster workflows, and
  test suites.
- **Code style** — the repo's `STYLE_GUIDE.adoc` is the authority on Go and
  TypeScript style. Load-bearing rules (also enforced by CI): `gofmt` +
  `golangci-lint` clean (`make format lint` before committing), `any` over
  `interface{}`, no trailing whitespace, struct fields and YAML keys sorted
  alphabetically, 3-group Go imports; on the frontend `PascalCase` component
  files, `data-test` attributes for Cypress selectors, `kialiStyle`/PF
  design tokens for styling, and i18n via `import { t } from 'utils/I18nUtils'`.
  ^[raw/articles/kiali-repo-contributing.md] ^[raw/articles/kiali-repo-agents.md]
- **Internationalization** — adding a language or improving an existing one
  follows `frontend/README.adoc` (Internationalization section) plus the shared
  `I18N-AGENTS.md` glossary/style rules (Spanish and Chinese). ^[raw/articles/kiali-repo-contributing.md]

## Commit signing (required)

**All repositories in the Kiali organization require commits to be
cryptographically signed.** Set this up *before* submitting any changes. The
canonical walkthrough is `COMMIT-SIGNING-SETUP.md` in the repo:
^[raw/articles/COMMIT-SIGNING-SETUP.md]

1. **Generate an ed25519 signing key** with your primary verified GitHub
   email (`ssh-keygen -t ed25519 -C "<your-email>" -f ~/.ssh/github_signing_key`).
   Pressing Enter twice skips the passphrase; if you set one, it's only needed
   when loading the key into the agent, and many Linux desktops (e.g. Fedora
   with GNOME) auto-load keys at login.
2. **Configure git:**

   ```bash
   git config --global user.email "<your-email>"
   git config --global gpg.format ssh
   git config --global user.signingkey ~/.ssh/github_signing_key.pub
   git config --global commit.gpgsign true
   ```

3. **Load the key into your SSH agent:** `ssh-add ~/.ssh/github_signing_key`
4. **Copy the public key** (`cat ~/.ssh/github_signing_key.pub`).
5. **Upload to GitHub** — https://github.com/settings/keys → "New SSH key" →
   name it (e.g. "Signing Key") → **set the key type to "Signing Key"** (not
   "Authentication Key") → paste → Add.
6. **Enable Vigilant Mode** on the same page: "Flag unsigned commits as
   unverified".
7. **Local verification (optional but recommended)** — without this,
   `git log --show-signature` errors even on properly signed commits. Create an
   allowed signers file:

   ```bash
   echo "$(git config --global user.email) $(cat ~/.ssh/github_signing_key.pub)" > ~/.ssh/allowed_signers
   git config --global gpg.ssh.allowedSignersFile ~/.ssh/allowed_signers
   ```

8. **Verify:** `git commit --allow-empty -m "test: verify commit signing"` →
   `git log --show-signature -1` → `git reset HEAD~1`. The output must show
   `Good "git" signature` with your email (or push the test commit first and
   check the "Verified" badge on GitHub before resetting).
   ^[raw/articles/COMMIT-SIGNING-SETUP.md]

## AI-assisted contributions (AI Policy)

Contributors who use AI tools must follow the repo's `AI_POLICY.md` (aligned
with the Linux Foundation and CNCF guidelines): humans remain fully
accountable for all AI-generated code, and AI assistance is **required** to be
disclosed via `Assisted-by` / `Generated-by` trailers and comments. Blind
submission, license violations, and gaming the system are prohibited.
Full policy: [[kiali-ai-contributions]]. ^[raw/articles/kiali-repo-ai-policy.md]
## Submitting changes (PR workflow)

Once the issue is agreed and implemented: ^[raw/articles/kiali-repo-contributing.md]

- **Never push feature branches to upstream** `kiali/*` repos. Always push to
  your **personal fork** and open the PR from there. Before pushing, run
  `git remote -v` to confirm which remote is your fork (your username) and
  which is upstream (`kiali/*`); if you have no fork remote, stop and ask.
- **Write a detailed PR description** — explain the changes in detail
  (screenshots for UI changes) and **link the originating issue**.
- **Expect iterative review** — the committer team reviews, you incorporate
  feedback by adding further commits, until the PR is merged.

The repo's `AGENTS.md` documents the org-membership workflow for after the PR
exists (org members only): add yourself as **assignee**
(`gh pr edit <N> --repo <REPO> --add-assignee <USER>`), add the PR to the
**Kiali GitHub Project** (`gh project item-add <PROJECT> --owner kiali
--url <PR_URL>`), set its status (**"In progress"** for draft PRs, **"In
review"** for ready PRs), and request reviewers
(`gh pr edit <N> --repo <REPO> --add-reviewer <USER>`).
^[raw/articles/kiali-repo-agents.md]

### Pre-commit checklist (from AGENTS.md)

Before committing: `make format lint`; `make test`; remove trailing
whitespace; sort struct fields and YAML keys alphabetically; build UI before
backend (`make build-ui` then `make build`). ^[raw/articles/kiali-repo-agents.md]

### Backporting to older versions

Kiali maintains versioned release branches (see [[kiali-release-process]]).
The backport checklist: duplicate changes from `kiali-operator/roles/default/`
into the versioned roles as appropriate, and cherry-pick the changes to the
appropriate git branches. ^[raw/articles/kiali-repo-agents.md]

## Roles in the project (summary)

Kiali's governance doc defines **Maintainers** (write access to the org's
repos; can merge own and others' patches; elevated via nomination — 3+ months
of participation, 10 non-trivial PR reviews, 10 non-trivial merged PRs,
proposed by a maintainer with a second from another, 5-working-day objection
window, then simple-majority vote if contested), **Testers** (same privileges
granted in good faith for active system/integration testing; 3+ months of PR
testing and 5 non-trivial defects found; simple-majority vote to formalize),
and **Leaders** (maintainers with project-wide direction and mentoring
role; simple-majority vote). Inactivity policies apply to all. The full
details, current rosters, and inactivity rules belong to the community/governance
page; the raw source is `kiali-repo-governance.md`.
^[raw/articles/kiali-repo-governance.md]

## Related

- [[kiali-build-and-dev]] — build system, clusters, test suites, CI
- [[kiali-release-process]] — cadence, branches, backports, release mechanics
- [[kiali-keps]] — proposing large enhancements
- [[kiali-architecture]] — what you are contributing to
- [[kiali-ai-contributions]] — full AI-assisted contribution policy
