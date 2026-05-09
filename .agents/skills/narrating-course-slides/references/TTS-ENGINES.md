# TTS engines for slide narration

Comparison of TTS engines tested for the
[oracle-101-course](https://supachai-j.github.io/oracle-101-course/) deck.
Pick based on quality target and budget.

## Quick recommendation

| You want… | Use |
|---|---|
| Free, decent quality, no API key | **edge-tts** (Multilingual voices) |
| Best EN, multilingual support, cheap | **Gemini 2.5 Flash TTS** ⭐ recommended default |
| Best EN voice quality money can buy | **ElevenLabs** |
| Voice cloning (your own voice) | **ElevenLabs** ($5+/mo, 1-min source recording) |

## Engine comparison

### edge-tts (Microsoft)

```bash
pip3 install edge-tts
```

| Aspect | Notes |
|---|---|
| Cost | Free, no API key |
| Rate limit | ~Generous; concurrency of 3-5 is safe |
| EN voice quality | ⭐⭐⭐⭐ with Multilingual, ⭐⭐⭐ with classic |
| TH voice quality | ⭐⭐⭐ Premwadee/Niwat — Thai-native, slightly robotic |
| Style control | None. Only `rate`, `pitch`, `volume` |
| SSML support | Limited — passing `<speak>` blocks is buggy in the Python SDK |

**EN voice picks** (top 5):

| Voice | Tone |
|---|---|
| `en-US-AvaMultilingualNeural` | warm female (newer) — best default |
| `en-US-AndrewMultilingualNeural` | conversational male — best default M |
| `en-US-EmmaMultilingualNeural` | clear professional female |
| `en-US-BrianMultilingualNeural` | confident male |
| `en-US-AriaNeural` | older but stable female (use only as fallback) |

**TH voice picks**:

- `th-TH-PremwadeeNeural` — female (only choice)
- `th-TH-NiwatNeural` — male (only choice)

(No Multilingual variant for Thai. Mitigate with `rate=-8%` for slightly more
natural pacing.)

**Code snippet**:

```python
import edge_tts, asyncio
async def synth():
    com = edge_tts.Communicate(
        text="Hey, welcome to Oracle 101.",
        voice="en-US-AvaMultilingualNeural",
        rate="-8%",
    )
    await com.save("out.mp3")
asyncio.run(synth())
```

Output is MP3 directly. No transcoding needed.

### Gemini 2.5 Flash TTS (Google) ⭐

```bash
pip3 install google-genai
```

| Aspect | Notes |
|---|---|
| Cost | Free tier (~15 RPM); paid ~$0.01 / 1k chars |
| Rate limit | 15 RPM on free tier — concurrency of 3 safe |
| EN voice quality | ⭐⭐⭐⭐⭐ — natural prosody, breath pauses native |
| TH voice quality | ⭐⭐⭐⭐ multilingual — accent passable but not native-perfect |
| Style control | **Yes** — prepend prose-style instruction to prompt; engine adapts delivery |
| Output format | 24kHz mono 16-bit PCM (WAV) — needs ffmpeg transcode to MP3 |

**Voice picks** (work for both EN and TH via multilingual mode):

| Voice | Tone |
|---|---|
| `Aoede` | warm female — best welcome/closing |
| `Kore` | clear female — best for hands-on / definitional |
| `Charon` | confident male — best for principles / capstone |
| `Puck` | curious male — best for memory / coordination |
| `Fenrir` | bass male — gravitas |
| `Leda` | youthful female — agenda / overview |
| `Orus` | tenor male — alternative to Puck |
| `Zephyr` | airy female — alternative to Aoede |

**Code snippet** (with style prompt):

```python
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-flash-preview-tts",
    contents=(
        "Speak with conviction. Slow on the principle name and key claim.\n\n"
        "Of all six rules, this is the one. If you only remember one, make it this. "
        "Nothing gets deleted. Ever."
    ),
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Charon")
            )
        ),
    ),
)
pcm = response.candidates[0].content.parts[0].inline_data.data
# pcm is raw 24kHz mono 16-bit; wrap in WAV header then ffmpeg → MP3
```

**Why it sounds better**: the style prompt is *interpreted*, not just
prefixed. Gemini reads "Speak with conviction, slow on the key claim" as
instruction and adjusts pacing/emphasis on the actual content. This is
fundamentally beyond what voice-only engines can do.

**Future versions**: `gemini-3.x-flash-tts` may exist; check
`client.models.list()` for current names. The skill's
`scripts/generate-gemini-tts.py` tries newer first, falls back.

### OpenAI TTS

```bash
pip3 install openai
```

| Aspect | Notes |
|---|---|
| Cost | `tts-1`: $0.015 / 1k chars; `gpt-4o-mini-tts`: same |
| Rate limit | Generous on paid tier |
| EN voice quality | ⭐⭐⭐⭐⭐ — top-tier natural |
| TH voice quality | ⭐⭐⭐ — accent noticeably non-native |
| Style control | Yes via persona prompt |

Voices: `alloy`, `nova`, `shimmer`, `echo`, `fable`, `onyx`. Multilingual
but EN-strongest.

**Use when**: EN-only deck where you want best-in-class TTS at low cost.

### ElevenLabs

| Aspect | Notes |
|---|---|
| Cost | $5+/mo, 30-100k chars depending on plan |
| Rate limit | Per-plan |
| EN voice quality | ⭐⭐⭐⭐⭐ — indistinguishable from human in many cases |
| TH voice quality | ⭐⭐⭐ — multilingual model, accent fairly noticeable |
| Style control | Voice settings (stability, similarity), some style fields |
| Voice cloning | **Yes** — give 1-2 minutes of source audio, get a personal voice |

**Use when**: Premium production, voice-cloning your own (or a brand) voice,
or you've outgrown Gemini quality for EN-only delivery.

## Secret handling

API keys must NEVER be pasted inline into a chat conversation. Once a key
is in transcript history, it cannot be unsaid.

**Recommended pattern** (works with Claude Code's `!` prefix):

```bash
# 1. User saves key to a stash file (one-time, in their own shell, not in chat)
mkdir -p ~/.config
echo "AIzaSy..." > ~/.config/gemini-key
chmod 600 ~/.config/gemini-key

# 2. Scripts read from the file
export GEMINI_API_KEY="$(cat ~/.config/gemini-key)"
python3 scripts/generate-gemini-tts.py
```

**Alternative**: set in shell profile (`~/.zshrc`):

```bash
export GEMINI_API_KEY="$(cat ~/.config/gemini-key 2>/dev/null)"
```

The skill's scripts read from `$GEMINI_API_KEY` — they don't accept the
key as an argument, so you can't accidentally bake it into a command line
that's later logged.

If a key WAS exposed (in chat, in commit history, in a screenshot):

1. Revoke immediately at the provider:
   - Gemini: https://aistudio.google.com/apikey
   - OpenAI: https://platform.openai.com/api-keys
   - ElevenLabs: https://elevenlabs.io/app/settings/api-keys
2. Generate a new key
3. Update the stash file
4. Audit any usage logs at the provider for unauthorized calls

## Cost estimates for a 40-slide bilingual deck

(80 slides total · ~3,500 words EN + ~3,500 word-chunks TH ≈ 50,000 chars combined)

| Engine | Estimated cost |
|---|---|
| edge-tts | $0.00 (free) |
| Gemini Flash TTS | ~$0.50 (often within free tier) |
| OpenAI TTS | ~$0.75 |
| ElevenLabs | covered by $5/mo plan if not exceeded |

For an 80-slide test run, all four are accessible budgets.

## Migration path

If you start on edge-tts and later want to upgrade:

1. Keep `audio/{lang}/sNN.mp3` paths — the audio bar code doesn't care
   what generated the files.
2. Re-run with new generator script. Files overwrite cleanly.
3. Pages rebuilds; user gets new voices on next visit (no cache busting
   needed because filenames stay the same).

You don't have to pick the right engine on day one. Iterate.
