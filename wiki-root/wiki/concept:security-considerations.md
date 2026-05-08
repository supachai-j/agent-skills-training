---
id: concept:security-considerations
type: concept
title: Skill security model
status: active
confidence: 0.85
sources:
  - raw/2026-05-08-anthropic-engineering-skills.md
  - raw/2026-05-08-platform-docs-overview.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created
tiers: semantic
half_life_days: 180
tags: [deck]
---

# Skill security model

## Summary

Skills are powerful precisely because they let Claude run new instructions and code; that same power makes them dangerous if obtained from an untrusted source. **Treat installing a Skill like installing software.**

## Threat model

- Malicious instructions can redirect tool use away from the stated purpose.
- Bundled scripts can exfiltrate data or attack the host.
- External-URL fetches inside a skill can be tampered with after installation.
- A skill with broad `allowed-tools` quietly raises the trust boundary.

## Mitigations

- Install only from trusted sources (Anthropic-published or org-internal). `[src: raw/2026-05-08-anthropic-engineering-skills.md, raw/2026-05-08-platform-docs-overview.md] {conf: 0.95}`
- Review **every** bundled file: SKILL.md, references, scripts, assets. `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.9}`
- Be suspicious of skills that fetch external content at runtime. `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.9}`
- In Claude Code: project skills' `allowed-tools` only takes effect after workspace trust is granted. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.9}`
- Use `disable-model-invocation: true` for side-effect actions (`/deploy`, `/send-slack`) to keep the trigger human. `[src: raw/2026-05-08-claude-code-skills.md] {conf: 0.9}`

## Claims

- Skills run in a code-execution VM with filesystem + bash, so a compromised skill has the same access as the agent. `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.9}`
- API runtime has no network — partial mitigation against exfiltration. `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.9}`
- claude.ai's network access is admin-policy-governed. `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.85}`
- Skills are **not** ZDR-eligible today. `[src: raw/2026-05-08-platform-docs-overview.md] {conf: 0.9}`

## Relationships

- depends-on → [[feature:agent-skills]] `{conf: 0.9}`
- composes → [[pattern:authoring-best-practices]] `{conf: 0.7}`

## Changelog

- 2026-05-08 — created.
