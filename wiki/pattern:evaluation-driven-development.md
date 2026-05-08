---
id: pattern:evaluation-driven-development
type: pattern
title: Evaluation-driven Skill development
status: active
confidence: 0.85
sources:
  - raw/2026-05-08-best-practices.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created
tiers: procedural
half_life_days: 365
tags: [deck]
---

# Evaluation-driven Skill development

## Summary

Build evaluations *before* writing extensive Skill content. Evaluations are the source of truth for whether a Skill actually solves a problem, not whether it documents one.

## Steps

1. **Identify gaps** — run Claude on representative tasks **without** the skill; record specific failures.
2. **Create 3 evaluation scenarios** that test those gaps.
3. **Establish baseline** — measure Claude's performance pre-skill.
4. **Write minimal SKILL.md** — only enough to address the gaps.
5. **Iterate** — re-run evaluations, compare against baseline, refine.

## Evaluation example (verbatim from docs)

```json
{
  "skills": ["pdf-processing"],
  "query": "Extract all text from this PDF file and save it to output.txt",
  "files": ["test-files/document.pdf"],
  "expected_behavior": [
    "Successfully reads the PDF file using an appropriate PDF processing library or command-line tool",
    "Extracts text content from all pages in the document without missing any pages",
    "Saves the extracted text to a file named output.txt in a clear, readable format"
  ]
}
```
`[src: raw/2026-05-08-best-practices.md] {conf: 0.95}`

## Claims

- Evaluations come **before** documentation. `[src: raw/2026-05-08-best-practices.md] {conf: 0.95}`
- There is no built-in evaluation runner; users wire their own. `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`
- Pair Claude-A (author) with Claude-B (user) for iterative refinement. `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`

## Relationships

- composes → [[pattern:authoring-best-practices]] `{conf: 0.9}`

## Changelog

- 2026-05-08 — created.
