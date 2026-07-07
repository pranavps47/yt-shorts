"""Step 3 — generate one Veo 3 clip per scene prompt, with shot-to-shot continuity.

Reads stories/<n>/prompts.json and writes 9:16 clips to stories/<n>/clips/NN.mp4.

Continuity (config.CONTINUITY, default on): the first clip is text-to-video; every
following clip is generated image-to-video, seeded with the *last frame* of the
previous clip (Veo 3.1 frame conditioning). So each shot begins where the last one
ended instead of hard-cutting to unrelated footage. If a clip fails, the chain
resets and the next clip starts fresh (text-to-video).

Video generation is async and metered per second, so this script:
  - polls each long-running operation until it's done,
  - skips clips that already exist (safe to re-run / resume after a failure),
  - keeps going if one clip fails, and reports which scenes still need a retry.

Uses the google-genai SDK (reads GEMINI_API_KEY). Veo's own audio is ignored —
we overlay narration + music in the edit step.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path

from google import genai
from google.genai import types

import config

POLL_SECONDS = 15


def _clip_path(clips_dir: Path, index: int) -> Path:
    return clips_dir / f"{index:02d}.mp4"


def _lastframe_path(clips_dir: Path, index: int) -> Path:
    return clips_dir / f"{index:02d}_lastframe.png"


def _extract_last_frame(video_path: Path, out_png: Path) -> Path:
    """Grab the final frame of a clip as a PNG (to seed the next clip)."""
    subprocess.run(
        ["ffmpeg", "-sseof", "-0.1", "-i", str(video_path), "-frames:v", "1", "-y", str(out_png)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    return out_png


def _generate_one(client: genai.Client, prompt: str, out_path: Path, image_path: Path | None) -> None:
    cfg = types.GenerateVideosConfig(
        aspect_ratio=config.VEO_ASPECT_RATIO,
        resolution=config.VEO_RESOLUTION,
        number_of_videos=1,
        negative_prompt=config.VEO_NEGATIVE_PROMPT,
    )
    kwargs: dict = {"model": config.VEO_MODEL, "prompt": prompt, "config": cfg}
    if image_path is not None:  # image-to-video: continue from the previous clip's last frame
        kwargs["image"] = types.Image(image_bytes=image_path.read_bytes(), mime_type="image/png")

    operation = client.models.generate_videos(**kwargs)
    while not operation.done:  # poll the long-running operation until the video is ready
        time.sleep(POLL_SECONDS)
        operation = client.operations.get(operation)

    generated = operation.response.generated_videos[0]
    client.files.download(file=generated.video)
    generated.video.save(str(out_path))


def generate(story_no: int) -> list[Path]:
    """Generate every clip for a story from its prompts.json. Returns clip paths."""
    out_dir = config.story_dir(story_no)
    prompts_path = out_dir / "prompts.json"
    if not prompts_path.exists():
        raise FileNotFoundError(f"{prompts_path} missing — run split_story_prompts first")

    data = json.loads(prompts_path.read_text(encoding="utf-8"))
    scenes = sorted(data["scenes"], key=lambda s: s["index"])
    clips_dir = out_dir / "clips"
    clips_dir.mkdir(exist_ok=True)

    client = genai.Client()  # picks up GEMINI_API_KEY
    mode = "continuity (last-frame chained)" if config.CONTINUITY else "independent shots"
    print(f"[veo] story #{story_no}: {len(scenes)} clips via {config.VEO_MODEL} "
          f"({config.VEO_ASPECT_RATIO}, {config.VEO_RESOLUTION}) — {mode}")

    produced: list[Path] = []
    failed: list[int] = []
    prev_last_frame: Path | None = None  # None => next clip is text-to-video

    for scene in scenes:
        idx = scene["index"]
        out_path = _clip_path(clips_dir, idx)
        last_frame = _lastframe_path(clips_dir, idx)

        if out_path.exists() and out_path.stat().st_size > 0:
            print(f"[veo]   scene {idx:02d}: exists, skipping")
            produced.append(out_path)
            if config.CONTINUITY:  # still need this clip's last frame to seed the next one
                if not last_frame.exists():
                    _extract_last_frame(out_path, last_frame)
                prev_last_frame = last_frame
            continue

        seed = prev_last_frame if (config.CONTINUITY and prev_last_frame and prev_last_frame.exists()) else None
        kind = f"continue from scene {idx - 1:02d}" if seed else "text-to-video"
        print(f"[veo]   scene {idx:02d}: generating ({kind})...")
        try:
            _generate_one(client, scene["veo_prompt"], out_path, seed)
            print(f"[veo]   scene {idx:02d}: saved {out_path.name}")
            produced.append(out_path)
            if config.CONTINUITY:
                _extract_last_frame(out_path, last_frame)
                prev_last_frame = last_frame
        except Exception as e:  # keep going; one bad scene shouldn't lose the batch
            print(f"[veo]   scene {idx:02d}: FAILED — {e}")
            failed.append(idx)
            prev_last_frame = None  # chain broken — next clip starts fresh

    if failed:
        print(f"[veo] {len(failed)} scene(s) failed: {failed}. Re-run to retry just those.")
    return sorted(produced)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Generate Veo 3 clips for a story")
    ap.add_argument("story_no", type=int)
    args = ap.parse_args()
    generate(args.story_no)
