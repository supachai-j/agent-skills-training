---
name: narrating-course-slides
description: Adds TTS narration, transcript drawer, and live captions to a finished reveal.js slide deck. Generates per-slide MP3 audio from `<aside class="notes">` speaker notes via edge-tts (free) or Gemini TTS (paid, more natural), embeds an audio control bar with auto-advance, an optional transcript drawer, and a sentence-synced captions overlay. Use when the user wants narrated slides, slide audio, voice-over, self-paced training audio, accessibility captions, or asks "can the slides talk?".
license: Apache-2.0
compatibility: Requires Python 3.9+, ffmpeg, and either edge-tts (pip install) or a Gemini API key. Tested with reveal.js 5.x.
metadata:
  author: supachai-j
  version: "1.0"
allowed-tools: Bash(python3:*) Bash(pip3:*) Bash(ffmpeg:*) Bash(grep:*) Read Write Edit
---

# Narrating course slides

Turns a silent reveal.js deck into a self-paced narrated course — speaker
notes become per-slide audio, with an audio bar, transcript drawer, and
live captions wired in. Distilled from shipping
[oracle-101-course](https://supachai-j.github.io/oracle-101-course/) bilingually.

## When to use

Trigger when:
- User has a reveal.js deck and wants narration / voice-over / audio
- User wants accessibility (captions, transcript)
- User wants self-paced training where slides advance with audio
- User asks "can the slides talk?" / "ใส่เสียงให้ slide" / "narrate the deck"

Do **not** use for:
- Decks not built with reveal.js (use a different runner)
- Live instructor-led decks where the instructor is the narrator (overkill)
- Slides without speaker notes — generate notes first via [`generating-reveal-deck`](../generating-reveal-deck/SKILL.md)

## Pre-flight

The deck must already exist with `<aside class="notes">` on every slide.
If notes are missing, generate them first using the style guide in
[`references/SPEAKER-NOTES-STYLE.md`](references/SPEAKER-NOTES-STYLE.md).

## The 4-stage pipeline

| # | Stage | Time | Output |
|---|---|---|---|
| 1 | Speaker notes review | ~30 m | every `<section>` has 30-90 word `<aside class="notes">` in the natural conversational style |
| 2 | Choose TTS engine | ~5 m | edge-tts (free) or Gemini (paid, more natural) — see [`references/TTS-ENGINES.md`](references/TTS-ENGINES.md) |
| 3 | Generate audio | ~10 m | `audio/{lang}/sNN.mp3` (one per slide × languages) |
| 4 | Embed UI | ~10 m | audio bar + transcript drawer + live captions wired into deck HTML |

**Total**: ~1 hour for a 40-slide bilingual deck.

## Stage 1 — Speaker notes (the foundation)

Notes are the script. Voice quality follows script quality.

**Style snapshot** (full guide in `references/SPEAKER-NOTES-STYLE.md`):

- Conversational, not lecture-ish: "Okay, here's the trick…" not "In this slide we examine…"
- 30-90 words per slide. Aim ~50-70.
- Periods as breath beats. Short sentences mixed with longer.
- No parens, no markdown, no special chars (TTS hates them).
- Spell out symbols and abbreviations: `ψ` → "psi", `MCP` → "M-C-P".

**Anti-pattern**: writing notes that just paraphrase the slide bullets. The
slide is what the audience *sees*; the note is what they *hear*. Different
job.

## Stage 2 — Choose TTS engine

| Engine | Cost | Quality (EN) | Quality (TH) | Style control |
|---|---|---|---|---|
| **edge-tts** Multilingual | Free | ⭐⭐⭐⭐ | ⭐⭐⭐ | rate/pitch only |
| **Gemini 2.5 Flash TTS** | ~$0.01/1k chars | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | full prose-style prompts |
| **OpenAI gpt-4o-mini-tts** | ~$0.015/1k chars | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | persona prompts |
| **ElevenLabs** | $5+/mo | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | voice cloning available |

**Default recommendation**: Gemini 2.5 Flash TTS. The "speak warmly, like a
teacher" style prompts genuinely improve delivery beyond what voice-only
engines can do.

**If no API key**: edge-tts with Multilingual voices is the best free option.
Don't use the basic Aria/Guy voices — switch to AvaMultilingualNeural /
AndrewMultilingualNeural for noticeably more natural EN. TH stays on
PremwadeeNeural / NiwatNeural (no multilingual variant).

## Stage 3 — Generate audio

### Voice rotation strategy

Alternate F/M voices by module to add variety. Recommended for 10-module
courses:

```
Intro/framing slides     → female warm  (Aoede / Aria)
M1 (definitional)        → female       (Kore / Aria)
M2 (principles)          → male strong  (Charon / Guy)
M3 (anatomy)             → female       (Aoede)
M4 (memory/depth)        → male thoughtful (Puck / Andrew)
M5 (hands-on install)    → female practical (Kore)
M6 (ritual/awakening)    → male slow    (Charon)
M7 (skills/builder)      → female       (Aoede)
M8 (multi-agent)         → male curious (Puck)
M9 (autonomous/caution)  → female measured (Kore)
M10 (capstone/coach)     → male motivating (Charon)
Closing/Q&A              → female warm  (Aoede)
```

### Style prompts (Gemini only)

Per module, prepend a style instruction to the speaker note. Example
prompts in `scripts/generate-gemini-tts.py`:

- Intro: "Speak warmly and conversationally, like welcoming a class."
- Principles: "Speak with conviction. Slow on the principle name."
- Lab: "Speak step-by-step, energetic and practical."
- Capstone: "Speak motivating, like a coach before the final challenge."

### Run

```bash
# edge-tts path (free, no API key)
pip3 install edge-tts
python3 scripts/generate-edge-tts.py /path/to/deck.html

# Gemini path (paid, more natural)
pip3 install google-genai
export GEMINI_API_KEY=AIzaSy...     # see TTS-ENGINES.md for safer secret handling
python3 scripts/generate-gemini-tts.py /path/to/deck.html
```

Both scripts emit `audio/{lang}/sNN.mp3` (one per slide). Concurrency is
limited to 3 to stay under free-tier rate limits. Failed slides retry with
backoff; if any fail at the end, you can re-run for just those slides.

## Stage 4 — Embed UI

Drop the snippet from `assets/narration-bar.html` into your deck just
before `</body>`. It includes:

- **Audio control bar** (bottom-right, fixed) — play/pause, scrubber, volume
- **`auto-advance` checkbox** (default on) — slide advances when audio ends, unless user paused
- **`captions` checkbox** (default off) — sentence-synced overlay at bottom of slide canvas
- **`transcript` checkbox** (default off) — slide-up drawer with full notes, scrollable
- **Sync logic** — on `slidechanged`, loads the matching MP3 and rebuilds the sentence timeline

### Sentence sync (caption math)

Captions use sentence-level sync via character-ratio across audio duration:

```
sentence_start_time = (chars_before_sentence / total_chars) * audio.duration
```

This is ~80-90% accurate without transcription. For word-level precision,
upgrade to Whisper transcription (1-2 hr extra work) — out of scope for
this skill.

### Per-language tweaks

The TH narration bar uses Noto Sans Thai font and slightly larger
line-height (1.55 vs 1.4) for tone-mark room. The snippet has both
`LANG = "en"` and `LANG = "th"` variants.

## Quality gates

Before declaring narration done:

- [ ] Every slide has `<aside class="notes">` with ≥30 words
- [ ] All `audio/{lang}/sNN.mp3` files generated (no gaps)
- [ ] Spot-check 3 random slides per language by listening start-to-finish
- [ ] Auto-advance triggers slide change on audio end
- [ ] Captions toggle reveals overlay synced to audio
- [ ] Transcript drawer shows current slide's notes; updates on slide change
- [ ] Audio bar lifts above transcript drawer when both open
- [ ] Print stylesheet hides bar/drawer/captions

## Common anti-patterns

- **Bulk-generating before sampling.** Always generate slide 1 (and one Lab/principle slide for tone variety) FIRST. Listen. Confirm with user. Then bulk. Saved my hide on the original Oracle 101 build.
- **Pasting API keys inline.** Once a key is in the conversation transcript, it's exposed forever. Use file-based stash or environment-only.
- **Translating notes word-by-word.** Bilingual narration: keep the *intent* equivalent, not the word count. Thai needs fewer words for the same idea. Reuse canonical phrasings from your source corpus where possible.
- **Captions for 100-word notes.** If your note is one giant paragraph, captions overlap or scroll past audio. Keep notes ≤90 words AND use periods as sentence breaks (TTS pauses on `.`, captions split on `.`).
- **Skipping the audio bar's auto-advance pause guard.** If the user pauses mid-slide, don't auto-advance. The snippet handles this; don't strip it out.

## What this skill does NOT cover

- **Recording your own voice** — out of scope. Use a DAW (Audacity, Reaper) or ElevenLabs voice cloning.
- **Word-level karaoke** — sentence-level only. Word-level requires Whisper transcription; can be added as Stage 5 if needed.
- **MP4 export** — for YouTube/Vimeo, separate pipeline (Playwright + ffmpeg). The narrated reveal.js deck stays in browser.
- **Live transcription of instructor speech** — opposite direction. This is pre-recorded narration.

## References

- [`references/SPEAKER-NOTES-STYLE.md`](references/SPEAKER-NOTES-STYLE.md) — conversational style guide with examples
- [`references/TTS-ENGINES.md`](references/TTS-ENGINES.md) — engine comparison + voice catalog + secret handling
- [`assets/narration-bar.html`](assets/narration-bar.html) — drop-in HTML/CSS/JS snippet for the audio bar + transcript drawer + captions
- [`scripts/generate-edge-tts.py`](scripts/generate-edge-tts.py) — free TTS pipeline
- [`scripts/generate-gemini-tts.py`](scripts/generate-gemini-tts.py) — paid TTS pipeline with style prompts

## Related skills

- [`generating-reveal-deck`](../generating-reveal-deck/SKILL.md) — produces the deck this skill narrates
- [`scaffolding-course-portal`](../scaffolding-course-portal/SKILL.md) — orchestrator; calls this in optional Phase 7b
- [`translating-to-thai-technical`](../translating-to-thai-technical/SKILL.md) — for bilingual notes (translate notes between EN/TH before generating audio)
