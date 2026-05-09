# PIPELINE — full phase walkthrough

The 12-phase pipeline for building a bilingual training course portal. Each phase has its own "done when" criterion. Don't move on until met.

---

## Phase 1 — Scope (~30 min)

Before writing anything, commit a `scope.md` with these four answers:

```markdown
# Scope — <Course Name>

## Outcome
One sentence: "After this course, the reader will be able to ____."

## Audience
Who? Junior engineers? Tech leads? Specific role?

## Format
Self-paced reading? 1-day workshop? Course series?

## Time budget
30 min? 2 hours? 8 hours?
```

**Done when:** scope.md committed.

---

## Phase 2 — Research & capture (~2-4 h)

Find 3-5 **primary sources** — official docs, engineering blogs, formal specs. Avoid "5 best ways to..." aggregator articles.

```bash
mkdir -p raw
# For each source URL:
#   1. WebFetch (or curl + html-to-markdown)
#   2. Save as raw/YYYY-MM-DD-<slug>.md
#   3. Add frontmatter
```

Frontmatter format:

```yaml
---
source_type: web | doc | transcript
source_url: https://...
ingested_at: YYYY-MM-DD
title: <verbatim title>
---
```

**Filter secrets** before saving — replace API keys/tokens with `<REDACTED:kind>`.

**Done when:** ≥3 files in `raw/` with frontmatter, captured verbatim.

---

## Phase 3 — Wiki init (~30 min)

Customise `SCHEMA.md` for your domain:

- **Entity types:** add domain-specific types (e.g. for Kubernetes: `resource`, `controller`, `cluster`)
- **Relations:** keep small and stable (`uses`, `depends-on`, `composes`, `alternative-to`)
- **Half-life:** shorten if domain changes fast (e.g. JS frameworks: 90 days vs Linux fundamentals: 365 days)

**Done when:** SCHEMA.md reflects your domain, not the template defaults.

---

## Phase 4 — Ingest (~2-3 h)

For each raw source, extract entities and write wiki pages:

```bash
# For each entity in raw/<source>:
#   - decide: new entity? or update existing?
#   - if new: wiki/<type>:<slug>.md from wiki/_TEMPLATE.md
#   - every claim ends with [src: raw/<source>] {conf: 0.5}
#   - update graph/entities.jsonl + graph/edges.jsonl
```

**Confidence formula:**
- First observation: `confidence: 0.5`
- Reinforcement (independent source): `conf ← 1 - (1 - conf) * 0.6`

**Rule of thumb:** ~10-15 wiki pages for a 12-module course.

**Done when:** every claim has citation, confidence is set, `wiki-index.md` lists every page.

---

## Phase 5 — Outline (~1 h)

Draft 10-12 modules. **Every module must cite at least one wiki page.** If you can't cite, the domain isn't ready — go back to Phase 4.

Pattern that works:

```
01. Welcome & what you'll learn
02. Definition & analogy
03. Anatomy / contract
04. Core mechanism (the "magic" of the topic)
05. Ecosystem / where it fits
06. Surfaces / variants
07. vs alternatives (decision framework)
08. Best practices
09. Lab / hands-on
10. Implementation guide (advanced)
11. Security & rollout
12. Cheatsheet & resources
```

**Done when:** `outline.md` maps every module → wiki page(s).

---

## Phase 6 — Course pages (~3-5 h)

Fill in `course-en.html`. Each module:

```html
<section id="m{n}" class="module">
  <div class="num">Module 0{n}</div>
  <h2>Module title</h2>
  <p class="summary">One-sentence summary.</p>

  <p>2-3 paragraphs of content...</p>

  <pre><code>// 1-2 code blocks or examples</code></pre>

  <div class="callout takeaway">
    <h4>Takeaway</h4>
    <p>One crisp claim the reader should remember.</p>
  </div>
</section>
```

**Done when:** every anchor resolves, every wiki citation is valid.

---

## Phase 7 — Slide deck (~2-3 h)

