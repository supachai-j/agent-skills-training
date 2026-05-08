---
id: feature:claude-code-skills
type: feature
title: Skills in Claude Code
status: active
confidence: 0.9
sources:
  - raw/2026-05-08-claude-code-skills.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created
tiers: semantic
half_life_days: 180
tags: [deck]
---

# Skills in Claude Code

## Summary

In Claude Code, a Skill is a directory under `~/.claude/skills/` (personal), `.claude/skills/` (project), an enterprise managed location, or a plugin's `skills/` folder. The directory name becomes the slash command (`/skill-name`). Custom commands have been merged into Skills — `.claude/commands/<name>.md` and `.claude/skills/<name>/SKILL.md` both create `/<name>`.

## Claims

- Claude Code only supports **custom** Skills (filesystem-based). `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.9}`
- Precedence: enterprise > personal > project; plugin skills are namespaced `plugin-name:skill-name` and don't conflict. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.9}`
- Live change detection: edits in skill directories take effect within the current session without restart. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.9}`
- Nested-directory discovery: subdirectory `.claude/skills/` paths are picked up (monorepo-friendly). `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.85}`
- `disable-model-invocation: true` → only the user can invoke; useful for actions with side effects (e.g. `/deploy`). `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.95}`
- `user-invocable: false` → only Claude can invoke; for background reference content. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.9}`
- `allowed-tools` pre-approves tools while the skill is active; project skills require workspace trust before this activates. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.9}`
- `context: fork` runs the skill in a forked subagent with no access to the main conversation history; `agent` selects the subagent type. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.9}`
- Dynamic context injection — `` !`cmd` `` runs before Claude sees the skill; output replaces placeholder. Multi-line ` ```! ` blocks supported. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.95}`
- Skill content lifecycle: once invoked, the rendered SKILL.md content stays in the conversation as a single message for the rest of the session. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.9}`
- After auto-compaction Claude Code re-attaches the most recent invocation of each skill (first 5,000 tokens each, 25,000-token combined budget). `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.85}`
- `${CLAUDE_SKILL_DIR}` resolves to the directory containing SKILL.md — use it to call bundled scripts portably regardless of CWD. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.9}`
- Description budget is 1% of the context window (fallback 8,000 chars), per-skill cap 1,536 chars; tunable via `SLASH_COMMAND_TOOL_CHAR_BUDGET`. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.9}`

## Relationships

- composes → [[feature:agent-skills]] `{conf: 0.95}`
- depends-on → [[concept:skill-md]] `{conf: 0.95}`
- alternative-to → [[concept:slash-commands]] `{conf: 0.7}`
- composes → [[concept:subagents]] `{conf: 0.7}` (via `context: fork`)
- composes → [[concept:hooks]] `{conf: 0.6}` (skill-scoped hooks)

## Open questions

- [ ] Best practices for organising plugin-namespaced skills.

## Changelog

- 2026-05-08 — created.
