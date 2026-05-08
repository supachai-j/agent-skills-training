---
id: pattern:client-implementation
type: pattern
title: Implementing Skills in a client agent
status: active
confidence: 0.9
sources:
  - raw/2026-05-08-agentskills-io-adding-skills-support.md
created: 2026-05-08
updated: 2026-05-08
updated_log:
  - 2026-05-08: created
tiers: procedural
half_life_days: 365
tags: [deck]
---

# Implementing Skills in a client agent

## Summary

If you're building an agent and want to be a conformant Skills client, agentskills.io publishes the complete lifecycle — five steps from discovery through context management. This page captures the canonical pattern.

## Five-step lifecycle

### 1. Discover

Scan project + user (and optionally org/built-in) scopes for subdirectories containing exactly `SKILL.md`. Also scan the cross-client convention `.agents/skills/`. Many clients pragmatically include `.claude/skills/` for compatibility.

Bound the search (depth ≤6, ~2k dirs max). Skip `.git/`, `node_modules/`. Honour `.gitignore`.

Apply a **trust check** before loading project skills — they come from the repo, which may be untrusted. `[src: raw/2026-05-08-agentskills-io-adding-skills-support.md] {conf: 0.95}`

### 2. Parse

Lenient validation: warn on cosmetic violations (name mismatch, >64 chars), only **skip** on essentials (missing description, unparseable YAML). Be tolerant of unquoted-colon YAML by quoting and retrying. `[src: raw/2026-05-08-agentskills-io-adding-skills-support.md] {conf: 0.9}`

Store at minimum: `name`, `description`, `location` (absolute path).

### 3. Disclose (Tier 1 — catalog)

Inject a structured catalog (XML/JSON/list) into the system prompt or a tool description. ~50–100 tokens per skill.

```xml
<available_skills>
  <skill>
    <name>pdf-processing</name>
    <description>...</description>
    <location>/.../SKILL.md</location>
  </skill>
</available_skills>
```

Add a behavioural instruction telling the model how to load a skill (file-read tool **or** `activate_skill` tool). Hide disabled / model-locked skills entirely. If empty, omit the block.

### 4. Activate (Tier 2 — instructions)

Two patterns:
- **File-read activation** — model uses its existing read tool on `SKILL.md`. Simplest.
- **Dedicated `activate_skill(name)` tool** — required when model can't read files; useful even when it can.

Constrain `name` to the discovered enum so the model can't hallucinate a skill name.

Wrap returned content in identifying tags so context-management can find it later:

```xml
<skill_content name="pdf-processing">
... body ...
Skill directory: /.../pdf-processing
<skill_resources>
  <file>scripts/extract.py</file>
  <file>references/pdf-spec-summary.md</file>
</skill_resources>
</skill_content>
```

Allowlist the skill directory in your permission system so bundled files don't trigger per-file consent prompts.

### 5. Manage skill context over time

- **Protect skill content from compaction.** Losing it silently degrades behaviour.
- **Deduplicate activations** — skip re-injection if already in context.
- **Subagent delegation** — advanced; run skill in a separate session and return a summary.

## Claims

- "Universal convention: project-level skills override user-level." `[src: raw/2026-05-08-agentskills-io-adding-skills-support.md] {conf: 0.95}`
- Catalog adds ~50–100 tokens per skill. `[src: raw/2026-05-08-agentskills-io-adding-skills-support.md] {conf: 0.9}`
- Most existing dedicated activation tools strip frontmatter after extracting `name`/`description`. `[src: raw/2026-05-08-agentskills-io-adding-skills-support.md] {conf: 0.9}`
- A trust check on project skills is the recommended way to keep untrusted repos from injecting instructions. `[src: raw/2026-05-08-agentskills-io-adding-skills-support.md] {conf: 0.95}`

## Relationships

- composes → [[feature:open-standard]] `{conf: 0.95}`
- depends-on → [[concept:cross-client-convention]] `{conf: 0.9}`
- depends-on → [[concept:security-considerations]] `{conf: 0.85}`

## Open questions

- [ ] Are there agreed protocol-level error codes for skill-load failures across clients?

## Changelog

- 2026-05-08 — created from agentskills.io implementation guide.
