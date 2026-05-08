# Density rules — full rationale

Why these specific numbers, and what to do when content doesn't fit.

## The problem

reveal.js's default canvas is **960 × 700**. At that size, a slide with:
- ~8 bullets at default font size
- A 4-column table with 6 rows
- A 25-line code snippet

…all crop on projection. No warning, no error. The slide just doesn't fit and
the audience reads only the top half.

## The fix

Change the canvas to **1280 × 800** in `Reveal.initialize()`. This gives ~50%
more vertical room. Combined with tighter base font (30 px instead of the
implicit 36 px from default theme), most realistic slides fit.

## Hard limits (above 1280×800 canvas)

| Element | Max | What happens past this |
|---|---|---|
| Bullets per slide | 6 | Reading time on stage exceeds attention span; audience drops |
| Lines of code | 15 | Code font drops below 14px on a 1080p projector — pixel mush |
| Table columns | 5 | Cell padding reduces below comfortable; type shrinks |
| Table data rows | 5 | Combined with header, 6 rows × ~10 px line-height = overflow |
| Heading levels per slide | 1 + 2 (h2 + 2× h3) | More than this and the slide reads like a document |

## What to do when content exceeds limits

### "I have 8 bullets I need to cover"

Split into 2 slides. Use a transition like "(continued)" or split by sub-topic:

```
Slide 1:  "Authoring rules — Required"
          - 4 bullets

Slide 2:  "Authoring rules — Optional"
          - 4 more bullets
```

### "I have a 30-line code example"

Three options, in priority order:

1. **Trim to the essential 10-15 lines.** Show the structure, omit boilerplate.
2. **Show the diff/highlight, not the full file.** Use comments like `// ... 50 lines elided` for context.
3. **Split into two slides** showing related parts.

### "I have an 8-column comparison table"

Don't. The table won't be readable on screen. Instead:

- Pick 5 most-important dimensions
- OR rotate: use rows for the dimensions and columns for the items
- OR turn it into a 2-column "before vs after" comparison if the matrix has structure

### "I need to cite 6 sources"

Move citations to a single "Resources" slide near the end, or use abbreviated
markers (`[A]`, `[B]`) inline and full citations in the speaker notes.

## CSS that enforces some of this

The bundled template has these constraints baked into CSS:

```css
.reveal pre { font-size: 0.46em; }           /* keeps code readable */
.reveal table { font-size: 0.6em; }          /* keeps tables readable */
.reveal h2 { font-size: 1.35em; }            /* keeps heading from eating space */
.reveal ul li { line-height: 1.4; }          /* tightens bullet spacing */
```

Don't loosen these unless you know the slide is sparse.

## Verifying density

Before claiming a deck is done:

1. Open in browser, full screen
2. Hit `o` for overview mode
3. Scan for slides where content visibly clips at the bottom
4. Anything cropped → split or trim that slide

Or, projector-test at 1080p resolution if you have access — that's the lowest
common denominator for venues.
