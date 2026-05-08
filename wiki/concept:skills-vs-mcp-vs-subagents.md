---
id: concept:skills-vs-mcp-vs-subagents
type: concept
title: Skills vs MCP vs Subagents (and Prompts, Projects)
status: active
confidence: 0.9
sources:
  - raw/2026-05-08-skills-vs-mcp-vs-subagents.md
  - raw/2026-05-08-anthropic-engineering-skills.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created
tiers: semantic
half_life_days: 180
tags: [deck, core]
---

# Skills vs MCP vs Subagents (and Prompts, Projects)

## Summary

Most production agent setups use Skills, MCP, and Subagents *together*. The three answer different questions:

- **Skills** — *how* to do something repeatably.
- **MCP** — *access* to external systems, data, and tools.
- **Subagents** — *delegate* a task to a specialist with its own context and permissions.

Prompts are per-turn instructions; Projects are background knowledge bases. Both pair with Skills.

## Decision framework

```
Need Claude to know HOW to do X repeatably?  → Skill
Need Claude to ACCESS an external system?    → MCP
Need work done IN ISOLATION with own context? → Subagent
```

## Comparison table

| Feature | Skills | Prompts | Projects | Subagents | MCP |
|---|---|---|---|---|---|
| Purpose | Procedural know-how | Per-turn instructions | Background knowledge | Task delegation | Tool connectivity |
| Persistence | Across conversations | Single conversation | Within project | Across sessions | Continuous |
| Contains | Instructions + code + assets | Natural language | Documents + context | Full agent logic | Tool defs |
| Loading | Dynamic, on-demand | Each turn | Always in project | When invoked | Always available |
| Includes code | Yes | No | No | Yes | Yes |

## Claims

- "Skills teach Claude *how*; MCP enables Claude to *access*; Subagents do work *independently*." `[src: raw/2026-05-08-skills-vs-mcp-vs-subagents.md] {conf: 0.95}`
- The most powerful pattern: a subagent calls a skill that uses MCP. `[src: raw/2026-05-08-skills-vs-mcp-vs-subagents.md] {conf: 0.95}`
- Skills are dynamically loaded; Projects are always-loaded background context. `[src: raw/2026-05-08-skills-vs-mcp-vs-subagents.md] {conf: 0.9}`

## Relationships

- alternative-to → [[feature:agent-skills]] `{conf: 0.5}` (different surfaces of same problem)
- composes → [[feature:mcp]] `{conf: 0.6}`
- composes → [[concept:subagents]] `{conf: 0.7}`

## Open questions

- [ ] Cost / latency of nested compositions (subagent → skill → MCP) on large workflows.

## Changelog

- 2026-05-08 — created.
