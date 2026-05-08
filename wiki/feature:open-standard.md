---
id: feature:open-standard
type: feature
title: Agent Skills open standard (agentskills.io)
status: active
confidence: 0.95
sources:
  - raw/2026-05-08-agentskills-io-home.md
  - raw/2026-05-08-agentskills-io-specification.md
  - raw/2026-05-08-agentskills-io-adding-skills-support.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created from agentskills.io
tiers: semantic
half_life_days: 180
tags: [deck, core]
---

# Agent Skills open standard

## Summary

`agentskills.io` is the home of the **open standard** for the SKILL.md format. The spec was originally developed by Anthropic, released as an open standard, and has been adopted by a wide ecosystem of agent products from many vendors. The standard governs only the **format** — directory layout, frontmatter fields, validation rules, and progressive-disclosure semantics — leaving discovery and execution policy to each client.

## Authoritative scope

- Spec: <https://agentskills.io/specification>
- Reference SDK + validator (`skills-ref`): <https://github.com/agentskills/agentskills>
- Cross-client convention: skills live under `.agents/skills/<name>/SKILL.md` (project) or `~/.agents/skills/<name>/SKILL.md` (user).

## Frontmatter (canonical, per agentskills.io spec)

| Field | Required | Constraints |
|---|---|---|
| `name` | yes | ≤64 · lowercase + digits + hyphens · no leading/trailing `-` · no `--` · **must match parent directory name** |
| `description` | yes | ≤1024 chars · what + when |
| `license` | no | license name or filename |
| `compatibility` | no | ≤500 chars · runtime/env requirements |
| `metadata` | no | arbitrary string→string map |
| `allowed-tools` | no | space-separated, **experimental** |

`[src: raw/2026-05-08-agentskills-io-specification.md] {conf: 0.95}`

## Claims

- The spec is published under an open license and is owned by the community via <https://github.com/agentskills/agentskills>. `[src: raw/2026-05-08-agentskills-io-home.md] {conf: 0.9}`
- The skill folder must contain a file named **exactly** `SKILL.md`. `[src: raw/2026-05-08-agentskills-io-specification.md, raw/2026-05-08-agentskills-io-adding-skills-support.md] {conf: 0.95}`
- Canonical sibling directories: `scripts/`, `references/`, `assets/`. `[src: raw/2026-05-08-agentskills-io-specification.md] {conf: 0.95}`
- `name` **must match the parent directory name** — this is the spec, even though Anthropic's first-party docs are silent on it. `[src: raw/2026-05-08-agentskills-io-specification.md] {conf: 0.95}`
- `compatibility` is the standard place to record env requirements (e.g. `Requires Python 3.14+ and uv`). `[src: raw/2026-05-08-agentskills-io-specification.md] {conf: 0.9}`
- `allowed-tools` is **experimental** in the open spec; support varies by client. `[src: raw/2026-05-08-agentskills-io-specification.md] {conf: 0.9}`
- Validate skills with `skills-ref validate ./my-skill`. `[src: raw/2026-05-08-agentskills-io-specification.md] {conf: 0.9}`
- Adopters as of May 2026 include (non-exhaustive): Claude Code, Claude (claude.ai), GitHub Copilot, VS Code, OpenAI Codex, Cursor, Gemini CLI, OpenCode, OpenHands, Goose, Letta, Roo Code, Mistral Vibe, Mux, Junie, Amp, Firebender, Snowflake Cortex Code, Databricks Genie Code, Kiro, Spring AI, Laravel Boost, Factory, Ona, Workshop, Agentman, Trae, Piebald, Pi, Emdash, Qodo, VT Code, Command Code, Google AI Edge Gallery, nanobot, fast-agent, Autohand Code CLI. `[src: raw/2026-05-08-agentskills-io-home.md] {conf: 0.9}`

## Why this matters

The same `SKILL.md` you author for Claude Code can run unchanged in Copilot, Cursor, Codex, Gemini CLI, etc. — provided you stay within the standard's frontmatter and file-layout rules. That's the upside of an open spec: write once, reuse across the ecosystem.

## Relationships

- composes → [[feature:agent-skills]] `{conf: 0.95}` (spec is the formal definition of the format)
- depends-on → [[concept:skill-md]] `{conf: 0.95}`
- depends-on → [[concept:cross-client-convention]] `{conf: 0.9}`
- composes → [[tool:skills-ref]] `{conf: 0.9}`

## Open questions

- [ ] Long-term governance model — is there a formal RFC/SIG process beyond GitHub issues?
- [ ] Versioning — how does spec evolution interact with client adoption?

## Changelog

- 2026-05-08 — created from agentskills.io home, spec, and implementation guide.
