"""Align each scene's narration excerpt to its spoken time window.

The narration is one continuous voiceover of the full script; the per-scene
`narration_excerpt`s in prompts.json are condensed paraphrases of consecutive
chunks of it. To sync the clips to the voice we need, for each scene, the moment
its line is spoken — not a flat 8s per clip.

Given `narration_words.json` (a list of timed segments: sentence- or word-level,
each {text, start, end}) and the ordered excerpts, we:
  1. explode the script into word tokens, each stamped with a time interpolated
     across its segment,
  2. explode the excerpts into tokens tagged by scene,
  3. run a monotonic subsequence match (difflib) between the two token streams,
  4. read off each scene's start time = earliest script token matched to it,
  5. turn starts into per-scene widths, floor tiny ones, and renormalize so the
     widths sum exactly to the narration length (keeps the end in sync).
"""

from __future__ import annotations

import difflib
import re

_TOK = re.compile(r"[a-z0-9]+")


def _tokens(text: str) -> list[str]:
    return _TOK.findall(text.lower())


def scene_widths(excerpts: list[str], segments: list[dict], total_dur: float,
                 min_width: float = 0.6) -> list[float] | None:
    """Return a per-scene on-screen duration (seconds) aligned to the narration.

    `excerpts` is ordered scene 1..N. Returns None if there's nothing to align
    against (caller should fall back to equal-length clips)."""
    if not segments or not excerpts:
        return None

    # 1. script tokens with interpolated per-word times
    script_tok: list[str] = []
    tok_time: list[float] = []
    for seg in segments:
        toks = _tokens(seg["text"])
        span = seg["end"] - seg["start"]
        for k, t in enumerate(toks):
            script_tok.append(t)
            tok_time.append(seg["start"] + (k / max(len(toks), 1)) * span)
    if not script_tok:
        return None

    # 2. excerpt tokens tagged by scene index
    ex_tok: list[str] = []
    ex_scene: list[int] = []
    for idx, ex in enumerate(excerpts):
        for t in _tokens(ex):
            ex_tok.append(t)
            ex_scene.append(idx)

    # 3. monotonic match; 4. earliest matched script token per scene
    sm = difflib.SequenceMatcher(a=ex_tok, b=script_tok, autojunk=False)
    start_j: list[int | None] = [None] * len(excerpts)
    for i, j, n in sm.get_matching_blocks():
        for k in range(n):
            sc = ex_scene[i + k]
            if start_j[sc] is None or (j + k) < start_j[sc]:
                start_j[sc] = j + k

    # starts -> monotonic non-decreasing times; unmatched scenes inherit previous
    starts: list[float] = []
    last = 0.0
    for sc in range(len(excerpts)):
        j = start_j[sc]
        t = tok_time[j] if j is not None else last
        t = max(t, last)
        starts.append(t)
        last = t
    starts[0] = 0.0

    # 5. widths, floor, renormalize to the true narration length
    widths = [
        (starts[sc + 1] if sc + 1 < len(starts) else total_dur) - starts[sc]
        for sc in range(len(starts))
    ]
    widths = [max(w, min_width) for w in widths]
    scale = total_dur / sum(widths)
    return [w * scale for w in widths]
