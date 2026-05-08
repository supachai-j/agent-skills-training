---
source_type: web
source_url: https://claude.com/blog/skills-explained
ingested_at: 2026-05-08
title: Skills vs Prompts vs Projects vs MCP vs Subagents
---

# Comparison: Skills vs Prompts vs Projects vs Subagents vs MCP

| Feature | Skills | Prompts | Projects | Subagents | MCP |
|---|---|---|---|---|---|
| Purpose | Procedural knowledge | Per-turn instructions | Background knowledge | Task delegation | External tool connectivity |
| Persistence | Across conversations | One conversation | Within project | Across sessions | Continuous connection |
| Contains | Instructions + code + assets | Natural language | Documents + context | Full agent logic | Tool definitions |
| Loading | Dynamically, on demand | Each turn | Always in project | When invoked | Always available |
| Includes code | Yes | No | No | Yes | Yes |

## Decision framework

- Need access to external system → **MCP**.
- Need work done independently with own context/model → **Subagent**.
- Need Claude to know how to do something repeatably → **Skill**.

## Composition (most powerful pattern)

> A subagent can call a skill that uses MCP.

Example: a code-review subagent uses Skills for language-specific best practices, calls MCP for repo access, returns to main agent.

## Practical example — research agent

1. **Project** — industry reports + competitor data.
2. **MCP** — Google Drive + GitHub.
3. **Skills** — analytical frameworks.
4. **Subagents** — specialised tasks (market vs technical).
5. **Prompts** — conversational refinement.

Result: layered competitive analysis.
