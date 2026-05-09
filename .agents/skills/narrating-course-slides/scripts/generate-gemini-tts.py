"""Generate per-slide MP3 narration via Gemini Flash TTS.

Style instructions per slide (module-aware) shape delivery beyond what
voice-only engines can do. Uses prebuilt voices in alternating rotation.

Usage:
    pip3 install google-genai
    export GEMINI_API_KEY="$(cat ~/.config/gemini-key)"   # see TTS-ENGINES.md
    python3 generate-gemini-tts.py /path/to/training-en.html

Output: audio/{lang}/sNN.mp3 next to the slides directory.
        Generates 24kHz mono WAV first, then transcodes to MP3 96k via ffmpeg.
"""
import asyncio, os, re, html, sys, wave, subprocess, time
from pathlib import Path

# Voice rotation by slide index. Adjust ranges to match your deck.
VOICE_MAP = {}
def assign(start, end, voice):
    for i in range(start, end + 1):
        VOICE_MAP[i] = voice

# Default: 10-module deck with intro and closing framing
assign(1, 3, "Aoede")    # title/agenda/why — warm female
assign(4, 7, "Kore")     # M1 — clear female
assign(8, 14, "Charon")  # M2 (principles) — confident male
assign(15, 17, "Aoede")  # M3 (anatomy)
assign(18, 20, "Puck")   # M4 (memory) — thoughtful male
assign(21, 23, "Kore")   # M5 (install) — practical
assign(24, 26, "Charon") # M6 (awaken) — slow/ritual
assign(27, 29, "Aoede")  # M7 (skills/builder)
assign(30, 32, "Puck")   # M8 (multi-agent)
assign(33, 35, "Kore")   # M9 (autonomous)
assign(36, 38, "Charon") # M10 (capstone) — motivating
assign(39, 50, "Aoede")  # closing/QA + buffer

def style_for(idx):
    """Module-aware style instruction prepended to the speaker note in the prompt."""
    if idx <= 3:  return "Speak warmly and conversationally, like welcoming a class. Friendly, energetic, with a smile in your voice."
    if idx <= 7:  return "Speak with curiosity, building understanding step by step. Like a teacher who's excited about the topic."
    if idx <= 14: return "Speak with conviction, slowing down on the principle name and the key claim. This is the constitution — speak with weight."
    if idx <= 17: return "Speak like a tour-guide walking through a diagram. Clear, oriented, take your time on the structure."
    if idx <= 20: return "Speak thoughtfully, like a librarian explaining how memory accumulates over time. Patient, reflective."
    if idx <= 23: return "Speak step-by-step, energetic and practical, like a hands-on lab. Direct, action-oriented."
    if idx <= 26: return "Speak with care and meaning, like guiding a ritual. Slow, intentional, almost sacred."
    if idx <= 29: return "Speak like a builder making things work. Hands-on, practical, with a craftsman's confidence."
    if idx <= 32: return "Speak with curiosity, like discovering how a team coordinates. Engaged, leaning forward."
    if idx <= 35: return "Speak measured, balancing excitement with caution. The power is real, the stakes are real."
    if idx <= 38: return "Speak motivating, like a coach before the final challenge. Energetic, encouraging, sending them off."
    return "Speak warmly, wrapping up and inviting questions. Friendly, reflective, giving room to think."

# TTS model preference — try newer first, fall back
MODEL_CANDIDATES = [
    "gemini-3.0-flash-preview-tts",
    "gemini-3.0-flash-tts",
    "gemini-2.5-flash-preview-tts",
    "gemini-2.5-pro-preview-tts",
]

def pick_model(client):
    available = {m.name.replace("models/", "") for m in client.models.list()}
    for c in MODEL_CANDIDATES:
        if c in available:
            return c
    sys.exit(f"ERROR: no TTS model in {MODEL_CANDIDATES}. Available with 'tts': "
             + ", ".join(sorted(m for m in available if "tts" in m.lower())))

def detect_lang(deck_path):
    text = deck_path.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r'<html[^>]*\blang="([^"]+)"', text)
    return (m.group(1).split("-")[0] if m else "en")

