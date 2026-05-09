---
name: translating-to-thai-technical
description: Mirrors English technical content into Thai while preserving code, identifiers, and English technical terms in <code> or term-en spans. Adjusts typography (line-height 1.7, Noto Sans Thai font) for readable Thai script. Use when the user wants a Thai version, แปลเป็นไทย, TH version, ภาษาไทย, or a bilingual mirror of any technical document — courses, slides, READMEs, blog posts.
license: Apache-2.0
compatibility: Works on any HTML or Markdown content. Pairs naturally with course pages and slide decks but applies broadly to technical writing.
metadata:
  author: supachai-j
  version: "1.0"
  audience: Thai-speaking engineers
allowed-tools: Read Edit Write Grep
---

# Translating to Thai for technical audiences

Thai-language mirror of English technical content, following the patterns used
in [agent-skills-training](https://supachai-j.github.io/agent-skills-training/course-th.html)
and [course-portal-template](https://github.com/supachai-j/course-portal-template).

The big idea: **keep the engineering English, translate the prose**.

## When to use

Trigger when:
- User wants Thai version / TH version / แปลเป็นไทย / ภาษาไทย
- User has English technical content (course, slides, README, blog)
- User describes the audience as Thai engineers
- User wants a bilingual EN/TH course

Don't use for:
- Non-technical content (marketing copy, fiction, legal — different rules)
- Translating Thai → English (this skill is one-directional)
- Whole-document machine translation (this is structured + opinionated)

## The 5 rules that matter

### Rule 1 — Code stays English

Variable names, function names, file paths, command-line flags, JSON keys,
YAML field names, error messages — **never translate**. Thai engineers read
English code natively; translating it just makes it un-runnable.

```python
# ✅ Good
result = calculate_total(items)  # คำนวณยอดรวม

# ❌ Bad
ผลลัพธ์ = คำนวณยอดรวม(รายการ)
```

### Rule 2 — Technical English terms preserved inline

When a Thai sentence references a concept that has a precise English term,
keep the English in `<code>` or `<span class="term-en">`. Don't try to
manufacture a Thai translation for `frontmatter`, `progressive disclosure`,
`subagent`, `pull request`, etc.

```markdown
ทุกไฟล์ <code>SKILL.md</code> เริ่มด้วย YAML <code>frontmatter</code>
ที่ขนาบด้วย <code>---</code>
```

```html
<p>หลักการสำคัญคือ <span class="term-en">progressive disclosure</span> —
   เปิดเผยทีละชั้น</p>
```

Where it adds value, gloss the English term once on first use:

> "หลักการสำคัญคือ <em>progressive disclosure</em> (เปิดเผยทีละชั้น) ซึ่ง..."

### Rule 3 — Tone matches the English

If the source is third-person and pedagogical (e.g. "This skill processes
PDFs"), keep that in Thai too: "Skill นี้ประมวลผลไฟล์ PDF" — not informal
"ฉันช่วย..." or "คุณสามารถ...". Match register.

### Rule 4 — Headings, callouts, and metadata follow the source

Don't reorganise. If the EN page has 12 modules in order A→L, the TH page has
the same 12 modules in the same order. Internal anchors (`#m1`, `#m2`) stay
identical so cross-language links work.

Module numbers stay as Arabic numerals (`Module 01` ↔ `โมดูล 01`), not
spelled out.

### Rule 5 — Typography adjustments are mandatory

Thai script has both top and bottom marks (vowels, tone marks). Default
line-heights designed for Latin script clip them.

| Element | EN | TH | Why |
|---|---|---|---|
| Body line-height | 1.65 | **1.7** | Thai marks need vertical room |
| Slide line-height | 1.4 | **1.5** | Same, tighter context |
| Code line-height | 1.55 | **1.55** | Same — code is English in both |
| Base font (slides) | 30px | **28px** | Thai glyphs render slightly larger |
| Font stack | Inter, system-ui | **"Noto Sans Thai", "Inter", system-ui** | Noto Sans Thai first |

## Workflow

1. **Read the source.** Don't translate yet — understand the structure first.

2. **Duplicate the file.** `cp course-en.html course-th.html`. Or `slides/training-en.html` → `slides/training-th.html`.

3. **Update `<html lang>`.** `<html lang="en">` → `<html lang="th">`.

4. **Swap the font + typography vars** per Rule 5. See
   [`references/TYPOGRAPHY.md`](references/TYPOGRAPHY.md) for exact CSS deltas.

5. **Translate prose paragraph by paragraph.** Skip code blocks entirely.
   For each paragraph, ask: which English terms are technical (Rule 2)?
   Wrap them in `<code>` or `<span class="term-en">`.

6. **Translate headings.** Match the original's structure. Keep code-like
   headings (e.g. "`SKILL.md` frontmatter") with the English token intact.

7. **Translate UI strings.** Buttons, nav links, callouts, status pills:
   "Coming soon" → "เร็วๆ นี้", "Read more" → "อ่านต่อ", "Back to top" →
   "↑ กลับด้านบน", "Theme" → "ธีม", "Lab — try it now" → "Lab — ลองทำเลย".

8. **Cross-link.** Add a "switch language" link at the top: TH page links to
   EN, EN page links to TH.

9. **Spot-check rendering** by opening in browser. Look for:
   - Tone marks not clipping (Rule 5)
   - English code blocks rendering identically
   - Thai prose flowing naturally (no awkward direct-translation seams)

## Common term mappings

See [`references/COMMON-MAPPINGS.md`](references/COMMON-MAPPINGS.md) for the
running glossary. Top-50 highlights:

| EN | TH (Rule 2 says: keep EN inline; this is the gloss when needed) |
|---|---|
| Skill / Agent Skill | Skill / Agent Skill (เก็บ EN — เป็นชื่อเฉพาะ) |
| frontmatter | เก็บ EN |
| progressive disclosure | เก็บ EN — gloss "เปิดเผยทีละชั้น" ครั้งแรกที่ใช้ |
| description | คำอธิบาย — แต่ใน context ของฟิลด์ frontmatter ให้เก็บ EN |
| validation | การตรวจสอบ |
| pipeline | pipeline / กระบวนการ |
| workflow | workflow / กระบวนการทำงาน |
| anti-pattern | anti-pattern / รูปแบบที่ควรเลี่ยง |
| context window | context window — gloss "หน้าต่างบริบท" ครั้งแรก |
| token (LLM) | token (เก็บ EN — เป็นหน่วย) |
| evaluation / eval | evaluation / eval (เก็บ EN) |
| trigger | trigger / การกระตุ้น |
| scaffold | scaffold / โครงสร้างเริ่มต้น |
| repo / repository | repo / repository |
| commit | commit |
| pull request / PR | PR / pull request |
| deploy / deployment | deploy / นำขึ้นใช้งาน |

**Rule of thumb:** if a junior Thai engineer would Google the English word,
keep the English. Don't invent Thai for technical concepts that don't have
a settled translation.

## Slide-deck specifics

For reveal.js decks ([`generating-reveal-deck`](../generating-reveal-deck/SKILL.md)):

```css
/* TH-specific overrides */
.reveal { font-family: "Noto Sans Thai","Inter",system-ui,sans-serif; font-size: 28px; }
.reveal section { line-height: 1.5; }
.reveal pre { font-family: "JetBrains Mono","Menlo",monospace; line-height: 1.4; }
```

Add `.term-en` styling so English terms in Thai prose stand out subtly:

```css
.term-en { color: var(--muted); font-style: italic; font-size: 0.85em; }
```

## Mirroring speaker notes (`<aside class="notes">`)

If the EN deck has speaker notes for narration (typical when the
[`narrating-course-slides`](../narrating-course-slides/SKILL.md) skill will
run later), **mirror the notes to TH too**. Without TH notes, you can only
generate EN audio — the TH deck stays silent.

### Rules for note translation

1. **Don't word-for-word translate.** Notes are spoken script, not document
   text. Match the *intent* and *delivery* — Thai compresses ideas, so word
   count typically drops 30-40%.

2. **Use canonical Thai for quoted source material.** When a note quotes a
   principle, definition, or maxim that exists verbatim in your raw Thai
   source (e.g. `raw/<source>.md` from a course portal scaffold), lift the
   canonical phrasing directly. Don't double-translate Thai → English (in
   slide visible content) → Thai (in notes).

3. **Preserve TTS hygiene from the EN style guide:**
   - No parens, markdown, or special characters
   - Spell out symbols and abbreviations: `ψ` → "psi", `MCP` → "M-C-P",
     `/awaken` → "slash awaken" (or just say "awaken" in context)
   - Periods as breath beats — TTS engines pause naturally on `.`

4. **Particle warmth, used sparingly.** Thai particles like "นะ", "ครับ",
   "ค่ะ", "ล่ะ" add warmth to spoken delivery — but if used on every line
   the result feels affected. 1-2 per slide max.

5. **Match conversational openers.** EN openers like "Hey,", "Alright,",
   "So," map to Thai "เฮ้", "เอ้า", "OK งั้น", "ทีนี้นะ", "ลองคิดดู". Vary
   them so the deck doesn't sound like every slide opens the same way.

### Example

**EN note** (from a slide on Principle 1):

> "Of all six rules, this is the one. If you only remember one, make it
> this. Nothing gets deleted. Ever. Got something wrong? You don't reach
> for delete — you append the correction."

**Bad TH** (literal translation, awkward):

> "จากกฎทั้งหกข้อ ข้อนี้คือข้อนั้น ถ้าคุณจะจดจำเพียงข้อเดียวเท่านั้น
> จงทำให้ข้อนี้เป็นข้อนั้น ไม่มีสิ่งใดถูกลบทิ้ง..."

**Good TH** (canonical Thai from raw source + conversational frame):

> "ในหกหลักทั้งหมด ข้อนี้แหละคือตัวจริง. ถ้าจำได้แค่ข้อเดียว ขอให้เป็นข้อนี้.
> Nothing is Deleted. ลบไม่ได้ ห้ามลบ. ถ้าผิด เราจะ append คำแก้ไขลงไปข้าง ๆ
> ของเก่า ไม่ลบทิ้ง."

Notice: kept "Nothing is Deleted" and "append" in English (canonical terms),
used "ลบไม่ได้ ห้ามลบ" as a single-word-style breath beat for emphasis,
matched the rhythm of the EN ("Ever." → "ลบไม่ได้").

### Done check (when notes are part of the mirror)

- [ ] TH `<aside class="notes">` count equals EN count
- [ ] Each TH note feels like a Thai teacher *talking*, not a translation
- [ ] Quoted material uses canonical Thai (no double-translation)
- [ ] Same English tokens left in English in both decks (`Oracle`, `MCP`,
      `psi`, `/awaken`, etc.)

## Markdown content (READMEs, blog posts)

Markdown doesn't have inline classes by default, but you can:

- Use backtick code spans (` `frontmatter` `) — they render in monospace and
  preserve English
- Use *italics* (`*progressive disclosure*`) for technical terms when no
  code styling fits
- Use `**bold**` for emphasis as in the EN source

Don't try to inject HTML `<span>` into markdown unless the renderer is
known to allow it.

## Anti-patterns

- ❌ **Translating code**: `def create_user()` → `def สร้างผู้ใช้()` — breaks the code
- ❌ **Inventing Thai for technical terms** with no settled translation
- ❌ **Same line-height as EN** → Thai marks clip
- ❌ **Reordering content** to "match Thai readability" — keep parity
- ❌ **Auto-translating with no review** — output sounds like Google Translate; readers can tell
- ❌ **Skipping the gloss on first use** for terms readers won't have seen

## Output review

Before declaring the translation done, ask a fluent reviewer to:

1. Skim the first 200 words in TH — does it flow as if written in Thai, or
   read like a translation?
2. Spot 5 random technical terms — are they handled per Rule 2?
3. Compare anchor IDs and module numbering — match exactly?
4. Open in browser and look for clipping, weird font fallback, broken layout.

## Related skills

- [`scaffolding-course-portal`](../scaffolding-course-portal/SKILL.md) — calls this in Phase 8
- [`generating-reveal-deck`](../generating-reveal-deck/SKILL.md) — TH-specific deck CSS

## References

- [`references/TYPOGRAPHY.md`](references/TYPOGRAPHY.md) — CSS deltas for Thai
- [`references/COMMON-MAPPINGS.md`](references/COMMON-MAPPINGS.md) — running glossary
