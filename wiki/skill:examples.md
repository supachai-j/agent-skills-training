---
id: skill:examples
type: skill
title: Worked Skill examples
status: active
confidence: 0.85
sources:
  - raw/2026-05-08-claude-code-skills.md
  - raw/2026-05-08-best-practices.md
  - raw/2026-05-08-platform-docs-overview.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created
tiers: semantic
half_life_days: 180
tags: [deck]
---

# Worked Skill examples

## Summary

Three concrete Skills from the docs that illustrate the full range — pure markdown reference, dynamic-context wrapper, and bundled-script visualisation.

## Example 1 — `summarize-changes` (dynamic context)

```yaml
---
description: Summarizes uncommitted changes and flags anything risky. Use when the user asks what changed, wants a commit message, or asks to review their diff.
---

## Current changes

!`git diff HEAD`

## Instructions

Summarize the changes above in two or three bullet points, then list any risks
you notice such as missing error handling, hardcoded values, or tests that need
updating. If the diff is empty, say there are no uncommitted changes.
```

`!`git diff HEAD`` runs **before** Claude sees the skill — Claude is grounded in real diff output, not guesses. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.95}`

## Example 2 — `deploy` (locked-down user-only action)

```yaml
---
name: deploy
description: Deploy the application to production
disable-model-invocation: true
allowed-tools: Bash(git push *) Bash(./scripts/deploy *)
---
Deploy $ARGUMENTS to production:
1. Run the test suite
2. Build the application
3. Push to the deployment target
4. Verify the deployment succeeded
```

`disable-model-invocation: true` ensures Claude won't auto-deploy. `allowed-tools` skips per-command approval prompts. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.95}`

## Example 3 — `codebase-visualizer` (bundled Python + browser HTML)

Layout:
```
~/.claude/skills/codebase-visualizer/
├── SKILL.md
└── scripts/
    └── visualize.py
```

SKILL.md uses `${CLAUDE_SKILL_DIR}` for path-portability:

```yaml
---
name: codebase-visualizer
description: Generate an interactive collapsible tree visualization of your codebase. Use when exploring a new repo, understanding project structure, or identifying large files.
allowed-tools: Bash(python3 *)
---
python3 ${CLAUDE_SKILL_DIR}/scripts/visualize.py .
```

The Python script writes `codebase-map.html` and opens it in a browser. Claude orchestrates; the script does the work. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.95}`

## Example 4 — `pdf-processing` (Anthropic pre-built)

The pre-built `pdf` Skill demonstrates Pattern 1 progressive disclosure: lean SKILL.md, sidecar `FORMS.md`, `REFERENCE.md`, `EXAMPLES.md`, and a `scripts/` folder of utility Python. `[src: raw/2026-05-08-platform-docs-overview.md, raw/2026-05-08-best-practices.md] {conf: 0.9}`

## Relationships

- composes → [[feature:claude-code-skills]] `{conf: 0.9}`
- depends-on → [[concept:skill-md]] `{conf: 0.95}`
- depends-on → [[pattern:authoring-best-practices]] `{conf: 0.85}`

## Changelog

- 2026-05-08 — created.
