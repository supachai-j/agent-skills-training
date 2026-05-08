---
id: pattern:description-optimization
type: pattern
title: Skill description optimization (trigger-rate evaluation)
status: active
confidence: 0.9
sources:
  - raw/2026-05-08-agentskills-io-optimizing-descriptions.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created
tiers: procedural
half_life_days: 365
tags: [deck, core]
---

# Skill description optimization

## Summary

The `description` field is the **only** thing that decides whether a skill activates. agentskills.io documents a structured optimization loop with a labeled query set, train/validation split, and 3-run trigger-rate measurement.

## Writing principles

- **Imperative phrasing** — "Use this skill when…" beats "This skill does…"
- **User intent over implementation** — match the user's words, not the internals
- **Pushy** — list adjacent contexts, e.g. "even if they don't explicitly mention 'CSV' or 'analysis.'"
- **Concise** — paragraph max; hard cap 1024 chars
- **Activation nuance** — agents skip skills for tasks they can already handle alone; lean on *specialised* knowledge cues

`[src: raw/2026-05-08-agentskills-io-optimizing-descriptions.md] {conf: 0.95}`

## Eval set

20 queries: 8-10 should-trigger, 8-10 should-not.

```json
[
  { "query": "I've got a spreadsheet in ~/data/q4_results.xlsx with revenue in col C and expenses in col D — can you add a profit margin column and highlight anything under 10%?", "should_trigger": true },
  { "query": "whats the quickest way to convert this json file to yaml", "should_trigger": false }
]
```

Vary should-trigger queries on **phrasing**, **explicitness**, **detail**, **complexity**.

Strong **negatives** are *near-misses* — same keywords, different task. Weak negatives ("write fibonacci") test nothing.

## Optimization loop

1. **Evaluate** on train (~60%) + validation (~40%) sets.
2. **Identify train failures** only.
3. **Revise**:
   - Too narrow → broaden scope.
   - Too broad → add specificity, mark out-of-scope.
   - Don't paste keywords from failed queries (overfit) — find the underlying category.
   - Stay ≤1024 chars.
4. **Repeat** ~5 iterations.
5. **Pick by best validation pass-rate**, not the latest. Earlier iterations sometimes generalise better.

## Trigger-rate measurement

- Run each query 3 times (model is non-deterministic).
- pass(should_trigger=true) ↔ trigger_rate > 0.5
- pass(should_trigger=false) ↔ trigger_rate < 0.5

Bash harness for Claude Code is captured in raw/.

## Before / after

```yaml
# Before
description: Process CSV files.

# After
description: >
  Analyze CSV and tabular data files — compute summary statistics,
  add derived columns, generate charts, and clean messy data. Use this
  skill when the user has a CSV, TSV, or Excel file and wants to
  explore, transform, or visualize the data, even if they don't
  explicitly mention "CSV" or "analysis."
```

The "after" is **specific** about *what* + **broad** about *when*.

## Tooling

`skill-creator` skill (Anthropic) automates the loop end-to-end with a live HTML report. Repo: <https://github.com/anthropics/skills/tree/main/skills/skill-creator>. `[src: raw/2026-05-08-agentskills-io-optimizing-descriptions.md] {conf: 0.9}`

## Relationships

- composes → [[pattern:authoring-best-practices]] `{conf: 0.9}`
- depends-on → [[pattern:evaluation-driven-development]] `{conf: 0.9}`
- composes → [[concept:skill-md]] `{conf: 0.85}`

## Changelog

- 2026-05-08 — created.
