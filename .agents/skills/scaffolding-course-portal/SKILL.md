---
name: scaffolding-course-portal
description: Scaffolds a bilingual (EN/TH) self-paced training course portal — wiki + slides + landing page + GitHub Pages deploy. Use when the user wants to start a new course, training, workshop, or self-paced learning material; mentions building a "training portal" or "course site"; or asks how to structure a new training repo. Even applies when the user describes the topic without naming the deliverable (e.g. "I want to teach my team about X").
license: Apache-2.0
compatibility: Requires git, gh (GitHub CLI), and curl. Designed for Claude Code; works in any agent that supports SKILL.md.
metadata:
  author: supachai-j
  version: "1.0"
  template_repo: https://github.com/supachai-j/course-portal-template
allowed-tools: Bash(git:*) Bash(gh:*) Bash(curl:*) Bash(mkdir:*) Read Write Edit Grep
---

# Scaffolding a course portal

This skill walks the user through a 12-phase pipeline to produce a complete bilingual training portal — wiki + course pages + slide decks + marketing landing — and deploy it to GitHub Pages. The pattern was distilled from `agent-skills-training` (the project that hosts this skill).

## When to use

Trigger when:
- User starts a new training, workshop, or course
- User wants to "build a course portal" or "training site"
- User describes a topic to teach but hasn't named the deliverable
- User wants a structured way to capture domain knowledge they'll be teaching

Do **not** trigger for:
- One-off blog posts or articles
- Non-pedagogical project scaffolding
- Adding content to an existing course (that's a wiki ingest, not a scaffold)

## Quick start (the happy path)

The fastest start is to use the [course-portal-template](https://github.com/supachai-j/course-portal-template) repo:

```bash
# Option A — Use GitHub's "Use this template" button (recommended)
# Visit https://github.com/supachai-j/course-portal-template
# Click "Use this template → Create a new repository"
# Then locally:
git clone https://github.com/<your-org>/<your-new-repo>
cd <your-new-repo>
./setup.sh

# Option B — Clone fresh (no template button)
git clone https://github.com/supachai-j/course-portal-template.git my-course
cd my-course
rm -rf .git
./setup.sh
```

`setup.sh` is interactive and replaces every `{{TOKEN}}` placeholder. After it runs, follow Phases 2-12 below.

## The 12 phases

Detailed walkthrough in [references/PIPELINE.md](references/PIPELINE.md).

| # | Phase | Time | Output |
|---|---|---|---|
| 1 | Scope | ~30 m | One-sentence outcome, audience, format |
| 2 | Research & capture | ~2-4 h | 3-5 primary sources in `raw/` |
| 3 | Wiki init | ~30 m | Customised `SCHEMA.md` |
| 4 | Ingest | ~2-3 h | 8-15 wiki pages with citations |
| 5 | Outline | ~1 h | 10-12 modules, each citing wiki |
| 6 | Course pages | ~3-5 h | `course-en.html` complete |
| 7 | Slide deck | ~2-3 h | `slides/training-en.html` complete |
| 8 | Bilingual mirror | ~3-4 h | `course-th.html` + `slides/training-th.html` |
| 9 | Landing tuning | ~1-2 h | `index.html` polished |
| 10 | Deploy | ~30 m | Live on GitHub Pages |
| 11 | Validate | ~1-2 h | Peer review + link checks |
| 12 | Promote | ~1 h | Hub + blog announcement |

**Total:** ~20-30 h bilingual · ~6-8 h EN-only fast path.

## Phase quality gates

Each phase has a "done when" criterion. Don't move on until met.

- **P1 done when:** `scope.md` committed with one-sentence outcome.
- **P2 done when:** ≥3 files in `raw/` with frontmatter, captured verbatim.
- **P3 done when:** `SCHEMA.md` customised for the domain.
- **P4 done when:** Every wiki claim has `[src: raw/...]` and confidence.
- **P5 done when:** Every module in outline maps to ≥1 wiki page.
- **P6 done when:** All anchors resolve, all wiki citations valid.
- **P7 done when:** No slide overflows the 1280×800 canvas.
- **P8 done when:** TH version mirrors EN structure exactly.
- **P9 done when:** Light + dark modes both pass eye-test.
- **P10 done when:** All entry-point URLs return HTTP 200.
- **P11 done when:** ≥3 rounds of feedback incorporated.
- **P12 done when:** Hub Featured/Courses card live, blog post drafted.

## Common anti-patterns

- **Skipping Phase 4** (writing course before ingesting sources) → claims drift from truth.
- **Slide overflow** — using reveal.js default 960×700. Use 1280×800 always.
- **Translating prematurely** — TH before EN is finalised wastes effort. Always EN-first, TH-mirror.
- **Hardcoded colours** — prevents dark/light theming. Always use CSS variables.
- **Forgetting `.nojekyll`** — Pages tries to Jekyll-process files with colons in names and chokes.

## Fast-path skips (if EN-only, solo author)

| Phase | Can skip? | Why |
|---|---|---|
| 1-5 | ❌ never | Scope/sources/outline are the foundation |
| 6 | ✅ trim to 6-8 modules | Cut security/implementation guide |
| 7 | ⚠️ optional | Skip if not running live sessions |
| 8 | ✅ skip | Add TH later |
| 9 | ⚠️ minimal | Hero + cards only |
| 10-11 | ❌ never | Deploy + validate are quality gates |
| 12 | ⚠️ optional | Promote later |

## Workspace layout produced

```
your-course/
├── index.html              # Landing
├── 404.html
├── course-en.html          # Self-paced EN
├── course-th.html          # Self-paced TH
├── wiki-index.md
├── SCHEMA.md
├── slides/
│   ├── training-en.html    # reveal.js EN
│   └── training-th.html    # reveal.js TH
├── wiki/                   # Cited knowledge pages
├── raw/                    # Primary sources, immutable
└── graph/                  # Entity + edge JSONL
```

## Detailed references

- [PIPELINE.md](references/PIPELINE.md) — full phase-by-phase walkthrough
- [Template repo](https://github.com/supachai-j/course-portal-template)
- [Live process doc](https://supachai-j.github.io/process.html)
- [Worked example](https://supachai-j.github.io/agent-skills-training/) — the original this pattern was extracted from

## Validate before sharing

Once your course is built, run:

```bash
# Spec validation (if you ship .agents/skills/ inside)
skills-ref validate ./

# HTTP smoke test
for path in "/" "/course-en.html" "/course-th.html" "/slides/training-en.html" "/slides/training-th.html"; do
  printf "  %-32s " "$path"
  curl -s -o /dev/null -w "%{http_code}\n" "$LIVE_URL$path"
done
```

All paths should return 200.