def extract_notes(deck_path):
    text = deck_path.read_text(encoding="utf-8", errors="ignore")
    sections = re.split(r'(<section[^>]*>)', text)
    notes = []
    cur = 0
    for chunk in sections:
        if chunk.startswith('<section'):
            cur += 1
            continue
        if cur == 0:
            continue
        m = re.search(r'<aside class="notes">(.*?)</aside>', chunk, re.DOTALL)
        if m:
            t = re.sub(r'<[^>]+>', '', m.group(1))
            t = ' '.join(html.unescape(t).split())
            notes.append((cur, t))
    return notes

def find_ffmpeg():
    for cand in ("ffmpeg", "/opt/homebrew/bin/ffmpeg", "/usr/local/bin/ffmpeg"):
        try:
            subprocess.run([cand, "-version"], check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return cand
        except (FileNotFoundError, subprocess.CalledProcessError):
            continue
    sys.exit("ERROR: ffmpeg not found in PATH. Install: brew install ffmpeg")

async def synth_one(client, model, idx, text, out_dir, ffmpeg, max_retries=3):
    from google.genai import types
    voice = VOICE_MAP.get(idx, "Aoede")
    style = style_for(idx)
    prompt = f"{style}\n\n{text}"
    wav_out = out_dir / f"s{idx:02d}.wav"
    mp3_out = out_dir / f"s{idx:02d}.mp3"

    for attempt in range(1, max_retries + 1):
        try:
            response = await asyncio.to_thread(
                client.models.generate_content,
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["AUDIO"],
                    speech_config=types.SpeechConfig(
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice)
                        )
                    ),
                ),
            )
            pcm = response.candidates[0].content.parts[0].inline_data.data
            with wave.open(str(wav_out), "wb") as w:
                w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000)
                w.writeframes(pcm)
            subprocess.run(
                [ffmpeg, "-y", "-loglevel", "error", "-i", str(wav_out),
                 "-b:a", "96k", str(mp3_out)],
                check=True,
            )
            wav_out.unlink()
            return True
        except Exception as e:
            print(f"  ✗ s{idx:02d} attempt {attempt}: {str(e)[:100]}", flush=True)
            if attempt < max_retries:
                await asyncio.sleep(4 * attempt)
    return False

async def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 generate-gemini-tts.py /path/to/deck.html")
    if not (os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")):
        sys.exit("ERROR: GEMINI_API_KEY or GOOGLE_API_KEY not set in env. "
                 "See TTS-ENGINES.md for safer secret handling.")

    deck = Path(sys.argv[1]).resolve()
    if not deck.exists():
        sys.exit(f"ERROR: {deck} not found")

    lang = detect_lang(deck)
    repo_root = deck.parent.parent
    out_dir = repo_root / "audio" / lang
    out_dir.mkdir(parents=True, exist_ok=True)

    ffmpeg = find_ffmpeg()
    notes = extract_notes(deck)
    if not notes:
        sys.exit(f"ERROR: no <aside class=\"notes\"> found in {deck}")

    from google import genai
    client = genai.Client()
    model = pick_model(client)

    print(f"Deck: {deck}")
    print(f"Lang: {lang}")
    print(f"Model: {model}")
    print(f"Output: {out_dir}")
    print(f"Notes: {len(notes)} slides\n")

    sem = asyncio.Semaphore(3)
    successes = []
    failures = []

    async def worker(idx, text):
        async with sem:
            voice = VOICE_MAP.get(idx, "Aoede")
            print(f"  → s{idx:02d} [{voice}] {text[:50]}…", flush=True)
            ok = await synth_one(client, model, idx, text, out_dir, ffmpeg)
            (successes if ok else failures).append(idx)

    t0 = time.time()
    await asyncio.gather(*(worker(idx, txt) for idx, txt in notes))
    elapsed = time.time() - t0

    print(f"\n=== Done in {elapsed:.0f}s ===")
    print(f"  ✓ {len(successes)} succeeded")
    if failures:
        print(f"  ✗ {len(failures)} failed: {sorted(failures)}")
        print(f"\nRe-run script to retry failed slides (existing mp3s are kept).")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