Fill in `slides/training-en.html`. ~30-35 slides condensing the course.

**Density rules:**
- Max 6 bullets per slide
- Max 15 lines of code per slide
- Max 5 columns × 5 rows per table
- Use canvas **1280×800**, not the reveal.js default 960×700

**Done when:** every slide fits in canvas, no overflow when projected.

---

## Phase 8 — Bilingual mirror (~3-4 h) — _optional_

Mirror EN → TH:

- **Code blocks stay in English** — never translate identifiers
- **Technical English terms preserved** in `<code>` or `<span class="term-en">`
- **Line-height 1.7** for Thai (1.65 for English) — Thai script has top-and-bottom marks
- **Font:** `Noto Sans Thai` first, then `Inter`

**Done when:** TH structure mirrors EN exactly, language flows naturally.

---

## Phase 9 — Landing page tuning (~1-2 h)

Polish `index.html`. The 8-section pattern:

1. Sticky nav + theme toggle + primary CTA
2. Hero with gradient blur, animated badge, bilingual title, 2-3 CTAs
3. Stats bar (4 numbers building credibility)
4. Why (before/after 2-col)
5. What you'll learn (3-col feature grid, 6 cards)
6. Code/visual preview (real example)
7. How it works (3-tier diagram of core mechanism)
8. Get started cards → Final CTA → Footer

**Done when:** light + dark modes both polished, responsive on 375px width.

---

## Phase 10 — Deploy (~30 min)

```bash
git init -b main
git add .
git commit -m "Initial: <course-name>"
gh repo create your-org/<repo> --public --source=. --push
gh api -X POST /repos/your-org/<repo>/pages \
  -f "build_type=legacy" -f "source[branch]=main" -f "source[path]=/"

# Wait ~30s for first build, then verify
sleep 30
for path in "/" "/course-en.html" "/course-th.html"; do
  curl -s -o /dev/null -w "%{http_code} $path\n" "https://your-org.github.io/<repo>$path"
done
```

**Done when:** all entry-point URLs return HTTP 200.

---

## Phase 11 — Validate (~1-2 h)

| Test | How |
|---|---|
| **Asset coverage** (the one we missed first time) | For each asset (course-en, course-th, slides-en, slides-th, wiki) — grep `index.html` for at least one link. If any asset is reachable only via footer or only in one language, hero/start-section is incomplete. |
| Internal links | `grep -oE 'href="[^"]+"' *.html` then curl each |
| Mobile responsive | DevTools 375px width |
| Theme toggle | Click sun/moon, scroll every section |
| Reading flow | Hand to one peer + one junior, observe friction |
| Citations | Spot-check 5 quotes against wiki/raw |

### Quick asset-coverage check

```bash
# Run from the course repo root
echo "Hero CTAs (visible above the fold):"
sed -n '/class="ctas"/,/<\/div>/p' index.html | grep -oE 'href="[^"]+"' | sort -u

echo
echo "Start-section cards:"
sed -n '/id="start"/,/<\/section>/p' index.html | grep -oE 'href="[^"]+"' | sort -u

echo
echo "All assets that should be reachable from index:"
echo "  course-en.html  course-th.html"
echo "  slides/training-en.html  slides/training-th.html"
echo "  wiki-index.md"

# If any asset is missing from the hero AND start-section, fix before deploy.
```

**Why this check exists:** in the first pass of building a course portal, the index.html had `Pillars of this training` and `Pick your format` filled out — but the start-section only listed the 2 course pages, and the hero CTA had a single `View slides` button (EN-only). Result: a TH reader landing on the page never saw the TH slides existed unless they scrolled to the footer. Footer != entry point.

**Done when:** ≥3 rounds of feedback incorporated AND every asset reachable from index above-the-fold (hero or start-section, not just footer).

---

## Phase 12 — Promote (~1 h)

- Add Featured/Courses card to your personal hub
- Draft blog post: "What I learned writing X" (~600 words)
- Update repo description, add topics
- Tweet/Medium

**Done when:** hub updated, blog post drafted.
