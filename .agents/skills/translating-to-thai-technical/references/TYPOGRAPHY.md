# Thai typography — exact CSS deltas

The minimal CSS changes to convert an EN page to TH-readable.

## Font stack

```css
/* EN */
body { font-family: "Inter","Segoe UI",system-ui,-apple-system,sans-serif; }

/* TH */
body { font-family: "Noto Sans Thai","Inter","Segoe UI",system-ui,-apple-system,sans-serif; }
```

Load Noto Sans Thai from Google Fonts in `<head>`:

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+Thai:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

Note the order — Noto Sans Thai is added alongside Inter, both load.

## Line-heights

| Context | EN | TH | Reason |
|---|---|---|---|
| Body prose | 1.65 | **1.7** | Top tone marks (อ่อ) + bottom vowels (ู) need vertical room |
| Headings | 1.2 | **1.25** | Slight increase for `<h1>` `<h2>` clipping |
| Lists | implicit | **1.5** | Bullets at 0.92em base text need explicit line-height |
| Code blocks | 1.55 | **1.55** | Code is English — keep EN value |
| Slide body | 1.4 | **1.5** | Slide context needs more vertical room than docs |

## Base font sizes

| Context | EN | TH | Reason |
|---|---|---|---|
| Body | implicit (16px) | implicit | Same |
| Slides (reveal.js base) | 30px | **28px** | Thai glyphs render slightly larger; 30 wraps too early |
| Code (in slides) | 0.46em | 0.46em | Same — code is English |
| Tables (in slides) | 0.6em | 0.6em | Same — but check if Thai wraps in cells |

## Letter-spacing

Thai script doesn't need negative letter-spacing for headings the way Latin
display fonts often do. Reduce or zero it:

```css
/* EN */
h1 { letter-spacing: -0.025em; }

/* TH — reset to 0 */
h1 { letter-spacing: 0; }
```

## Word wrapping

Thai doesn't use spaces between words. Browsers can break anywhere. To get
sensible breaks in body text, no special CSS is needed — but for headings
that should NOT break:

```css
h1, h2 { word-break: keep-all; }  /* discourages mid-word breaks */
```

(Use sparingly — over-long Thai headings will overflow if `keep-all` is too
aggressive.)

## The `.term-en` style

When inserting English technical terms inline in Thai prose, give them a
subtle visual cue:

```css
.term-en {
  color: var(--muted);
  font-style: italic;
  font-size: 0.9em;
}
```

Usage:

```html
<p>หลักการสำคัญคือ <span class="term-en">progressive disclosure</span> —
   เปิดเผยทีละชั้น</p>
```

## Bilingual side-by-side

If you're showing EN above TH (e.g. on the course landing page subtitle):

```html
<h1>Course Name</h1>
<p class="h1-th">{{COURSE_NAME_TH}}</p>
```

```css
h1 { font-size: clamp(2.4rem, 6vw, 4rem); font-weight: 800; line-height: 1.05; }
.h1-th {
  font-size: clamp(1.1rem, 2.5vw, 1.5rem);   /* smaller, secondary */
  color: var(--muted);                         /* visually demoted */
  font-weight: 500;
  font-family: "Noto Sans Thai","Inter",sans-serif;
  line-height: 1.4;                            /* TH always needs more */
  margin: 0 0 8px;
}
```

## Mixed-language paragraphs

When a paragraph has both Thai and English (Rule 2 of the parent skill):

- **Browser handles this fine** — Latin characters use Inter, Thai uses Noto
  Sans Thai (Inter doesn't have Thai glyphs, so it falls through automatically).
- **Don't manually wrap** every English word in `<span>`.
- **Do** wrap technical terms in `<code>` or `<span class="term-en">` for
  styling, not for fonts.

## Verifying

After applying the deltas, test by opening the page and:

1. Ctrl/Cmd + scroll to zoom — check that tone marks don't clip
2. View on mobile (375px) — check line-wrapping of long compound words
3. Compare side-by-side with the EN version — text density should look similar
