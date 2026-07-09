"""Pluggable clip-generation backends.

Select with the VIDEO_BACKEND env var (see config.py):
  gemini  -> Google Veo via the Gemini API   (default; needs GEMINI_API_KEY)
  fal     -> fal.ai hosted open models        (needs FAL_KEY; $10 free credits on signup)
             e.g. Kling / Wan 2.2 / LTX-Video, chosen via FAL_MODEL.

Every backend exposes the same call:
    generate_clip(prompt, out_path, image_path)
`image_path` is the previous clip's final frame for continuity, or None for
plain text-to-video.
"""

from __future__ import annotations

import time
import urllib.request
from pathlib import Path

import config

_POLL_SECONDS = 15


def generate_clip(prompt: str, out_path: Path, image_path: Path | None) -> None:
    if config.VIDEO_BACKEND == "gemini":
        _gemini(prompt, out_path, image_path)
    elif config.VIDEO_BACKEND == "fal":
        _fal(prompt, out_path, image_path)
    else:
        raise ValueError(f"Unknown VIDEO_BACKEND {config.VIDEO_BACKEND!r} (use 'gemini' or 'fal')")


# --------------------------------------------------------------------------- #
# Google Veo (Gemini API)
# --------------------------------------------------------------------------- #
def _gemini(prompt: str, out_path: Path, image_path: Path | None) -> None:
    from google import genai
    from google.genai import types

    client = genai.Client()  # reads GEMINI_API_KEY
    cfg_kwargs: dict = dict(
        aspect_ratio=config.VEO_ASPECT_RATIO,
        resolution=config.VEO_RESOLUTION,
        number_of_videos=1,
    )
    if config.VEO_USE_NEGATIVE_PROMPT:
        cfg_kwargs["negative_prompt"] = config.VEO_NEGATIVE_PROMPT
    kwargs: dict = {
        "model": config.VEO_MODEL,
        "prompt": prompt,
        "config": types.GenerateVideosConfig(**cfg_kwargs),
    }
    if image_path is not None:  # image-to-video (continuity)
        kwargs["image"] = types.Image(image_bytes=image_path.read_bytes(), mime_type="image/png")

    op = client.models.generate_videos(**kwargs)
    while not op.done:
        time.sleep(_POLL_SECONDS)
        op = client.operations.get(op)
    gen = op.response.generated_videos[0]
    client.files.download(file=gen.video)
    gen.video.save(str(out_path))


# --------------------------------------------------------------------------- #
# fal.ai (hosted open models — Kling / Wan / LTX / …)
# --------------------------------------------------------------------------- #
def _fal(prompt: str, out_path: Path, image_path: Path | None) -> None:
    import fal_client  # pip install fal-client ; reads FAL_KEY

    args: dict = {
        "prompt": prompt,
        "aspect_ratio": config.VEO_ASPECT_RATIO,
        "duration": config.FAL_DURATION,
    }
    model = config.FAL_MODEL
    # Continuity: only if an image-to-video model is configured (many fal t2v
    # models don't accept an image). Otherwise fall back to text-to-video.
    if image_path is not None and config.FAL_I2V_MODEL:
        args["image_url"] = fal_client.upload_file(str(image_path))
        model = config.FAL_I2V_MODEL

    result = fal_client.subscribe(model, arguments=args)
    urllib.request.urlretrieve(_video_url(result), str(out_path))


def _video_url(result) -> str:
    """fal result shapes vary by model — dig out the output video URL."""
    if isinstance(result, dict):
        v = result.get("video")
        if isinstance(v, dict) and v.get("url"):
            return v["url"]
        if isinstance(v, str) and v:
            return v
        vids = result.get("videos")
        if vids:
            first = vids[0]
            return first["url"] if isinstance(first, dict) else first
        if result.get("url"):
            return result["url"]
    raise RuntimeError(f"Could not find an output video URL in the fal result: {result}")
