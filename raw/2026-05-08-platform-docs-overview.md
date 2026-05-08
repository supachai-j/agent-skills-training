---
source_type: web
source_url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
ingested_at: 2026-05-08
title: Agent Skills overview (Claude Developer Platform docs)
---

# Agent Skills — Platform docs overview

## Definition

Modular capabilities that extend Claude's functionality. Each Skill packages instructions, metadata, and optional resources (scripts, templates).

## Skill content + loading levels

| Level | When loaded | Token cost | Content |
|---|---|---|---|
| L1 Metadata | Always (startup) | ~100 tokens / skill | `name` + `description` |
| L2 Instructions | When triggered | < 5k tokens | SKILL.md body |
| L3+ Resources | As needed | Effectively unlimited | Bundled files via bash |

## Frontmatter validation

- `name` — max 64 chars, lowercase letters/numbers/hyphens, no XML, no reserved words ("anthropic", "claude").
- `description` — non-empty, max 1024 chars, no XML.
- Description should describe both **what** and **when** to use.

## Architecture

Skills live in a code-execution VM with filesystem + bash + code execution. Claude `cat`s SKILL.md on trigger; references propagate through bash; scripts execute and only output enters context.

> No practical limit on bundled content. Files don't consume context until accessed.

## Surfaces

| Surface | Pre-built | Custom | Notes |
|---|---|---|---|
| Claude API | Yes | Yes (org-wide) | needs beta headers `code-execution-2025-08-25`, `skills-2025-10-02`, `files-api-2025-04-14` |
| Claude.ai | Yes | Yes (per-user, ZIP upload) | Pro/Max/Team/Enterprise |
| Claude Code | No (FS-based custom only) | Yes (`~/.claude/skills/` or `.claude/skills/`) | Can be packaged as plugins |

## Cross-surface limitations

Custom Skills do not sync across surfaces — upload separately for API, Claude.ai, and Claude Code.

## Sharing scope

- Claude.ai: per-user.
- API: workspace-wide.
- Claude Code: personal `~/.claude/skills/` or project `.claude/skills/`; can ship via plugins.

## Runtime constraints

- Claude.ai: variable network (admin policy).
- API: no network, no runtime install — pre-installed packages only.
- Claude Code: full network, but skills should install packages locally.

## Security

> Skills provide Claude with new capabilities through instructions and code, and while this makes them powerful, it also means a malicious Skill can direct Claude to invoke tools or execute code in ways that don't match the Skill's stated purpose.

Treat installing a Skill like installing software. Audit thoroughly. External-URL-fetching skills are particularly risky.
