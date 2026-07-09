"""Central config + small helpers for the YouTube Shorts pipeline.

Every path here is derived from this file's location, so the whole
`shorts_pipeline/` folder is portable — move it and nothing breaks.
"""

from __future__ import annotations

import csv
import os
import subprocess
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PIPELINE_DIR = Path(__file__).resolve().parent          # .../yt_reddit_horror/shorts_pipeline
PROJECT_DIR = PIPELINE_DIR.parent                        # .../yt_reddit_horror
CSV_PATH = PROJECT_DIR / "yt_reddit_stories.csv"         # 25 stories (No, Video Title, ... Modified Script)
BGM_PATH = PROJECT_DIR / "bgm_horror.mp3"                # suspenseful music bed (reused for every story)
STORIES_DIR = PIPELINE_DIR / "stories"                   # per-story output folders live here

# Load API keys from a local .env (never committed — see .gitignore). Checks the
# project root and this pipeline folder; real environment variables always win.
try:
    from dotenv import load_dotenv

    for _env in (PROJECT_DIR / ".env", PIPELINE_DIR / ".env"):
        load_dotenv(_env)
except ModuleNotFoundError:
    pass

# A blank ANTHROPIC_API_KEY / ANTHROPIC_AUTH_TOKEN still "wins" the SDK's auth
# precedence and shadows an `ant auth login` OAuth profile. Drop empties so you
# can authenticate Claude via OAuth (no key) instead. (GEMINI_API_KEY must be a
# real key — Veo has no OAuth path.)
for _k in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN"):
    if not os.environ.get(_k, "").strip():
        os.environ.pop(_k, None)

# ---------------------------------------------------------------------------
# Narration (edge-tts) — same voice as the existing story-1 pipeline
# ---------------------------------------------------------------------------
TTS_VOICE = "en-US-GuyNeural"
TTS_RATE = "-8%"

# ---------------------------------------------------------------------------
# Prompt splitting (Claude / Anthropic API)
# ---------------------------------------------------------------------------
# Reads ANTHROPIC_API_KEY from the environment.
CLAUDE_MODEL = "claude-opus-4-8"

# ---------------------------------------------------------------------------
# Backend selection — which service generates the clips (see backends.py)
#   VIDEO_BACKEND=gemini  -> Google Veo (default; needs GEMINI_API_KEY)
#   VIDEO_BACKEND=fal     -> fal.ai hosted open models (needs FAL_KEY; $10 free on signup)
# ---------------------------------------------------------------------------
VIDEO_BACKEND = (os.environ.get("VIDEO_BACKEND") or "gemini").strip().lower()

# fal.ai settings (used when VIDEO_BACKEND=fal). Reads FAL_KEY from the environment.
# Text-to-video model. Override with FAL_MODEL. Kling is a solid, credit-cheap default;
# swap to an open model like "fal-ai/wan/v2.2-a14b/text-to-video" or an LTX id if preferred.
FAL_MODEL = os.environ.get("FAL_MODEL") or "fal-ai/kling-video/v1.6/standard/text-to-video"
# Optional image-to-video model for continuity (leave empty to disable on fal).
FAL_I2V_MODEL = os.environ.get("FAL_I2V_MODEL") or ""
# Seconds per clip (model-dependent; Kling accepts "5" or "10").
FAL_DURATION = os.environ.get("FAL_DURATION") or "5"

# ---------------------------------------------------------------------------
# Video generation (Google Veo 3 via the Gemini API)
# ---------------------------------------------------------------------------
# Reads GEMINI_API_KEY from the environment.
#
# Model IDs vary by the access your key has. "Fast" tier is the default (≈$0.15/s,
# 720p, ~5x cheaper than Standard). If a generate call 404s on the model name,
# run:  python -c "from google import genai; [print(m.name) for m in genai.Client().models.list()]"
# and pick the veo-*-fast id your key can see, then set it here.
#
# Common alternatives:
#   veo-3.1-fast-generate-preview   (Veo 3.1 Fast — default below)
#   veo-3.1-generate-preview        (Veo 3.1 Standard/Quality — ~$0.40/s)
#   veo-3.0-fast-generate-001       (Veo 3.0 Fast)
#   veo-3.0-generate-001            (Veo 3.0 Standard)
# Override per run with the VEO_MODEL env var, e.g.
#   VEO_MODEL=veo-3.1-lite-generate-preview .venv/bin/python run_story.py 1
VEO_MODEL = os.environ.get("VEO_MODEL") or "veo-3.1-fast-generate-preview"

