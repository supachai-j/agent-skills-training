---
id: tool:skills-ref
type: tool
title: skills-ref reference SDK + validator
status: active
confidence: 0.85
sources:
  - raw/2026-05-08-agentskills-io-specification.md
  - raw/2026-05-08-agentskills-io-adding-skills-support.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created
tiers: semantic
half_life_days: 180
tags: [deck]
---

# `skills-ref`

## Summary

The official reference SDK + CLI for the Agent Skills standard. Validates `SKILL.md` against the canonical frontmatter rules and naming conventions, and ships the parser/loader logic that downstream clients can re-use.

- Repo: <https://github.com/agentskills/agentskills/tree/main/skills-ref>

## Usage

```bash
skills-ref validate ./my-skill
```

Checks:
- Frontmatter parses as YAML.
- `name` and `description` are present.
- `name`: 1-64 chars, lowercase + hyphens, no leading/trailing `-`, no `--`, **matches parent directory name**.
- `description`: 1-1024 chars.
- Optional fields obey their constraints (`compatibility` ≤500 chars; `metadata` is string→string).

`[src: raw/2026-05-08-agentskills-io-specification.md] {conf: 0.9}`

## Why use it

- Catches naming bugs before publishing.
- A canonical, well-tested parser to embed if you're writing a Skills client (instead of reinventing YAML edge-cases).
- Aligns with the lenient-but-warn approach recommended for client implementers.

## Relationships

- composes → [[feature:open-standard]] `{conf: 0.9}`
- depends-on → [[concept:skill-md]] `{conf: 0.9}`
- composes → [[pattern:client-implementation]] `{conf: 0.85}`

## Changelog

- 2026-05-08 — created.
