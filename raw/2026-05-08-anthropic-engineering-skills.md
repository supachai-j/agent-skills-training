---
source_type: web
source_url: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
ingested_at: 2026-05-08
title: Equipping agents for the real world with Agent Skills (Anthropic Engineering)
---

# Equipping agents for the real world with Agent Skills

Anthropic engineering blog on Agent Skills. Captured key extracts (paraphrased + direct quotes).

## What Agent Skills are

> Agent Skills are organized folders of instructions, scripts, and resources that agents can discover and load dynamically to perform better at specific tasks.

> Building a skill for an agent is like putting together an onboarding guide for a new hire.

Rather than building separate custom agents per use case, anyone can specialise an agent with composable capabilities by capturing and sharing procedural knowledge.

## SKILL.md format

- Root file: `SKILL.md`.
- YAML frontmatter required: `name` + `description`.
- Metadata is loaded into the system prompt at startup.

## Progressive disclosure (3 levels)

- **L1 — Metadata only**: name + description preloaded into system prompt at startup.
- **L2 — Core content**: Claude reads the full `SKILL.md` via Bash when it decides the skill is relevant.
- **L3 — Supplementary**: bundled files (`reference.md`, `forms.md`, scripts) read or executed only when needed.

> Agents with a filesystem and code execution tools don't need to read the entirety of a skill into their context window when working on a particular task. This means that the amount of context that can be bundled into a skill is effectively unbounded.

## Authoring methodology (5 steps)

1. Start with evaluation — find capability gaps with representative tasks.
2. Structure for scale — split SKILL.md into separate files when it grows.
3. Think from Claude's perspective — watch real usage; iterate name/description.
4. Iterate with Claude — ask Claude to capture successful approaches into reusable skills.
5. Code vs documentation — be explicit about whether Claude executes or reads.

## Security

Skills are powerful → malicious skills are dangerous. Recommendations:
- Install only from trusted sources.
- Audit code, dependencies, and bundled assets.
- Be wary of skills that fetch external URLs.

## Where Skills run

- claude.ai
- Claude Code
- Claude Agent SDK
- Claude Developer Platform / Claude API

Skills complement MCP — Skills teach how, MCP gives access.
