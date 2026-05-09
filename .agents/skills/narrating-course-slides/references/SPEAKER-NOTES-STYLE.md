# Speaker notes style guide

How to write speaker notes that sound like a teacher *talking* — not reading
a textbook aloud. These notes feed TTS engines; the voice can only do as
much as the script lets it.

## The core rule

> "Write what you'd say, not what you'd write."

Read every note out loud before saving. If it sounds like documentation, rewrite.

## Anatomy of a good note

```
Hey, here's the one sentence I want you to hold onto.       ← warm opener
Oracle is an external brain that humans and many agents     ← the claim, simply
use together. That's it.                                    ← short for emphasis
Not one chatbot. Not just a database. Not just a web page.  ← rhythm via parallelism
Hold that picture.                                          ← direct call to listener
Everything else hangs off of it.                            ← lands the takeaway
```

~50 words. Reads in ~20 seconds. Each sentence does one thing.

## Length target

| Slide type | Word range | Audio duration |
|---|---|---|
| Title / agenda / closing | 30-50 | 12-20 sec |
| Definitional / principles | 50-70 | 20-28 sec |
| Hands-on / lab | 60-90 | 24-36 sec |
| Anything | **never over 100** | 40 sec is the upper limit before listeners drift |

## Style rules

### 1. Conversational openers

