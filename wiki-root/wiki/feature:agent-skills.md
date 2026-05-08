---
id: feature:agent-skills
type: feature
title: Agent Skills
status: active
confidence: 0.95
sources:
  - raw/2026-05-08-anthropic-engineering-skills.md
  - raw/2026-05-08-platform-docs-overview.md
  - raw/2026-05-08-claude-code-skills.md
  - raw/2026-05-08-agentskills-io-home.md
  - raw/2026-05-08-agentskills-io-specification.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created from primary sources
  - 2026-05-08: reinforced from agentskills.io (open-standard authority + ecosystem)
tiers: semantic
half_life_days: 180
tags: [deck, core]
---

# Agent Skills

## Summary

**Agent Skills** are organised folders of instructions, scripts, and resources that an agent can discover and load **dynamically** to perform better on specific tasks. They are the Anthropic-defined way to package procedural knowledge — like an onboarding guide for a new hire — into a portable, composable unit. Each Skill is a directory whose entrypoint is a `SKILL.md` file with YAML frontmatter (`name` + `description`) and markdown instructions, optionally bundled with extra `.md` references and executable scripts.

## Claims

- A Skill is "an organized folder of instructions, scripts, and resources" loaded dynamically. `[src: raw/2026-05-08-anthropic-engineering-skills.md] {conf: 0.95}`
- Skills are designed around **progressive disclosure** — see [[concept:progressive-disclosure]]. `[src: raw/2026-05-08-anthropic-engineering-skills.md, raw/2026-05-08-platform-docs-overview.md] {conf: 0.95}`
- Skills are available on claude.ai, Claude Code, the Claude Agent SDK, and the Claude Developer Platform. `[src: raw/2026-05-08-anthropic-engineering-skills.md] {conf: 0.9}`
- Custom Skills do **not** sync across surfaces — must be uploaded separately to API, claude.ai, and Claude Code. `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.9}`
- Skills *complement* MCP: Skills teach how, MCP gives access. `[src: raw/2026-05-08-anthropic-engineering-skills.md, raw/2026-05-08-skills-vs-mcp-vs-subagents.md] {conf: 0.9}`
- Anthropic recommends installing skills only from trusted sources because malicious skills can hijack tool use. `[src: raw/2026-05-08-anthropic-engineering-skills.md, raw/2026-05-08-platform-docs-overview.md] {conf: 0.9}`
- Skills are published as an **open standard** at agentskills.io — see [[feature:open-standard]]. `[src: raw/2026-05-08-claude-code-skills.md, raw/2026-05-08-agentskills-io-home.md] {conf: 0.95}`
- The standard has been adopted by ~38+ agent products as of May 2026 — Claude Code, Claude.ai, GitHub Copilot, VS Code, OpenAI Codex, Cursor, Gemini CLI, OpenCode, OpenHands, Goose, Letta, Roo Code, Mistral Vibe, Snowflake Cortex Code, Databricks Genie, Spring AI, Laravel Boost, Kiro, Factory, Junie, Amp, etc. `[src: raw/2026-05-08-agentskills-io-home.md] {conf: 0.9}`

## Relationships

- composes → [[feature:open-standard]] `{conf: 0.95}` (the formal definition)
- composes → [[feature:claude-code-skills]] `{conf: 0.9}`
- composes → [[feature:claude-api-skills]] `{conf: 0.9}`
- composes → [[feature:claude-ai-skills]] `{conf: 0.9}`
- depends-on → [[concept:skill-md]] `{conf: 0.95}`
- depends-on → [[concept:progressive-disclosure]] `{conf: 0.95}`
- depends-on → [[concept:cross-client-convention]] `{conf: 0.85}`
- alternative-to → [[concept:slash-commands]] `{conf: 0.6}` (Claude Code merged commands into skills)
- alternative-to → [[feature:mcp]] `{conf: 0.5}` (different but adjacent)

## Open questions

- [ ] Roadmap for cross-surface sync.
- [ ] Adoption rate of agentskills.io standard outside Anthropic.

## Changelog

- 2026-05-08 — created from three primary sources.
