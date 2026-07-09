"""Step 2 — split a story into cinematic Veo 3 scene prompts using Claude.

Given a story and a target number of scenes (derived from narration length,
one ~8s Veo clip per scene), Claude breaks the script into sequential visual
beats and writes a detailed vertical-horror prompt for each.

Output: stories/<n>/prompts.json  (you can hand-edit this before generating).

Uses the Anthropic Python SDK, model claude-opus-4-8, adaptive thinking, and
structured outputs so the result is always valid JSON.

Claude auth (either works, no key needed for the first):
  - OAuth:  run `ant auth login` once (Anthropic CLI) — keyless.
  - API key: set ANTHROPIC_API_KEY (env or shorts_pipeline/.env).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import anthropic
from pydantic import BaseModel

import config


class Scene(BaseModel):
    index: int
    narration_excerpt: str   # the slice of script this shot covers (for your reference)
    veo_prompt: str          # the full cinematic prompt sent to Veo 3


class SceneList(BaseModel):
    scenes: list[Scene]


SYSTEM_PROMPT = """\
You are a cinematic prompt engineer for Google Veo 3. You turn a narrated Reddit
horror story into a sequence of standalone ~8 second vertical video shots that,
played in order, act as atmospheric b-roll under the narration.

Hard rules for every veo_prompt you write:
- Vertical 9:16 framing, shot for a phone screen.
- Photoreal, cinematic horror: dim / low-key lighting, deep shadows, subtle film
  grain, slow deliberate camera movement (push-in, slow pan, handheld drift).
- NO on-screen text, captions, subtitles, watermarks, logos, or UI.
- NO spoken dialogue, singing, or lip-synced talking — the audio is replaced, so
  characters must not appear to be speaking to camera.
- Each shot is self-contained and about 8 seconds long. Describe subject, setting,
  action, camera move, lighting, and mood concretely (not the plot).
- Maintain visual continuity across shots: keep recurring characters, locations,
  and props looking consistent from scene to scene. Each shot is generated
  starting from the final frame of the previous shot, so write prompts that flow
  naturally onward — continue the same space/subject and describe where the camera
  or action moves next, rather than jumping to an unrelated scene.
- Build dread progressively toward the story's climax.

Return EXACTLY the requested number of scenes, in narrative order, together
covering the whole script from hook to final beat."""


def _build_user_prompt(row: dict[str, str], num_scenes: int) -> str:
    return (
        f"TITLE: {row['Video Title']}\n\n"
        f"FULL NARRATION SCRIPT:\n{row['Modified Script']}\n\n"
        f"Split this into EXACTLY {num_scenes} sequential shots. For each shot give: "
        f"index (1..{num_scenes}), the narration_excerpt it visually covers, and a "
        f"detailed veo_prompt following all the rules."
    )


def split(story_no: int, num_scenes: int) -> Path:
    """Generate prompts.json for a story. Returns its path."""
    row = config.read_story(story_no)
    out_dir = config.story_dir(story_no)
    out_path = out_dir / "prompts.json"

    print(f"[split] story #{story_no} -> {num_scenes} scene prompts via {config.CLAUDE_MODEL}")
    client = anthropic.Anthropic()  # uses ANTHROPIC_API_KEY, or an `ant auth login` OAuth profile
    try:
        response = client.messages.parse(
            model=config.CLAUDE_MODEL,
            max_tokens=16000,
            thinking={"type": "adaptive"},
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": _build_user_prompt(row, num_scenes)}],
            output_format=SceneList,
        )
    except anthropic.AuthenticationError as e:
        raise SystemExit(
            "Claude auth failed. Either run `ant auth login` (keyless OAuth) or set "
            "ANTHROPIC_API_KEY in shorts_pipeline/.env.\n"
            f"  underlying error: {e}"
        )
    result = response.parsed_output
    if result is None:
        raise RuntimeError(f"Claude did not return a valid scene list (stop_reason={response.stop_reason})")

    payload = {
        "story_no": story_no,
        "title": row["Video Title"],
        "num_scenes": len(result.scenes),
        "scenes": [s.model_dump() for s in result.scenes],
    }
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[split] wrote {len(result.scenes)} prompts to {out_path}")
    return out_path


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Split a story into Veo scene prompts")
    ap.add_argument("story_no", type=int)
    ap.add_argument("num_scenes", type=int, help="How many ~8s shots to produce")
    args = ap.parse_args()
    split(args.story_no, args.num_scenes)
