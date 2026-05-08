---
source_type: web
source_url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
ingested_at: 2026-05-08
title: Skill authoring best practices
---

# Skill authoring best practices

## Core principles

- **Concise is key.** "The context window is a public good."
- **Default assumption:** Claude is already very smart — only add what Claude doesn't already have.
- **Set appropriate degrees of freedom**:
  - High freedom (text instructions) — multiple valid approaches.
  - Medium freedom (pseudocode / parameterised scripts).
  - Low freedom (specific scripts) — for fragile / sequential operations.
- **Test with all models you plan to use** (Haiku, Sonnet, Opus).

### Robot-on-a-path analogy

- Narrow bridge with cliffs → low freedom, exact instructions (e.g. DB migrations).
- Open field → high freedom, general direction (e.g. code reviews).

## Naming

Use **gerund form** when possible: `processing-pdfs`, `analyzing-spreadsheets`.
Avoid: `helper`, `utils`, `tools`, `documents`, `data`, `files`.
Reserved: `anthropic`, `claude`.

## Description

- Always third person. ("Processes Excel files…", **not** "I can help…")
- Include both **what** and **when**.
- Used by Claude to choose among potentially 100+ skills.
- Truncated at 1,536 chars (Claude Code combined description+when_to_use).

## Progressive disclosure patterns

- Keep SKILL.md body **under 500 lines**.
- Pattern 1 — high-level guide pointing to FORMS.md / REFERENCE.md / EXAMPLES.md.
- Pattern 2 — domain-specific organisation (e.g. `reference/finance.md`, `reference/sales.md`).
- Pattern 3 — conditional details: link advanced topics from main file.

## Avoid deeply nested references

> Keep references one level deep from SKILL.md.

Claude may `head -100` partial-read nested files; it won't transitively chase 3 levels.

## Long reference files: TOC

Files >100 lines need a Contents block at top so Claude can navigate.

## Workflows + checklists

For multi-step tasks, give Claude a checklist to copy and tick. Pattern: validator → fix → repeat.

## Content guidelines

- Avoid time-sensitive info; if needed, put under a "legacy / old patterns" section.
- Use consistent terminology.

## Anti-patterns

- Windows-style paths — use forward slashes always.
- Too many alternatives — give Claude one default.

## Scripts

- Solve, don't punt — handle errors in the script, don't let Claude figure them out.
- No "voodoo constants" — document every magic number.
- Pre-made utility scripts > Claude-generated code (more reliable, saves tokens).
- "Plan-validate-execute" pattern: produce intermediate JSON, validate it, then execute.

## MCP tool references

Always fully-qualify: `ServerName:tool_name`, e.g. `BigQuery:bigquery_schema`.

## Evaluation-driven development

> Create evaluations BEFORE writing extensive documentation.

1. Identify gaps (run Claude on real tasks without skill).
2. Create 3 evaluation scenarios.
3. Establish baseline.
4. Write minimal instructions.
5. Iterate.

## Claude A / Claude B authoring loop

- Claude A — helps you design the skill.
- Claude B — fresh instance using the skill on real tasks.
- Iterate by feeding Claude B's behaviour back to Claude A.

## Final checklist (verbatim)

Core quality:
- Description specific + key terms
- Description: what + when
- SKILL.md body < 500 lines
- Additional details in separate files
- No time-sensitive info (or in old patterns)
- Consistent terminology
- Concrete examples
- File references one level deep
- Progressive disclosure used
- Workflows have clear steps

Code & scripts:
- Scripts solve problems
- Explicit error handling
- No voodoo constants
- Required packages listed + verified
- Scripts documented
- No Windows paths
- Validation steps
- Feedback loops

Testing:
- ≥3 evaluations
- Tested with Haiku/Sonnet/Opus
- Real usage tested
- Team feedback incorporated
