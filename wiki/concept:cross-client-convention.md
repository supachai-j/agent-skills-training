---
id: concept:cross-client-convention
type: concept
title: .agents/skills cross-client convention
status: active
confidence: 0.9
sources:
  - raw/2026-05-08-agentskills-io-adding-skills-support.md
  - raw/2026-05-08-agentskills-io-quickstart.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created
tiers: semantic
half_life_days: 180
tags: [deck]
---

# `.agents/skills/` cross-client convention

## Summary

The Agent Skills spec **does not mandate** where skill directories live; it only defines what goes inside them. By convention, **`.agents/skills/`** is the cross-client path that all conformant agents are encouraged to scan in addition to their own native location. Drop a skill there, and Copilot, Cursor, Claude Code, OpenAI Codex, Gemini CLI etc. all see it.

## Scan paths

| Scope | Native (per-client) | Cross-client |
|---|---|---|
| Project | `<project>/.<your-client>/skills/` | `<project>/.agents/skills/` |
| User | `~/.<your-client>/skills/` | `~/.agents/skills/` |

`[src: raw/2026-05-08-agentskills-io-adding-skills-support.md] {conf: 0.95}`

## Pragmatic note

Many newer clients also scan **`.claude/skills/`** for compatibility, since so many existing skills already live there. `[src: raw/2026-05-08-agentskills-io-adding-skills-support.md] {conf: 0.9}`

## Claims

- VS Code's Copilot scans `.agents/skills/` by default — see Quickstart. `[src: raw/2026-05-08-agentskills-io-quickstart.md] {conf: 0.95}`
- Universal precedence rule: **project-level overrides user-level**. `[src: raw/2026-05-08-agentskills-io-adding-skills-support.md] {conf: 0.95}`
- Recommended bound: max depth 4–6, max ~2,000 directories scanned, skip `.git/`/`node_modules/`. `[src: raw/2026-05-08-agentskills-io-adding-skills-support.md] {conf: 0.85}`

## Implications for authors

- Place team skills under your repo at `.agents/skills/<name>/SKILL.md` for maximum portability.
- Personal skills live at `~/.agents/skills/<name>/SKILL.md`.
- Avoid bespoke client-only paths unless the skill genuinely depends on client-specific frontmatter (e.g. Claude Code's `context: fork`).

## Relationships

- composes → [[feature:open-standard]] `{conf: 0.95}`
- alternative-to → [[feature:claude-code-skills]] `{conf: 0.6}` (Claude Code's `~/.claude/skills/` is one of many native paths)

## Changelog

- 2026-05-08 — created.