Pick one to lead each note (vary across the deck so they don't all sound the same):

- "Hey," / "Alright," / "OK so,"
- "Look —"
- "Here's the trick —"
- "So you're here because…"
- "Let me give you the picture."
- "Now —"
- "Got something wrong?" (rhetorical question opener)
- Thai equivalents: "เฮ้", "เอ้า", "OK งั้น", "ทีนี้นะ", "ลองคิดดู", "เคยเจอไหม"

**Avoid**: "In this slide we will examine…", "ในสไลด์นี้เราจะมาดู…", "Welcome everyone to module N…"

### 2. Short sentences mixed with longer

Variety creates rhythm. TTS engines pause naturally on `.`, so periods are
your breath beats.

```
Of all six rules, this is the one. If you only remember one, make it this.
Nothing gets deleted. Ever. Got something wrong? You don't reach for delete —
you append the correction. New sits beside old.
```

Notice: "Ever." as a one-word sentence. "Got something wrong?" as a beat.

### 3. Contractions everywhere

Spoken English uses contractions. Written-aloud TTS does too.

| Don't write | Do write |
|---|---|
| "you will" | "you'll" |
| "we are" | "we're" |
| "do not" | "don't" |
| "is not" | "isn't" |
| "it is" | "it's" |

### 4. Direct address

Use "you" / "your" / "you'll". The listener is one person, not an audience.

```
✅ "Pick a name. Make it yours."
❌ "Learners should select a meaningful identity."
```

### 5. Imagery over jargon

Concrete pictures beat abstract terms. The voice can convey image; jargon flattens.

| Jargon | Image |
|---|---|
| "load-bearing rule for storage" | "history book — not a graveyard" |
| "multi-agent orchestration deployment" | "tiny family of agents on your machine" |
| "principle of progressive disclosure" | "you don't see everything at once — it reveals as you ask" |

### 6. Rhetorical questions

Let the listener fill in. Pauses naturally after `?`.

```
"Sound familiar?"
"Why does this matter?"
"Got something wrong?"
"เคยเจอไหม?"
"ใช่ไหมล่ะ?"
"ทำไมล่ะ?"
```

### 7. TTS hygiene

Avoid characters that confuse TTS engines. Spell things out:

| Don't write | Do write |
|---|---|
| `ψ` | `psi` |
| `MCP` | `M-C-P` (or just `MCP` and trust the voice — depends on engine) |
| `(see ch01)` | (drop the parens — context is on the slide already) |
| `→` | `to` or `becomes` |
| `#42` | `number forty-two` (long numbers especially) |
| Markdown like `**bold**` | drop the markdown — voice can't see it |

For symbols that have a known reading (`/`, `&`, `@`), most modern engines
handle them. Test 1 slide first.

## Module-specific tone (Gemini style prompts)

When using Gemini TTS, prepend a style instruction to each note. Match the
module's pedagogical role:

| Module type | Style prompt |
|---|---|
| Welcome / framing | "Speak warmly and conversationally, like welcoming a class." |
| Definitional | "Speak with curiosity, building understanding step by step." |
| Principles / canonical | "Speak with conviction. Slow on the principle name and key claim." |
| Architecture / anatomy | "Speak like a tour-guide walking through a diagram." |
| Memory / depth | "Speak thoughtfully, like a librarian explaining how memory accumulates." |
| Hands-on / lab | "Speak step-by-step, energetic and practical." |
| Ritual / awakening | "Speak with care and meaning. Slow, intentional." |
| Multi-agent / coordination | "Speak with curiosity, like discovering how a team works together." |
| Autonomous / cautionary | "Speak measured, balancing excitement with caution." |
| Capstone / closing | "Speak motivating, like a coach before a final challenge." |

These prompts stack on top of the note text. Gemini reads them as
*instruction* and adapts delivery accordingly. Cannot do this with edge-tts.

## Bilingual notes (TH mirror)

When mirroring EN notes to TH:

1. **Don't word-for-word translate.** Keep the *intent* — not the word count.
2. **Keep English tokens English** — `Oracle`, `MCP`, `psi`, `/awaken`, `arra-oracle-v3` stay as-is.
3. **Use Thai particles for warmth** sparingly — "นะ", "ครับ", "ล่ะ" — not on every line.
4. **Reuse canonical Thai** from source corpus when available — don't double-translate.
5. **Single-word sentences for rhythm** translate well: "เด็ดขาด." "ลบไม่ได้." "นั่นแหละ."

### TH style prompts (Gemini)

Translate the EN style prompt naturally:

| EN | TH |
|---|---|
| "Speak warmly, like welcoming a class" | "พูดอย่างอบอุ่น เหมือนทักนักเรียนใหม่ในชั้น" |
| "Speak with conviction, slowing on the key claim" | "พูดด้วยน้ำเสียงมั่นใจ พูดช้าเมื่อย้ำจุดสำคัญ" |
| "Speak step-by-step, energetic and practical" | "พูดทีละขั้น มีพลัง ปฏิบัติได้จริง" |

## Anti-patterns (audit your draft against these)

- **Telegraphing the takeaway**: "The takeaway from this slide is…" — just say the takeaway. The slide has its own callout.
- **Restating the slide bullets**: notes should *expand* or *motivate*, not echo. If you can replace the audio with the slide text, the audio added nothing.
- **Lists in narration**: "First, X. Second, Y. Third, Z." — sounds like a list. Try: "X is the start. Then Y kicks in. Z lands the deal."
- **Welcoming every module**: "Welcome to Module 5!" — they're already in module 5; they don't need welcoming again. Save warmth for the actual welcome slide.
- **Saying "this slide"**: "in this slide we cover…" — listener can already see the slide. Just talk about the content.

## Sample rewrites

### Before (textbook)
> "This module covers the five principles plus rule six. Each is a rule that governs Oracle behavior. Memorize them in order."

### After (teacher talking)
> "Here's the trick — six rules, but they're not equal. Number one carries the most weight. Numbers two through five hang off it. Rule six? That came later. Painful lesson learned the hard way. Don't memorize them in order — just feel out which one each module leans on."

### Before (formal Thai)
> "ในโมดูลนี้เราจะมาเรียนหลักทั้ง 5 ของ Oracle รวมทั้งกฎข้อที่ 6"

### After (teacher talking, Thai)
> "ทีนี้นะ. หกหลัก แต่ไม่ได้น้ำหนักเท่ากัน. หลักหนึ่งหนักสุด. หลักสองถึงห้าห้อยอยู่บนหลักหนึ่ง. ส่วน Rule 6? มาทีหลัง. บทเรียนเจ็บที่เกิดจริง ไม่ใช่ปรัชญาที่นั่งคิด."

## Final check before generating audio

```
[ ] Read aloud — does it sound like a person, not a document?
[ ] Word count between 30 and 90?
[ ] Periods placed deliberately for breath?
[ ] No parens, markdown, or unspelled symbols?
[ ] Direct address ("you" / "คุณ") used somewhere?
[ ] Imagery used at least once for non-trivial slides?
[ ] No telegraphed takeaways or restated bullets?
```

If any unchecked, rewrite before TTS. The audio will mirror exactly what
you wrote — including the flatness.
