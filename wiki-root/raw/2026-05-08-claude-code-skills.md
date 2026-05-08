---
source_type: web
source_url: https://code.claude.com/docs/en/skills
ingested_at: 2026-05-08
title: Extend Claude with skills (Claude Code docs)
---

# Skills in Claude Code

## What

A `SKILL.md` file in a directory becomes a tool Claude can use, or a slash command you can invoke as `/skill-name`. Custom commands (`.claude/commands/*.md`) have been merged into skills.

> Claude Code skills follow the [Agent Skills](https://agentskills.io) open standard, which works across multiple AI tools.

Claude Code adds: invocation control, subagent execution (`context: fork`), dynamic context injection.

## Where skills live (precedence)

| Location | Path | Scope |
|---|---|---|
| Enterprise | managed settings | org-wide |
| Personal | `~/.claude/skills/<name>/SKILL.md` | all your projects |
| Project | `.claude/skills/<name>/SKILL.md` | this project |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | where plugin enabled |

Precedence: enterprise > personal > project. Plugin skills are namespaced `plugin-name:skill-name`.

## Frontmatter fields (Claude Code extras)

| Field | Purpose |
|---|---|
| `name` | display name (defaults to dir) |
| `description` | what + when |
| `when_to_use` | extra context, trigger phrases |
| `argument-hint` | shown in autocomplete |
| `arguments` | named positional args |
| `disable-model-invocation` | only user can `/skill` (no auto) |
| `user-invocable` | hide from `/` menu (Claude-only) |
| `allowed-tools` | pre-approved tools when active |
| `model` | model override for current turn |
| `effort` | `low|medium|high|xhigh|max` |
| `context: fork` | run in subagent |
| `agent` | which subagent (`Explore`, `Plan`, custom) |
| `hooks` | skill-scoped hooks |
| `paths` | glob patterns to scope auto-trigger |
| `shell` | `bash` (default) or `powershell` |

## String substitutions

- `$ARGUMENTS` — full arg string
- `$ARGUMENTS[N]` / `$N` — positional
- `$name` — named arg
- `${CLAUDE_SESSION_ID}` — current session
- `${CLAUDE_EFFORT}` — active effort level
- `${CLAUDE_SKILL_DIR}` — directory of the skill (use to reference bundled scripts portably)

## Dynamic context injection

`` !`<command>` `` — runs the command before Claude sees the skill, replacing the placeholder with output. Multi-line:

```!
node --version
git status --short
```

Disable with `"disableSkillShellExecution": true`.

## Skill content lifecycle

> When you or Claude invoke a skill, the rendered SKILL.md content enters the conversation as a single message and stays there for the rest of the session.

Auto-compaction: re-attaches latest invocation of each skill, first 5,000 tokens, combined budget 25,000 tokens.

## Pre-approve tools

`allowed-tools: Bash(git add *) Bash(git commit *) Bash(git status *)` — grants permission while skill active. Project skills require workspace trust before `allowed-tools` activate.

## context: fork

Runs skill in isolated subagent. Skill body becomes the prompt; `agent` field sets the system prompt + tool set. Examples: `Explore` for read-only research; `Plan` for design. Best for skills with explicit action prompts (not pure reference content).

## Restrict Claude's skill access

- Deny the `Skill` tool entirely.
- `Skill(name)` exact, `Skill(name *)` prefix.
- `disable-model-invocation: true` removes a skill from Claude's context.
- `skillOverrides` setting: `"on" | "name-only" | "user-invocable-only" | "off"`.

## Description budget

- Skill descriptions share a budget. Default 1% of context window, fallback 8,000 chars.
- `SLASH_COMMAND_TOOL_CHAR_BUDGET` env var raises it.
- Per-skill cap: 1,536 chars (description + when_to_use).
