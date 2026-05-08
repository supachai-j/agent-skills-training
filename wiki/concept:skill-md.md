---
id: concept:skill-md
type: concept
title: SKILL.md file format
status: active
confidence: 0.96
sources:
  - raw/2026-05-08-platform-docs-overview.md
  - raw/2026-05-08-claude-code-skills.md
  - raw/2026-05-08-best-practices.md
  - raw/2026-05-08-agentskills-io-specification.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created
  - 2026-05-08: reinforced from agentskills.io spec + added open-standard fields
tiers: semantic
half_life_days: 180
tags: [deck, core]
---

# SKILL.md

## Summary

`SKILL.md` is the entrypoint of every Skill. It has YAML frontmatter at the top (between `---` markers) and markdown content below. The frontmatter is what Claude scans across **all** installed skills at startup to decide which one to load when. The markdown body is the procedural knowledge that arrives in context once the skill is triggered.

```yaml
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---

# PDF Processing
... markdown body ...
```

## Claims

- Required frontmatter fields: `name` and `description`. `[src: raw/2026-05-08-platform-docs-overview.md, raw/2026-05-08-agentskills-io-specification.md] {conf: 0.97}`
- `name`: ≤64 chars, lowercase letters/numbers/hyphens only, no XML tags, cannot use reserved words `anthropic` or `claude` (Anthropic clients). `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.95}`
- Open-standard `name` rules (per agentskills.io spec): 1-64 chars · no leading/trailing hyphen · no consecutive `--` · **must match the parent directory name**. `[src: raw/2026-05-08-agentskills-io-specification.md] {conf: 0.95}`
- `description`: non-empty, ≤1024 chars (≤1,536 with `when_to_use` in Claude Code's listing). `[src: raw/2026-05-08-platform-docs-overview.md, raw/2026-05-08-claude-code-skills.md, raw/2026-05-08-agentskills-io-specification.md] {conf: 0.95}`
- Open-standard optional fields: `license`, `compatibility` (≤500 chars), `metadata` (string→string map), `allowed-tools` (experimental). `[src: raw/2026-05-08-agentskills-io-specification.md] {conf: 0.9}`
- Description must always be in **third person** — first/second person harms discovery. `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`
- Description must include both **what** the Skill does *and* **when** to use it. `[src: raw/2026-05-08-best-practices.md] {conf: 0.95}`
- SKILL.md body should be **under 500 lines**; longer content goes in sibling `.md` files. `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`
- Claude Code adds extra fields: `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `model`, `effort`, `context: fork`, `agent`, `hooks`, `paths`, `shell`. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.9}`
- Claude Code supports string substitutions: `$ARGUMENTS`, `$N`, `$name`, `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}`, `${CLAUDE_SKILL_DIR}`. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.9}`

## Relationships

- depends-on → [[feature:agent-skills]] `{conf: 0.95}`
- depends-on → [[feature:open-standard]] `{conf: 0.95}`
- composes → [[concept:progressive-disclosure]] `{conf: 0.9}`
- depends-on → [[pattern:authoring-best-practices]] `{conf: 0.85}`
- composes → [[tool:skills-ref]] `{conf: 0.85}` (validator)

## Open questions

- [ ] How are competing schema extensions (e.g., from VS Code's adoption) reconciled with Anthropic's spec?

## Changelog

- 2026-05-08 — created.
