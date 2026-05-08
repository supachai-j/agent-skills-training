---
source_type: web
source_url: https://agentskills.io/skill-creation/optimizing-descriptions
ingested_at: 2026-05-08
title: Optimizing skill descriptions
---

# Optimizing skill descriptions

The description carries the **entire burden of triggering**. A poor description means the skill never activates — or activates when it shouldn't.

## Triggering nuance

> Agents typically only consult skills for tasks that require knowledge or capabilities beyond what they can handle alone. A simple, one-step request like "read this PDF" may not trigger a PDF skill even if the description matches perfectly.

Skills win where the task involves **specialized knowledge** — unfamiliar API, domain-specific workflow, uncommon format.

## Writing principles

- **Imperative phrasing.** "Use this skill when…" beats "This skill does…".
- **User intent over implementation.** Match what the user asked for, not internals.
- **Err on the side of being pushy.** List adjacent contexts: "even if they don't explicitly mention 'CSV' or 'analysis.'"
- **Concise.** Few sentences to a short paragraph; hard cap 1024 chars.

## Eval set design

Aim for ~20 queries: 8-10 should-trigger, 8-10 should-not.

```json
[
  { "query": "I've got a spreadsheet in ~/data/q4_results.xlsx with revenue in col C and expenses in col D — can you add a profit margin column and highlight anything under 10%?", "should_trigger": true },
  { "query": "whats the quickest way to convert this json file to yaml", "should_trigger": false }
]
```

### Vary should-trigger queries along axes

- Phrasing (formal / casual / typos)
- Explicitness (names domain vs hides it)
- Detail (terse vs context-heavy)
- Complexity (single-step vs multi-step)

The most useful positives are ones where the connection isn't obvious — that's where description wording matters.

### Strong negatives are **near-misses**

For a CSV-analysis skill:
- Weak negative: "Write a fibonacci function" (no overlap, tests nothing).
- Strong negative: "I need to update the formulas in my Excel budget spreadsheet" (overlaps but actually needs Excel editing, not CSV analysis).
- Strong negative: "write a python script that reads a csv and uploads each row to our postgres database" (CSV present, but task is ETL).

## Trigger rate measurement

Run each query **3 times** (model is non-deterministic). Pass rule:
- should_trigger queries pass if trigger_rate > 0.5
- should_not_trigger pass if trigger_rate < 0.5

## Train / validation split

- Train ~60%: drives revisions.
- Validation ~40%: tells you whether changes generalise.
- Both must contain proportional positives + negatives.
- Shuffle once, then keep the split fixed.

## Optimization loop

1. Evaluate on train and validation.
2. Identify train failures only.
3. Revise:
   - Too narrow → broaden scope, add adjacent contexts.
   - Too broad → add specificity, mark out-of-scope.
   - Avoid copying keywords from failed queries (overfit) — find the underlying category.
   - Stay under 1024 chars.
4. Repeat until train passes or improvement plateaus.
5. Select **best validation pass rate** — *not* the latest iteration.

> Five iterations is usually enough.

## skill-creator skill

> The `skill-creator` Skill automates this loop end-to-end: it splits the eval set, evaluates trigger rates in parallel, proposes description improvements using Claude, and generates a live HTML report you can watch as it runs.

Repo: <https://github.com/anthropics/skills/tree/main/skills/skill-creator>

## Before / after example

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

The "after" is **specific** about what the skill does and **broad** about when it applies.

## Bash eval harness (Claude Code)

```bash
#!/bin/bash
QUERIES_FILE="${1:?Usage: $0 <queries.json>}"
SKILL_NAME="my-skill"
RUNS=3

check_triggered() {
  local query="$1"
  claude -p "$query" --output-format json 2>/dev/null \
    | jq -e --arg skill "$SKILL_NAME" \
      'any(.messages[].content[]; .type == "tool_use" and .name == "Skill" and .input.skill == $skill)' \
      > /dev/null 2>&1
}

count=$(jq length "$QUERIES_FILE")
for i in $(seq 0 $((count - 1))); do
  query=$(jq -r ".[$i].query" "$QUERIES_FILE")
  should_trigger=$(jq -r ".[$i].should_trigger" "$QUERIES_FILE")
  triggers=0
  for run in $(seq 1 $RUNS); do
    check_triggered "$query" && triggers=$((triggers + 1))
  done
  jq -n --arg query "$query" --argjson should_trigger "$should_trigger" \
    --argjson triggers "$triggers" --argjson runs "$RUNS" \
    '{query:$query, should_trigger:$should_trigger, triggers:$triggers, runs:$runs, trigger_rate:($triggers/$runs)}'
done | jq -s '.'
```
