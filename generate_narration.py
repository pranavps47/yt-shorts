"""Read story #1 from the CSV, synthesize narration MP3 with timing via edge-tts."""

import asyncio
import csv
from pathlib import Path

import edge_tts

YT_DIR = Path(__file__).parent
CSV_PATH = YT_DIR / "yt_reddit_stories.csv"
MP3_PATH = YT_DIR / "story1_narration.mp3"
SRT_PATH = YT_DIR / "story1_narration.srt"
VOICE = "en-US-GuyNeural"
RATE = "-8%"


def read_first_script() -> tuple[str, str]:
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        row = next(reader)
    return row["Video Title"], row["Modified Script"]


async def synthesize(text: str) -> None:
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
    submaker = edge_tts.SubMaker()
    with MP3_PATH.open("wb") as audio_file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.feed(chunk)
    SRT_PATH.write_text(submaker.get_srt(), encoding="utf-8")


def main() -> None:
    title, script = read_first_script()
    print(f"Story: {title}")
    print(f"Script length: {len(script.split())} words")
    print(f"Voice: {VOICE} at rate {RATE}")
    asyncio.run(synthesize(script))
    print(f"\nWrote: {MP3_PATH}")
    print(f"Wrote: {SRT_PATH}")


if __name__ == "__main__":
    main()
