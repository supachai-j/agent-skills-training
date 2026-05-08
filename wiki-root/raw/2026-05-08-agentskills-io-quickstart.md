---
source_type: web
source_url: https://agentskills.io/skill-creation/quickstart
ingested_at: 2026-05-08
title: Agent Skills Quickstart — VS Code roll-dice example
---

# Quickstart — `roll-dice` skill

Demonstrates the cross-client portability of the open standard. Same SKILL.md works in VS Code (Copilot), Claude Code, OpenAI Codex, and any compliant client.

## Default location for VS Code

`.agents/skills/roll-dice/SKILL.md` — the `.agents/skills/` convention is what cross-client implementations scan.

## SKILL.md (verbatim)

````markdown
---
name: roll-dice
description: Roll dice using a random number generator. Use when asked to roll a die (d6, d20, etc.), roll dice, or generate a random dice roll.
---

To roll a die, use the following command that generates a random number from 1
to the given number of sides:

```bash
echo $((RANDOM % <sides> + 1))
```

```powershell
Get-Random -Minimum 1 -Maximum (<sides> + 1)
```

Replace `<sides>` with the number of sides on the die (e.g., 6 for a standard
die, 20 for a d20).
````

## What happens behind the scenes

1. **Discovery** — agent scans default skill directories at session start, reads only `name` + `description`.
2. **Activation** — when user asks "Roll a d20", agent matches and loads the full SKILL.md.
3. **Execution** — agent runs the bash command, substituting sides.

## Notes

- Tool-use reliability varies by model — small/cheap models may answer without invoking the skill.
- Type `/skills` in Copilot Chat to confirm the skill appears.
