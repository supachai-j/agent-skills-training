---
id: pattern:authoring-best-practices
type: pattern
title: Skill authoring best practices
status: active
confidence: 0.9
sources:
  - raw/2026-05-08-best-practices.md
  - raw/2026-05-08-anthropic-engineering-skills.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created
tiers: procedural
half_life_days: 365
tags: [deck, core]
---

# Skill authoring best practices

## Summary

A working set of authoring rules from Anthropic's official guidance. Treat the context window as a public good; assume Claude is already smart; calibrate "degrees of freedom" to task fragility; iterate empirically with both Claude-as-author and Claude-as-user.

## The five-step methodology

1. **Start with evaluation** — find capability gaps with representative tasks. `[src: raw/2026-05-08-anthropic-engineering-skills.md, raw/2026-05-08-best-practices.md] {conf: 0.95}`
2. **Structure for scale** — split SKILL.md when it grows; one level deep references. `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`
3. **Think from Claude's perspective** — name + description determine triggering. `[src: raw/2026-05-08-anthropic-engineering-skills.md] {conf: 0.9}`
4. **Iterate with Claude (Claude A / Claude B)** — Claude A drafts, Claude B uses, you observe and refine. `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`
5. **Code vs documentation** — be explicit whether Claude executes a script or reads it as reference. `[src: raw/2026-05-08-anthropic-engineering-skills.md] {conf: 0.9}`

## Claims

- "Concise is key" — every loaded SKILL.md token competes with conversation history. `[src: raw/2026-05-08-best-practices.md] {conf: 0.95}`
- Use **gerund form** for skill names (`processing-pdfs`, `analyzing-spreadsheets`). `[src: raw/2026-05-08-best-practices.md] {conf: 0.85}`
- Description **must** be third person; first/second person harms discovery. `[src: raw/2026-05-08-best-practices.md] {conf: 0.95}`
- Match degrees of freedom to task fragility: high-freedom for open work, low-freedom for fragile/sequential operations (e.g. DB migrations). `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`
- Test with all models the skill will run on (Haiku, Sonnet, Opus). `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`
- Keep file references **one level deep** — Claude may partial-read nested files. `[src: raw/2026-05-08-best-practices.md] {conf: 0.95}`
- Reference files >100 lines need a Contents block. `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`
- Use checklists for multi-step workflows; "validator → fix → repeat" pattern. `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`
- Avoid time-sensitive content; route deprecated material to a "legacy" section. `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`
- Use consistent terminology across the skill. `[src: raw/2026-05-08-best-practices.md] {conf: 0.85}`
- Anti-patterns: Windows-style paths, voodoo constants, "punt-to-Claude" error handling, presenting too many alternatives. `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`
- Plan-validate-execute pattern with intermediate JSON catches errors early on batch / destructive operations. `[src: raw/2026-05-08-best-practices.md] {conf: 0.9}`
- MCP tool references must be fully qualified: `ServerName:tool_name`. `[src: raw/2026-05-08-best-practices.md] {conf: 0.95}`

## Final checklist

**Core quality**
- [ ] Description specific + key terms, third person, what + when.
- [ ] SKILL.md body < 500 lines.
- [ ] Detail in separate files (one level deep).
- [ ] No time-sensitive content (or in legacy section).
- [ ] Consistent terminology.
- [ ] Concrete examples.
- [ ] Progressive disclosure used.
- [ ] Workflows have clear steps.

**Code & scripts**
- [ ] Scripts solve, not punt.
- [ ] Explicit error handling.
- [ ] No voodoo constants.
- [ ] Required packages listed + verified available.
- [ ] No Windows paths.
- [ ] Validation steps for critical ops.
- [ ] Feedback loops for quality-critical work.

**Testing**
- [ ] ≥3 evaluations.
- [ ] Tested with Haiku, Sonnet, Opus.
- [ ] Tested in real-usage scenarios.
- [ ] Team feedback incorporated.

`[src: raw/2026-05-08-best-practices.md] {conf: 0.95}`

## Relationships

- depends-on → [[concept:skill-md]] `{conf: 0.9}`
- depends-on → [[concept:progressive-disclosure]] `{conf: 0.9}`
- depends-on → [[pattern:evaluation-driven-development]] `{conf: 0.85}`

## Changelog

- 2026-05-08 — created.
