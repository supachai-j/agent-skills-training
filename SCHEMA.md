# SCHEMA — Agent Skill Knowledge Base (agentskill-101)

> Constitution of this wiki. The LLM reads it at the start of every Ingest / Query / Lint / Crystallize operation. If this document and SKILL.md disagree, this document wins.

## 1. Domain

This wiki is a **technical training & reference base for Agent Skills** — primarily Anthropic's *Agent Skills* (the `SKILL.md` + supporting files convention used by Claude Code, Claude.ai, and the Agent SDK), and adjacent ideas (slash commands, subagents, MCP, hooks, plugins). It is for engineers and team leads at Thai/SEA software organisations who want to upskill their teams beyond "vibe coding" into deliberate, composable agent skills. It should answer: *what is a Skill, how is it loaded, when do I use Skills vs MCP vs subagents, how do I author one safely, and how do I roll them out across a team*.

## 2. Entity catalogue

| type | id pattern | gets its own wiki page? | notes |
|---|---|---|---|
| `concept` | `concept:<kebab>` | yes | core ideas: skill, progressive-disclosure, frontmatter, etc. |
| `feature` | `feature:<kebab>` | yes | specific Claude/Anthropic features (skills, mcp, hooks, slash-commands, subagents, plugins) |
| `pattern` | `pattern:<kebab>` | yes | reusable authoring patterns (composable-skills, lint-flow, schema-driven) |
| `skill` | `skill:<name>` | yes | concrete example skills (pdf, docx, llm-wiki, etc.) |
| `tool` | `tool:<name>` | yes | tooling (Claude Code, Agent SDK, claude.ai, Cursor, etc.) |
| `decision` | `decision:<date>-<slug>` | yes | ADR-like records about how this training was scoped |
| `person` | `person:<handle>` | only if recurring | minimal PII; avoid unless needed |
| `source` | `source:<kebab>` | no — referenced from raw/ only | upstream URLs and authoritative docs |

## 3. Relation catalogue

- `uses` — A consumes B at runtime (e.g. skill uses tool)
- `depends-on` — A cannot function without B
- `composes` — A is built from / orchestrates B (skills compose with subagents)
- `alternative-to` — A and B solve overlapping problems (skill alternative-to slash-command)
- `extends` — A is a specialisation/extension of B
- `caused` — change/decision caused another
- `supersedes` — new claim/decision replaces an older one (old stays, marked stale)
- `contradicts` — flagged for Lint to resolve
- `mentions` — weak link, used when nothing stronger fits
- `cites` — A draws evidence from source B

## 4. Page rules

- One concept per page. If a page grows two clearly separable subjects, split it.
- Frontmatter is mandatory. See `wiki/_TEMPLATE.md`.
- Every claim has an inline source marker `[src: raw/...]`. Multiple sources → multiple markers.
- Wikilinks use entity IDs: `[[feature:agent-skills]]`, not `[[Agent Skills]]`.
- Status: `active` (default), `stale`, `faded`, `orphan`.

## 5. Ingest rules

- Raw source → `raw/YYYY-MM-DD-<slug>.md` untouched (after secret filter).
- Entity extraction runs against §2. Unknown types parked as `concept:` with TODO.
- Page is created when entity is "yes" in the catalogue *and* ≥1 non-trivial claim exists.
- Existing page updates: reinforce matching claims (bump confidence), append new ones. `updated_log` appends a dated line.

## 6. Confidence and decay

- First observation: `confidence: 0.5`
- Reinforcement (independent source): `conf ← 1 - (1 - conf) * 0.6`
- Contradiction: open supersession candidate, do not lower directly.
- Decay half-life:
  - `decision`: 365 days
  - `concept`, `pattern`, `feature`, `skill`, `tool`: 180 days
  - `person`: 90 days
  - `source`: not applicable (raw is immutable)

Claims with `conf < 0.2` and untouched ≥ 2× half-life → `status: faded`.

## 7. Privacy and secrets

Never written to wiki/ or graph/, redacted in raw/ on detection:
- API keys, tokens, signed URLs
- Passwords, private keys, certificates
- PII beyond `person:` name
- Anything the source marks confidential

Replacement token: `<REDACTED:apikey|token|pii|secret|other>`.

## 8. Lint policy

- Lint when ≥10 new sources since last lint, or on user request.
- Orphans with `conf > 0.5` → link from most relevant parent.
- Contradictions → resolve by (most recent authoritative source) > (most sources) > (highest prior confidence). Human confirms.
- Emit `raw/lint-YYYY-MM-DD.md` audit artifact.

## 9. Private vs shared

This wiki is **shared by default** — intended to be exported as training material. No `wiki/private/` planned. If added, those pages never appear in `index.md` or in slides.

## 10. Co-evolution

When the LLM hits a case this schema doesn't cover:
1. Do the right thing now.
2. Append note to `raw/schema-todo.md` with date, example, proposed amendment.
3. Next Lint surfaces `schema-todo.md` for human promotion.

## 11. Training-deck rules (project-specific)

This wiki feeds two HTML training decks (English + Thai) under `slides/`. Ingest rule: when a page is updated with a new "deck-worthy" claim, mark the claim with `tag: deck` so Crystallize can find it.
