"""Step 1 — synthesize the background voiceover for a story with edge-tts.

Reads the 'Modified Script' column for the given story and writes:
    stories/<n>/narration.mp3
    stories/<n>/narration.srt   (word-timed subtitles, optional for captions)

Same voice/rate as the original story-1 pipeline (en-US-GuyNeural, -8%).
"""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

import edge_tts

import config


async def _synthesize(text: str, mp3_path: Path, srt_path: Path) -> None:
    communicate = edge_tts.Communicate(text, config.TTS_VOICE, rate=config.TTS_RATE)
    submaker = edge_tts.SubMaker()
    with mp3_path.open("wb") as audio_file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.feed(chunk)
    srt_path.write_text(submaker.get_srt(), encoding="utf-8")


def generate(story_no: int) -> Path:
    """Create narration.mp3 (+ .srt) for a story. Returns the mp3 path."""
    row = config.read_story(story_no)
    script = row["Modified Script"]
    out_dir = config.story_dir(story_no)
    mp3_path = out_dir / "narration.mp3"
    srt_path = out_dir / "narration.srt"

    print(f"[voiceover] story #{story_no}: {row['Video Title']}")
    print(f"[voiceover] {len(script.split())} words, voice {config.TTS_VOICE} @ {config.TTS_RATE}")
    asyncio.run(_synthesize(script, mp3_path, srt_path))

    dur = config.audio_duration_seconds(mp3_path)
    print(f"[voiceover] wrote {mp3_path.name} ({dur:.1f}s) and {srt_path.name}")
    return mp3_path


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Generate narration for a story")
    ap.add_argument("story_no", type=int, help="Story number (matches the CSV 'No' column)")
    args = ap.parse_args()
    generate(args.story_no)
