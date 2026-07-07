"""Orchestrator — build a full YouTube Short for one or more stories.

Per story, in order:
  1. voiceover  -> narration.mp3 (+.srt)          [edge-tts]
  2. split      -> prompts.json (N ~8s scenes)     [Claude]   N = ceil(narration / 8s)
  3. veo        -> clips/NN.mp4                     [Veo 3]
  4. edit       -> <n>_final_vertical.mp4           [ffmpeg]

Everything for a story lands in stories/<n>/ (folder named after the story number).

Default scope is story 1 only — generate it, review it, then batch the rest:
    python run_story.py                 # story 1
    python run_story.py 1 2 3           # a subset
    python run_story.py --all           # all 25 (large Veo bill — see README)

Each step is resumable and skippable:
    python run_story.py 1 --skip voiceover split   # only (re)generate clips + edit
"""

from __future__ import annotations

import argparse
import math

import config
import edit_short
import generate_veo_clips
import generate_voiceover
import split_story_prompts

STEPS = ["voiceover", "split", "veo", "edit"]


def build_story(story_no: int, skip: set[str]) -> None:
    print(f"\n{'=' * 60}\nSTORY #{story_no}\n{'=' * 60}")
    out_dir = config.story_dir(story_no)

    # 1. voiceover — also gives us the target duration to size the scene count.
    narration = out_dir / "narration.mp3"
    if "voiceover" not in skip or not narration.exists():
        generate_voiceover.generate(story_no)

    duration = config.audio_duration_seconds(narration)
    num_scenes = max(1, math.ceil(duration / config.CLIP_SECONDS))
    print(f"[plan] narration {duration:.1f}s -> {num_scenes} clips of {config.CLIP_SECONDS}s")

    # 2. split into scene prompts
    if "split" not in skip or not (out_dir / "prompts.json").exists():
        split_story_prompts.split(story_no, num_scenes)

    # 3. generate Veo clips
    if "veo" not in skip:
        generate_veo_clips.generate(story_no)

    # 4. edit final Short
    if "edit" not in skip:
        edit_short.edit(story_no)


def main() -> None:
    ap = argparse.ArgumentParser(description="Build YouTube Shorts from the story CSV")
    ap.add_argument("stories", nargs="*", type=int, default=[1],
                    help="Story numbers to build (default: 1)")
    ap.add_argument("--all", action="store_true", help="Build all 25 stories")
    ap.add_argument("--skip", nargs="*", choices=STEPS, default=[],
                    help="Steps to skip if their output already exists")
    args = ap.parse_args()

    story_nos = list(range(1, 26)) if args.all else args.stories
    skip = set(args.skip)
    for n in story_nos:
        build_story(n, skip)


if __name__ == "__main__":
    main()
