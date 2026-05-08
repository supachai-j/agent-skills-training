---
source_type: web
source_url: https://agentskills.io/specification
ingested_at: 2026-05-08
title: Agent Skills — Specification (agentskills.io)
---

# Agent Skills Specification

The authoritative open-standard format spec.

## Directory structure

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...
```

## Frontmatter fields

| Field | Required | Constraints |
|---|---|---|
| `name` | **Yes** | ≤64 chars · lowercase letters/digits/hyphens · must not start/end with `-` · no `--` (consecutive) · **must match parent directory name** |
| `description` | **Yes** | ≤1024 chars · non-empty · what + when |
| `license` | No | License name or reference to bundled license file |
| `compatibility` | No | ≤500 chars · environment requirements (intended product, system pkgs, network needs) |
| `metadata` | No | Arbitrary key→value map for client-defined fields |
| `allowed-tools` | No | Space-separated string of pre-approved tools (**Experimental**) |

### Minimal SKILL.md

```markdown
---
name: skill-name
description: A description of what this skill does and when to use it.
---
```

### Full example

```markdown
---
name: pdf-processing
description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
license: Apache-2.0
metadata:
  author: example-org
  version: "1.0"
---
```

## `name` rules (verbatim)

- Must be 1-64 characters
- May only contain unicode lowercase alphanumeric (`a-z`) and hyphens (`-`)
- Must not start or end with a hyphen
- Must not contain consecutive hyphens
- **Must match the parent directory name**

Valid: `pdf-processing`, `data-analysis`, `code-review`.
Invalid: `PDF-Processing`, `-pdf`, `pdf--processing`.

## `description` rules

- 1-1024 characters
- Should describe **what** + **when**
- Should include keywords agents can match against tasks

Good: "Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction."

Poor: "Helps with PDFs."

## `compatibility` examples

- `Designed for Claude Code (or similar products)`
- `Requires git, docker, jq, and access to the internet`
- `Requires Python 3.14+ and uv`

> Most skills do not need the `compatibility` field.

## `metadata` example

```yaml
metadata:
  author: example-org
  version: "1.0"
```

## `allowed-tools` example (experimental)

```yaml
allowed-tools: Bash(git:*) Bash(jq:*) Read
```

## Optional directories — semantics

- **`scripts/`** — executable code agents can run; Python, Bash, JavaScript common.
- **`references/`** — additional docs read on demand. Examples: `REFERENCE.md`, `FORMS.md`, `finance.md`, `legal.md`.
- **`assets/`** — static resources (templates, images, lookup tables, schemas).

## Progressive disclosure budgets

| Tier | Budget |
|---|---|
| Metadata | ~100 tokens / skill |
| Instructions (SKILL.md body) | < 5,000 tokens recommended |
| Resources (scripts/references/assets) | as needed |

> Keep your main `SKILL.md` under 500 lines.

## File reference rule

Use **relative paths** from the skill root. Keep references **one level deep** from `SKILL.md`. Avoid deeply nested chains.

## Validator

Reference library: `skills-ref` at <https://github.com/agentskills/agentskills/tree/main/skills-ref>

```bash
skills-ref validate ./my-skill
```

Checks frontmatter validity and naming conventions.
