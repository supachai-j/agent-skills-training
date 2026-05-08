# Agent Skills 101 — Training Materials

A self-paced engineering training on the **[Agent Skills](https://agentskills.io) open standard** — what they are, how they load, and how to author, test, secure, and roll them out across a team. Bilingual (English + Thai).

🌐 **Live site:** [supachai-j.github.io/agent-skills-training](https://supachai-j.github.io/agent-skills-training/)

## What's inside

| Path | What it is |
|---|---|
| [`wiki-root/web/index.html`](wiki-root/web/index.html) | Bilingual portal landing page |
| [`wiki-root/web/course-en.html`](wiki-root/web/course-en.html) | 12-module self-paced course (English, ~45 min read) |
| [`wiki-root/web/course-th.html`](wiki-root/web/course-th.html) | 12-module self-paced course (ภาษาไทย) |
| [`wiki-root/slides/training-en.html`](wiki-root/slides/training-en.html) | reveal.js deck for instructor-led sessions (EN) |
| [`wiki-root/slides/training-th.html`](wiki-root/slides/training-th.html) | reveal.js deck (TH) |
| [`wiki-root/wiki/`](wiki-root/wiki/) | 17 cited wiki pages — source of truth for all training content |
| [`wiki-root/raw/`](wiki-root/raw/) | Captured primary sources (Anthropic docs, agentskills.io) |
| [`wiki-root/graph/`](wiki-root/graph/) | Knowledge graph (entities + edges, JSONL) |
| [`wiki-root/SCHEMA.md`](wiki-root/SCHEMA.md) | The wiki's domain schema (fields, relations, lint rules) |

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

Open `wiki-root/web/index.html` in any browser. No build step. External dependencies are loaded from CDNs (Google Fonts, reveal.js).

## License

Training content is original and covered by the same Apache 2.0 / CC-BY-4.0 split that the [Agent Skills standard](https://github.com/agentskills/agentskills) uses — code samples Apache 2.0, prose CC-BY-4.0.

Built 2026-05-08.
