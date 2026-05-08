---
source_type: web
source_url: https://agentskills.io/client-implementation/adding-skills-support
ingested_at: 2026-05-08
title: How to add skills support to your agent
---

# Implementing Skills in a client agent

The 5-step lifecycle every conformant skills client follows.

## 1. Discover skills

### Where to scan

Most local agents scan two scopes:
- **Project-level** (relative to working directory)
- **User-level** (relative to home directory)

Optional: organisation-wide (managed), bundled built-ins.

| Scope | Path | Purpose |
|---|---|---|
| Project | `<project>/.<your-client>/skills/` | client-native |
| Project | `<project>/.agents/skills/` | **cross-client** |
| User | `~/.<your-client>/skills/` | client-native |
| User | `~/.agents/skills/` | **cross-client** |

> The `.agents/skills/` paths have emerged as a widely-adopted convention for cross-client skill sharing.

Many clients also pragmatically scan `.claude/skills/` because so many existing skills live there. Other extras: ancestor directories up to the git root, XDG config dirs, user-configured paths.

### What to scan for

Subdirectories containing a file named exactly `SKILL.md`. Skip `.git/`, `node_modules/`, build dirs. Honour `.gitignore`. Bound depth (4-6) and total dirs (~2,000).

### Name collisions

Universal convention: **project-level overrides user-level**. Within the same scope, pick first-found or last-found and be consistent. Always log a warning so the user knows.

### Trust check (project skills)

> Project-level skills come from the repository being worked on, which may be untrusted.

Gate project-skill loading on a workspace-trust check.

### Cloud / sandboxed agents

- Project skills travel with the cloned repo.
- User/org skills must be provisioned externally (config repo, upload).
- Built-in skills can be packaged with the agent.

## 2. Parse SKILL.md

YAML frontmatter between `---` delimiters; markdown body after.

### Lenient validation rules (recommended)

- Name doesn't match parent dir → warn, load anyway.
- Name >64 chars → warn, load anyway.
- Description missing/empty → **skip**, log error (description is essential).
- YAML completely unparseable → skip, log error.

### YAML quirk

Skills authored for other clients may have technically-invalid YAML — most often unquoted colons:

```yaml
description: Use this skill when: the user asks about PDFs   # invalid
```

Recommended fallback: try wrapping such values in quotes / converting to YAML block scalars before retrying.

### Minimum stored fields

| Field | Source |
|---|---|
| `name` | frontmatter |
| `description` | frontmatter |
| `location` | absolute path to SKILL.md |

Body can be stored at discovery (faster activation) or read on demand (lower memory + picks up edits).

## 3. Disclose to the model (Tier 1 — catalog)

Format example:

```xml
<available_skills>
  <skill>
    <name>pdf-processing</name>
    <description>Extract PDF text, fill forms, merge files. Use when handling PDFs.</description>
    <location>/home/user/.agents/skills/pdf-processing/SKILL.md</location>
  </skill>
  ...
</available_skills>
```

~50-100 tokens per skill. Two placements:
- **System prompt section** (simplest, broadest compatibility).
- **Tool description** of a dedicated `activate_skill` tool (cleaner pairing).

### Behavioural instruction snippets

File-read activation:
```
The following skills provide specialized instructions for specific tasks.
When a task matches a skill's description, use your file-read tool to load
the SKILL.md at the listed location before proceeding.
```

Dedicated tool activation:
```
... call the activate_skill tool with the skill's name to load its full
instructions.
```

### Filtering

Hide disabled / model-locked skills entirely (e.g. `disable-model-invocation`). Don't list them and block at activation — wastes turns. If no skills available, omit the block entirely.

## 4. Activate (Tier 2 — instructions)

Two implementation patterns:

- **File-read activation** — model uses its existing read tool on `SKILL.md`. Simplest.
- **Dedicated tool activation** — `activate_skill(name)` returns content. Required when model can't read files; useful even when it can.

Tool advantages:
- Strip frontmatter or keep it (most existing tools strip after extracting `name`+`description`).
- Wrap in structured tags (helps context management).
- List bundled resources without eagerly reading them.
- Enforce permissions, prompt for consent.
- Track for analytics.

Constrain `name` parameter to the discovered set (enum) to prevent hallucinated skill names.

### Structured wrapping

```xml
<skill_content name="pdf-processing">
# PDF Processing
...body...

Skill directory: /home/user/.agents/skills/pdf-processing
Relative paths in this skill are relative to the skill directory.

<skill_resources>
  <file>scripts/extract.py</file>
  <file>scripts/merge.py</file>
  <file>references/pdf-spec-summary.md</file>
</skill_resources>
</skill_content>
```

Cap large listings.

### User-explicit activation

Slash command (`/skill-name`) or mention syntax (`$skill-name`). Harness intercepts and injects content directly — model receives instructions without taking action.

### Permission allowlist

Allowlist the skill directory so reading bundled resources doesn't pop a permission prompt for every file.

## 5. Manage skill context over time

- **Protect skill content from compaction** — losing it silently degrades behaviour.
- **Deduplicate activations** — skip re-injection if already in context.
- **Subagent delegation (advanced)** — run the skill in a separate subagent, return summary to main conversation.

## Specification reference

The above is the canonical implementation pattern of agentskills.io's open standard.

## Reference SDK

`skills-ref` — validator + parser at <https://github.com/agentskills/agentskills/tree/main/skills-ref>.
