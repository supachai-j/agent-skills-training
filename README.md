# Agent Skills 101 — Training Materials

A self-paced engineering training on the **[Agent Skills](https://agentskills.io) open standard** — what they are, how they load, and how to author, test, secure, and roll them out across a team. Bilingual (English + Thai).

🌐 **Live site:** [supachai-j.github.io/agent-skills-training](https://supachai-j.github.io/agent-skills-training/)

## What's inside

| Path | What it is |
|---|---|
| [`index.html`](index.html) | Bilingual portal landing page |
| [`course-en.html`](course-en.html) | 12-module self-paced course (English, ~45 min read) |
| [`course-th.html`](course-th.html) | 12-module self-paced course (ภาษาไทย) |
| [`slides/training-en.html`](slides/training-en.html) | reveal.js deck for instructor-led sessions (EN) |
| [`slides/training-th.html`](slides/training-th.html) | reveal.js deck (TH) |
| [`wiki/`](wiki/) | 17 cited wiki pages — source of truth for all training content |
| [`raw/`](raw/) | Captured primary sources (Anthropic docs, agentskills.io) |
| [`graph/`](graph/) | Knowledge graph (entities + edges, JSONL) |
| [`SCHEMA.md`](SCHEMA.md) | The wiki's domain schema (fields, relations, lint rules) |
| [`wiki-index.md`](wiki-index.md) | Wiki catalogue with links to every page |

## Topics covered

- The `SKILL.md` contract — frontmatter, validation, Claude Code extras
- **Progressive disclosure** — three-level loading model
- **Open standard** ([agentskills.io](https://agentskills.io)) and the cross-client `.agents/skills/` convention (~38 adopters as of May 2026)
- Skills vs MCP vs Subagents — decision framework + composition
- Authoring best practices and anti-patterns
- **Description optimization** — train/validation eval methodology
- Implementing a Skills client (5-step lifecycle)
- Security model + team rollout playbook

## Running locally

Open `index.html` in any browser. No build step. External dependencies are loaded from CDNs (Google Fonts, reveal.js).

## License

Training content is original and covered by the same Apache 2.0 / CC-BY-4.0 split that the [Agent Skills standard](https://github.com/agentskills/agentskills) uses — code samples Apache 2.0, prose CC-BY-4.0.

Built 2026-05-08.
