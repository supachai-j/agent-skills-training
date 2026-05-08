---
id: feature:claude-api-skills
type: feature
title: Skills via the Claude API
status: active
confidence: 0.85
sources:
  - raw/2026-05-08-platform-docs-overview.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created
tiers: semantic
half_life_days: 180
tags: [deck]
---

# Skills via the Claude API

## Summary

Both pre-built Anthropic Skills (PowerPoint, Excel, Word, PDF) and custom organisation-uploaded Skills run inside the API's code-execution container. Reference them by `skill_id` in the `container` parameter alongside the code-execution tool.

## Claims

- Three beta headers required: `code-execution-2025-08-25`, `skills-2025-10-02`, `files-api-2025-04-14`. `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.9}`
- Pre-built `skill_id`s include `pptx`, `xlsx`, `docx`, `pdf`. `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.95}`
- Custom Skills uploaded via `/v1/skills` endpoints are **workspace-wide** and shared across the org. `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.9}`
- API runtime: **no network access**, no runtime package installation — only pre-installed packages. `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.95}`
- API Skills **not** covered by Zero-Data-Retention (ZDR). `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.9}`

## Relationships

- composes → [[feature:agent-skills]] `{conf: 0.95}`
- alternative-to → [[feature:claude-code-skills]] `{conf: 0.6}`

## Open questions

- [ ] When will ZDR support land for Skills?

## Changelog

- 2026-05-08 — created.
