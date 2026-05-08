---
id: concept:progressive-disclosure
type: concept
title: Progressive disclosure
status: active
confidence: 0.95
sources:
  - raw/2026-05-08-anthropic-engineering-skills.md
  - raw/2026-05-08-platform-docs-overview.md
  - raw/2026-05-08-best-practices.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created
tiers: semantic
half_life_days: 180
tags: [deck, core]
---

# Progressive disclosure

## Summary

Progressive disclosure is the **core design principle** that makes Skills scale: information is loaded into the context window in stages, only as needed. Like a well-organised manual — table of contents, then chapters, then appendix — Skills expose only their metadata at startup and pull in the rest as the agent decides it's relevant.

## The three levels

| Level | Content | When loaded | Token cost |
|---|---|---|---|
| **L1 — Metadata** | `name` + `description` from frontmatter | Always (startup) | ~100 tokens / skill |
| **L2 — Instructions** | Body of `SKILL.md` | When the skill is triggered | < ~5,000 tokens |
| **L3+ — Resources** | Bundled `.md` references, scripts, data | On-demand via bash | Effectively unlimited |

## Claims

- Three-level loading model: metadata → SKILL.md body → bundled files. `[src: raw/2026-05-08-platform-docs-overview.md, raw/2026-05-08-anthropic-engineering-skills.md] {conf: 0.95}`
- ~100 tokens per skill in L1 metadata. `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.9}`
- L3 bundled content is "effectively unbounded" because files don't enter context until accessed. `[src: raw/2026-05-08-anthropic-engineering-skills.md, raw/2026-05-08-platform-docs-overview.md] {conf: 0.95}`
- Scripts execute via bash — only their **output** consumes tokens, not their source code. `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.9}`
- Authoring rule: keep references **one level deep** from SKILL.md so Claude reads complete files. `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`
- Reference files >100 lines should include a Contents block. `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`

## Why it matters

> Without progressive disclosure, installing ten skills would stuff your agent's context window with instructions leaving barely any room for conversation; with progressive disclosure you can have dozens or hundreds of skills installed and the overhead is negligible. `[src: raw/2026-05-08-anthropic-engineering-skills.md] {conf: 0.95}`

## Relationships

- composes → [[feature:agent-skills]] `{conf: 0.95}`
- composes → [[concept:skill-md]] `{conf: 0.9}`
- depends-on → [[concept:context-window]] `{conf: 0.8}`

## Open questions

- [ ] What's the empirical impact on selection accuracy when skill count ≫ 100?

## Changelog

- 2026-05-08 — created.
