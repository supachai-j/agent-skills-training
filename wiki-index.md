# Index — Agent Skill Knowledge Base

A wiki for engineers and team leads upskilling on **Anthropic Agent Skills** and the surrounding ecosystem (Claude Code, Claude API, Claude.ai, MCP, subagents). Pages cite raw sources under `raw/`.

## Concepts

- [SKILL.md file format](wiki/concept:skill-md.md) — the YAML+markdown contract every skill obeys.
- [Progressive disclosure](wiki/concept:progressive-disclosure.md) — the 3-level loading model that makes skills scale.
- [`.agents/skills/` cross-client convention](wiki/concept:cross-client-convention.md) — where to put skills so every client sees them.
- [Skills vs MCP vs Subagents](wiki/concept:skills-vs-mcp-vs-subagents.md) — when to reach for which.
- [Skill security model](wiki/concept:security-considerations.md) — threats, mitigations, and trust boundaries.

## Features

- [Agent Skills](wiki/feature:agent-skills.md) — the umbrella feature.
- [Open standard (agentskills.io)](wiki/feature:open-standard.md) — the formal spec + ecosystem.
- [Skills in Claude Code](wiki/feature:claude-code-skills.md) — frontmatter extras, dynamic context, `context: fork`.
- [Skills via Claude API](wiki/feature:claude-api-skills.md) — beta headers, workspace sharing, no-network sandbox.
- [Skills in claude.ai](wiki/feature:claude-ai-skills.md) — ZIP uploads, per-user sharing.

## Patterns

- [Skill authoring best practices](wiki/pattern:authoring-best-practices.md) — concise, third-person, one-level-deep, gerund names, checklists.
- [Evaluation-driven Skill development](wiki/pattern:evaluation-driven-development.md) — write evals before docs.
- [Description optimization](wiki/pattern:description-optimization.md) — trigger-rate eval, train/validation split, 5-iteration loop.
- [Implementing Skills in a client agent](wiki/pattern:client-implementation.md) — the 5-step lifecycle for client builders.

## Skills (concrete examples)

- [Worked Skill examples](wiki/skill:examples.md) — `summarize-changes`, `deploy`, `codebase-visualizer`, `pdf-processing`.

## Tools

- [`skills-ref` reference SDK + validator](wiki/tool:skills-ref.md) — `skills-ref validate ./my-skill`.

## Decisions

_(populated as research expands)_

## Explorations / Crystals

_(populated after lint/crystallize)_

## Training portal

- [Portal home](index.html) — bilingual landing page with cards to course, slides, wiki
- [Self-paced course (EN)](course-en.html) — 12-module long-form
- [Self-paced course (TH)](course-th.html) — 12-module long-form

## Slides

- [English deck](slides/training-en.html)
- [Thai deck](slides/training-th.html)
