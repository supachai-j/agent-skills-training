---
source_type: web
source_url: https://agentskills.io
ingested_at: 2026-05-08
title: agentskills.io — Open standard home page
---

# agentskills.io — Overview

## Definition (from the standard's home page)

> Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.
>
> At its core, a skill is a folder containing a `SKILL.md` file. This file includes metadata (`name` and `description`, at minimum) and instructions that tell an agent how to perform a specific task. Skills can also bundle scripts, reference materials, templates, and other resources.

## Canonical folder layout

```
my-skill/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

The names `scripts/`, `references/`, `assets/` are the conventional sibling directories.

## Three-stage progressive disclosure (verbatim)

1. **Discovery** — At startup, agents load only the name and description of each available skill, just enough to know when it might be relevant.
2. **Activation** — When a task matches a skill's description, the agent reads the full `SKILL.md` instructions into context.
3. **Execution** — The agent follows the instructions, optionally executing bundled code or loading referenced files as needed.

## Open development

> The Agent Skills format was originally developed by Anthropic, released as an open standard, and has been adopted by a growing number of agent products. The standard is open to contributions from the broader ecosystem.

- GitHub: <https://github.com/agentskills/agentskills>
- Discord: <https://discord.gg/MKPE9g8aUy>

## Adopters (Client Showcase, partial list captured 2026-05-08)

A non-trivial cross-vendor ecosystem already supports the format:

- Junie (JetBrains)
- Gemini CLI (Google)
- OpenCode (sst)
- OpenHands
- Mux (coder.com)
- Cursor
- Amp (Sourcegraph)
- Letta
- Firebender
- Goose (Block)
- GitHub Copilot
- VS Code
- Claude Code
- Claude (claude.ai)
- OpenAI Codex
- Piebald
- Factory
- Pi
- Databricks Genie Code
- Agentman
- TRAE (ByteDance)
- Spring AI
- Roo Code
- Mistral Vibe
- Command Code
- Ona
- VT Code
- Qodo
- Laravel Boost
- Emdash
- Snowflake Cortex Code
- Kiro
- Workshop
- Google AI Edge Gallery
- nanobot
- fast-agent
- Autohand Code CLI

(See agentskills.io for current list — adopters are growing.)

## Subpages of note (sitemap)

- /specification — full format spec
- /skill-creation/quickstart
- /skill-creation/best-practices
- /skill-creation/optimizing-descriptions
- /skill-creation/evaluating-skills
- /skill-creation/using-scripts
- /client-implementation/adding-skills-support
- /clients
