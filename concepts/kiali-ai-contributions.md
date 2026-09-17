---
title: AI-Assisted Contributions to Kiali
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, contribution, ai, reference]
sources: [raw/articles/kiali-repo-contributing.md, raw/articles/kiali-repo-ai-policy.md, raw/articles/COMMIT-SIGNING-SETUP.md, raw/articles/kiali-repo-agents.md, raw/articles/kiali-repo-governance.md]
confidence: high
---

# AI-Assisted Contributions to Kiali

Contributors who use AI tools (GitHub Copilot, ChatGPT, Claude, Cursor, or
similar) must follow the repo's `AI_POLICY.md`, which is aligned with the
Linux Foundation Generative AI Policy and CNCF guidelines. ^[raw/articles/kiali-repo-ai-policy.md]

**Core principles** — human accountability (all contributions must be reviewed,
understood, and validated by humans; you remain fully responsible regardless of
how the code was created), open source values, and quality/security
(supersedes speed; full testing required).

**Permitted uses** — AI may assist with code development (boilerplate,
well-defined implementations, refactoring, test writing), documentation
(drafting, clarity, API docs, examples), code review/analysis (finding bugs,
explaining code), and development assistance (debugging, research,
understanding unfamiliar code, generating regex/queries).

**Required practices** when AI assistance is used: ^[raw/articles/kiali-repo-ai-policy.md]

- **Understand the code** — review all AI-generated code, be able to explain
  and defend it in review.
- **Verify license compliance** — the AI tool's terms must not conflict with
  Kiali's Apache 2.0 license.
- **Address third-party materials** — if output contains copyrighted
  third-party code: verify permission, license compatibility, provide
  attribution; prefer tools that flag/suppress similar responses.
- **Test thoroughly** — AI-assisted code must ship with passing tests.
- **Disclose AI assistance — REQUIRED.** In commit messages and PR
  descriptions, identify the assistant used via a trailer, and in source files
  via a comment:

  ```
  Assisted-by: Claude Code
  ```

  ```go
  // Assisted-by: Claude Code
  ```

  ```bash
  # Generated-by: Cursor
  ```

  Maintainers may request additional information about code origin during
  reviews.

**Prohibited:** blind submission (unreviewed AI output you cannot explain or
maintain), license violations, security negligence, gaming the system (bulk
AI submissions to inflate contribution metrics, simulated community
engagement), and misrepresentation of authorship or code origin.

**Documentation & design docs** — AI-assisted docs are encouraged if
technically accurate, human-reviewed, and with verified examples. For design
documents/KEPs, the human author must genuinely understand and support the
design; community iteration is expected. **AI-generated images:** technical
diagrams are fine if accurate and not copyrighted elsewhere; prefer original
screenshots and properly licensed media; avoid decorative AI artwork.

**Employer policies** — contributors must also comply with their employer's
AI/open-source/IP policies; if an employer policy conflicts with Kiali's,
discuss with maintainers before contributing. Questions go to Slack or GitHub
Discussions. ^[raw/articles/kiali-repo-ai-policy.md]

## Related

- [[kiali-contribution]] — the full contribution workflow: pre-work, commit signing, PR process
- [[kiali-ai-chat-and-mcp]] — the AI features this policy applies to
- [[kiali-keps]] — design proposals; AI-assisted design docs have extra rules