VEO_ASPECT_RATIO = "9:16"   # vertical, native to Shorts — no cropping needed
VEO_RESOLUTION = "720p"     # Fast tier; bump to "1080p" on the Standard tier
CLIP_SECONDS = 8            # Veo 3 clips are 8s max; the whole short is many clips stitched together

# Shot-to-shot continuity: seed each clip with the previous clip's final frame
# (Veo 3.1 image-to-video), so shots flow into one another instead of cutting to
# unrelated footage. Override per run with CONTINUITY=0 (e.g. the Lite tier may
# not support image-to-video).
CONTINUITY = os.environ.get("CONTINUITY", "1").strip().lower() not in ("0", "false", "no", "")

# Keep baked-in captions, watermarks, and Veo's own dialogue out of the clips —
# we overlay our own narration + music, so the visuals must be clean.
VEO_NEGATIVE_PROMPT = (
    "text, captions, subtitles, watermark, logo, on-screen words, "
    "spoken dialogue, talking, singing, lyrics, "
    "cartoon, low quality, blurry, distorted, warped"
)

# Some tiers (Veo 3.1 Lite) reject `negativePrompt` with a 400. Auto-disable it
# for lite models; override with VEO_NEGATIVE=0/1.
VEO_USE_NEGATIVE_PROMPT = (
    os.environ.get("VEO_NEGATIVE", "0" if "lite" in VEO_MODEL.lower() else "1")
    .strip().lower() not in ("0", "false", "no", "")
)

# ---------------------------------------------------------------------------
# Final render (ffmpeg)
# ---------------------------------------------------------------------------
TARGET_W, TARGET_H = 1080, 1920   # 9:16 1080p output
NARRATION_VOLUME = 1.0
BGM_VOLUME = 0.35                  # music sits under the voiceover

# YouTube Shorts must be <= 3 min. If the assembled cut runs longer, edit_short
# speeds the whole thing up — video + audio in sync, voice pitch preserved (via
# atempo) — to land SHORTS_SAFETY_MARGIN seconds under this cap. Nothing is cut,
# so every scene stays in. Set SHORTS_MAX_SECONDS=0 to disable and keep full length.
SHORTS_MAX_SECONDS = float(os.environ.get("SHORTS_MAX_SECONDS") or 180)
SHORTS_SAFETY_MARGIN = 4.0        # land this many seconds under the cap


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def story_dir(story_no: int) -> Path:
    """Output folder for a story. The folder name IS the story number."""
    d = STORIES_DIR / str(story_no)
    d.mkdir(parents=True, exist_ok=True)
    return d


def read_story(story_no: int) -> dict[str, str]:
    """Return the CSV row for a story number (1-indexed, matching the 'No' column)."""
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if int(row["No"]) == story_no:
                return row
    raise ValueError(f"Story #{story_no} not found in {CSV_PATH}")


def audio_duration_seconds(path: Path) -> float:
    """Return the duration of an audio/video file in seconds via ffprobe."""
    out = subprocess.check_output(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        text=True,
    )
    return float(out.strip())


def shorts_speedup(content_seconds: float) -> float:
    """Speed factor (>= 1.0) to bring a `content_seconds`-long cut safely under
    the Shorts cap. Returns 1.0 (no change) when it already fits or when
    SHORTS_MAX_SECONDS is 0/disabled — never slows a short clip down."""
    if SHORTS_MAX_SECONDS <= 0:
        return 1.0
    target = SHORTS_MAX_SECONDS - SHORTS_SAFETY_MARGIN
    speed = content_seconds / target
    return speed if speed > 1.0 else 1.0


def atempo_chain(speed: float) -> str:
    """ffmpeg `atempo` filter string for an arbitrary speed. One atempo instance
    handles 0.5–2.0; chain instances for larger factors (pitch is preserved)."""
    parts, s = [], speed
    while s > 2.0:
        parts.append("atempo=2.0")
        s /= 2.0
    parts.append(f"atempo={s:.6f}")
    return ",".join(parts)
