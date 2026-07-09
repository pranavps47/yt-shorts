"""Step 3 — generate one video clip per scene prompt, via the selected backend.

Backend is chosen with the VIDEO_BACKEND env var (gemini | fal) — see backends.py.
Reads stories/<n>/prompts.json and writes 9:16 clips to stories/<n>/clips/NN.mp4.

Continuity (config.CONTINUITY): the first clip is text-to-video, each following
clip is seeded with the previous clip's last frame. On fal this needs an
image-to-video model (config.FAL_I2V_MODEL); Veo supports it natively. If a clip
fails the chain resets and the next clip starts fresh.

Resumable and fault-tolerant: skips clips that already exist, keeps going if one
clip fails, and reports which scenes still need a retry. (Note the file name is
historical — it now covers any backend, not just Veo.)
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path

import backends
import config


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


def _preflight() -> None:
    """Fail fast with one clear message if the backend's credentials are missing."""
    if config.VIDEO_BACKEND == "gemini" and not os.environ.get("GEMINI_API_KEY", "").strip():
        raise SystemExit("VIDEO_BACKEND=gemini needs GEMINI_API_KEY in shorts_pipeline/.env.")
    if config.VIDEO_BACKEND == "fal" and not os.environ.get("FAL_KEY", "").strip():
        raise SystemExit(
            "VIDEO_BACKEND=fal needs FAL_KEY. Get $10 free credits at https://fal.ai "
            "(Dashboard > Keys), add FAL_KEY to shorts_pipeline/.env, then retry."
        )


def generate(story_no: int) -> list[Path]:
    """Generate every clip for a story from its prompts.json. Returns clip paths."""
    out_dir = config.story_dir(story_no)
    prompts_path = out_dir / "prompts.json"
    if not prompts_path.exists():
        raise FileNotFoundError(f"{prompts_path} missing — run split_story_prompts first")

    _preflight()

    data = json.loads(prompts_path.read_text(encoding="utf-8"))
    scenes = sorted(data["scenes"], key=lambda s: s["index"])
    clips_dir = out_dir / "clips"
    clips_dir.mkdir(exist_ok=True)

    model_label = config.FAL_MODEL if config.VIDEO_BACKEND == "fal" else config.VEO_MODEL
    mode = "continuity (last-frame chained)" if config.CONTINUITY else "independent shots"
    print(f"[gen] story #{story_no}: {len(scenes)} clips via {config.VIDEO_BACKEND}:{model_label} "
          f"({config.VEO_ASPECT_RATIO}) — {mode}")

    produced: list[Path] = []
    failed: list[int] = []
    prev_last_frame: Path | None = None  # None => next clip is text-to-video

    for scene in scenes:
        idx = scene["index"]
        out_path = _clip_path(clips_dir, idx)
        last_frame = _lastframe_path(clips_dir, idx)

        if out_path.exists() and out_path.stat().st_size > 0:
            print(f"[gen]   scene {idx:02d}: exists, skipping")
            produced.append(out_path)
            if config.CONTINUITY:  # still need this clip's last frame to seed the next one
                if not last_frame.exists():
                    _extract_last_frame(out_path, last_frame)
                prev_last_frame = last_frame
            continue

        seed = prev_last_frame if (config.CONTINUITY and prev_last_frame and prev_last_frame.exists()) else None
        kind = f"continue from scene {idx - 1:02d}" if seed else "text-to-video"
        print(f"[gen]   scene {idx:02d}: generating ({kind})...")
        try:
            backends.generate_clip(scene["veo_prompt"], out_path, seed)
            print(f"[gen]   scene {idx:02d}: saved {out_path.name}")
            produced.append(out_path)
            if config.CONTINUITY:
                _extract_last_frame(out_path, last_frame)
                prev_last_frame = last_frame
        except Exception as e:  # keep going; one bad scene shouldn't lose the batch
            print(f"[gen]   scene {idx:02d}: FAILED — {e}")
            failed.append(idx)
            prev_last_frame = None  # chain broken — next clip starts fresh

    if failed:
        print(f"[gen] {len(failed)} scene(s) failed: {failed}. Re-run to retry just those.")
    return sorted(produced)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Generate video clips for a story")
    ap.add_argument("story_no", type=int)
    args = ap.parse_args()
    generate(args.story_no)
