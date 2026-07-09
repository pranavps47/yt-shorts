"""Step 1 — synthesize the background voiceover for a story with edge-tts.

Reads the 'Modified Script' column for the given story and writes:
    stories/<n>/narration.mp3
    stories/<n>/narration.srt          (word-timed subtitles, for captions)
    stories/<n>/narration_words.json   (per-word [text,start,end] — drives clip sync)

Same voice/rate as the original story-1 pipeline (en-US-GuyNeural, -8%).
"""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

import edge_tts

import config


def _fmt_ts(seconds: float) -> str:
    """seconds -> SRT timestamp HH:MM:SS,mmm"""
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _to_srt(segments: list[dict]) -> str:
    """One SRT cue per timed segment (sentence- or word-level)."""
    lines = []
    for cue, seg in enumerate(segments, start=1):
        text = seg["text"].strip()
        lines.append(f"{cue}\n{_fmt_ts(seg['start'])} --> {_fmt_ts(seg['end'])}\n{text}\n")
    return "\n".join(lines)


async def _synthesize(text: str, mp3_path: Path, srt_path: Path, words_path: Path) -> None:
    communicate = edge_tts.Communicate(text, config.TTS_VOICE, rate=config.TTS_RATE)
    # edge-tts emits WordBoundary on some versions and SentenceBoundary on others
    # (7.x). Capture whichever we get — both carry offset/duration in 100-ns ticks
    # and the spoken text — and let the aligner interpolate within a segment.
    segments: list[dict] = []
    with mp3_path.open("wb") as audio_file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_file.write(chunk["data"])
            elif chunk["type"] in ("WordBoundary", "SentenceBoundary"):
                start = chunk["offset"] / 1e7
                segments.append({
                    "text": chunk["text"],
                    "start": start,
                    "end": start + chunk["duration"] / 1e7,
                })
    words_path.write_text(json.dumps(segments, ensure_ascii=False), encoding="utf-8")
    srt_path.write_text(_to_srt(segments), encoding="utf-8")


def generate(story_no: int) -> Path:
    """Create narration.mp3 (+ .srt) for a story. Returns the mp3 path."""
    row = config.read_story(story_no)
    script = row["Modified Script"]
    out_dir = config.story_dir(story_no)
    mp3_path = out_dir / "narration.mp3"
    srt_path = out_dir / "narration.srt"
    words_path = out_dir / "narration_words.json"

    print(f"[voiceover] story #{story_no}: {row['Video Title']}")
    print(f"[voiceover] {len(script.split())} words, voice {config.TTS_VOICE} @ {config.TTS_RATE}")
    asyncio.run(_synthesize(script, mp3_path, srt_path, words_path))

    dur = config.audio_duration_seconds(mp3_path)
    print(f"[voiceover] wrote {mp3_path.name} ({dur:.1f}s), {srt_path.name}, {words_path.name}")
    return mp3_path


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Generate narration for a story")
    ap.add_argument("story_no", type=int, help="Story number (matches the CSV 'No' column)")
    args = ap.parse_args()
    generate(args.story_no)
