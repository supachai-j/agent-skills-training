---
name: generating-reveal-deck
description: Generates reveal.js HTML slide decks from a markdown outline, wiki claims, or course content — using a fixed canvas of 1280×800 and density rules that prevent overflow. Use when the user wants slides, a deck, a presentation, talk material, or to convert an existing course/wiki/markdown into projectable slides — even when reveal.js isn't named explicitly.
license: Apache-2.0
compatibility: Designed for static hosting (GitHub Pages, S3, Netlify). reveal.js loaded via CDN — no build step.
metadata:
  author: supachai-j
  version: "1.0"
  template_asset: assets/template-deck.html
allowed-tools: Read Write Edit Glob Grep Bash(open:*)
---

# Generating reveal.js slide decks

Produces single-file reveal.js decks following the design system used in
[agent-skills-training](https://github.com/supachai-j/agent-skills-training/tree/main/slides).
Skills isolates the canvas-size and density bugs that cause slides to crop on projectors.

## Quick start

Copy the bundled starter and edit:

```bash
cp ${CLAUDE_SKILL_DIR}/assets/template-deck.html slides/training-en.html
```

Then for each slide section, write content using the patterns in
[references/PATTERNS.md](references/PATTERNS.md) and obey the density rules in
[references/DENSITY-RULES.md](references/DENSITY-RULES.md).

## The two settings that matter most

### 1. Canvas size — always 1280 × 800

reveal.js's default is 960 × 700. **It will crop everything dense in your decks.**

```javascript
Reveal.initialize({
  width: 1280,
  height: 800,
  margin: 0.06,
  minScale: 0.2,
  maxScale: 1.8,
  ...
});
```

### 2. Base font size — 30 px (28 px for Thai)

```css
.reveal { font-family: "Inter", system-ui, sans-serif; font-size: 30px; }
/* TH variant */
.reveal { font-family: "Noto Sans Thai", "Inter", sans-serif; font-size: 28px; }
```

## Density rules (do not exceed)

| Element | Max per slide | Why |
|---|---|---|
| Bullets | **6** | Reading time on stage exceeds attention span beyond this |
| Lines of code | **15** | Anything more becomes unreadable at projector resolution |
| Table columns × rows | **5 × 5** | More rows mean type shrinks below readable on screen |
| Code font-size | **0.46em** | Tested working at 1280×800; smaller becomes pixel mush |
| Table font-size | **0.6em** | Same |

If a slide doesn't fit, **split it** — don't shrink fonts further.

## Slide patterns that work

See [references/PATTERNS.md](references/PATTERNS.md) for the full set:

- **Title slide** — `<section class="center">` with `<h1>` + tagline + pill badges
- **Agenda** — numbered `<ol>`, max 6 items
- **Definition** — `<p class="big">` lead + 3-bullet expansion
- **Comparison table** — for "X vs Y vs Z" decisions
- **Code example** — single `<pre><code>` block, max 15 lines
- **Takeaway / quote** — `<p class="quote">` with border-left
- **2-column grid** — `.grid2 { display: grid; grid-template-columns: 1fr 1fr; }`
- **Q&A close** — `<section class="center">` mirroring title
- **Speaker notes** — every slide should ship with `<aside class="notes">` for narration, accessibility, and instructor speaker-view. See [`narrating-course-slides`](../narrating-course-slides/SKILL.md).

## CSS that ships with the template

The starter HTML has CSS variables for accent colors and typography. The palette
matches the rest of the project:

- `--accent: #d97757` (project orange)
- `--accent2: #5d8aa8` (project blue)
- `--muted: #9aa0a6`

Don't rename these — every other skill in the project assumes them.

## Bilingual decks

Build EN first, then mirror to TH using the
[`translating-to-thai-technical`](../translating-to-thai-technical/SKILL.md) skill.

The TH template differs only in:
- Font stack: `"Noto Sans Thai", "Inter"` first
- Base font: `28px` instead of `30px`
- Line-height: `1.5` for body, `1.4` for code (Thai script needs more vertical room)

## Final checklist

Before declaring the deck done:

- [ ] Canvas set to `width: 1280, height: 800`
- [ ] Base font size set (30px EN / 28px TH)
- [ ] No slide exceeds 6 bullets
- [ ] No code block exceeds 15 lines
- [ ] Tested by opening in browser at full screen
- [ ] Slide numbers visible (`slideNumber: 'c/t'`)
- [ ] Highlight + notes plugins loaded
- [ ] Title slide + agenda slide + Q&A close exist
- [ ] Every slide has `<aside class="notes">` (≥30 words if narration is intended; can be brief or empty for live-only decks)

## Related skills

- [`scaffolding-course-portal`](../scaffolding-course-portal/SKILL.md) — orchestrator that calls this skill in Phase 7
- [`translating-to-thai-technical`](../translating-to-thai-technical/SKILL.md) — for the TH mirror
- [`adding-theme-toggle`](../adding-theme-toggle/SKILL.md) — for the landing page that links the deck
- [`narrating-course-slides`](../narrating-course-slides/SKILL.md) — adds TTS narration, transcript drawer, and live captions to a finished deck
