# Shorts Pipeline — Reddit Horror → YouTube Shorts (Veo 3)

Turns each story in `../yt_reddit_stories.csv` into a **9:16 vertical YouTube Short**:
AI-generated Veo 3 b-roll, cut to a synthesized background voiceover with a
suspenseful music bed. Everything for a story lands in one folder named after the
story number (`stories/1/`, `stories/2/`, …).

This document is the plan of record. It captures the decisions we locked in, the
architecture, cost, and how to run it.

---

## Decisions (locked)

| Question | Decision |
|----------|----------|
| Aspect ratio | **9:16 vertical, 1080×1920** (Veo 3 renders 9:16 natively — no cropping) |
| Video model | **Google Veo 3.1 — Fast tier** (720p, ≈ $0.15/s, ~5× cheaper than Standard) |
| Veo access | **Gemini API key** (`GEMINI_API_KEY`), via the `google-genai` SDK |
| Prompt splitting | **Claude API** (`claude-opus-4-8`) turns each script into cinematic scene prompts |
| First run scope | **Story 1 only**, then review, then batch the rest |
| Voiceover | `edge-tts`, `en-US-GuyNeural` @ `-8%` — narrates the CSV **"Modified Script"** (same as the original story-1 pipeline) |
| Music | the existing `../bgm_horror.mp3`, ducked under the voiceover |
| Veo native audio | **muted** — we overlay our own narration + music |
| Shot continuity | **on** — each clip is seeded with the previous clip's last frame (Veo 3.1 image-to-video) so shots flow into each other |

---

## Pipeline

Each ~3-minute story needs ~18–23 clips (Veo 3 clips are **8 s** max). Per story,
in order:

```
1. voiceover  edge-tts   ->  stories/<n>/narration.mp3 (+ .srt)
                             (its length decides the clip count: ceil(duration / 8s))
2. split      Claude      ->  stories/<n>/prompts.json      (N cinematic 9:16 prompts)
3. veo        Veo 3       ->  stories/<n>/clips/NN.mp4       (one 8s clip per prompt)
4. edit       ffmpeg      ->  stories/<n>/<n>_final_vertical.mp4
```

Voiceover runs **first** so the exact narration length sizes the scene count, and
so the final video can be cut precisely to the narration.

---

## Files

| File | Role |
|------|------|
| `config.py` | All paths, model IDs, tier settings, and small helpers (CSV reader, ffprobe duration). Portable — derives everything from its own location. |
| `generate_voiceover.py` | Step 1 — edge-tts narration + subtitle track. |
| `split_story_prompts.py` | Step 2 — Claude splits the script into `prompts.json` (structured output, hand-editable before you generate). |
| `generate_veo_clips.py` | Step 3 — one Veo 3 clip per prompt; async polling, resumable, skips existing clips, survives individual failures. |
| `edit_short.py` | Step 4 — normalize clips → concat → mix narration + looped BGM → final Short. |
| `run_story.py` | Orchestrator — runs all 4 steps for one/several/all stories. |
| `requirements.txt` | Python deps (ffmpeg is a system dependency). |
| `stories/<n>/` | Per-story output folder (created at runtime). |

---

## Prerequisites

```bash
pip install -r requirements.txt          # anthropic, google-genai, edge-tts, pydantic, python-dotenv
# ffmpeg + ffprobe must be on PATH (brew install ffmpeg)

cp .env.example .env                      # then edit .env and paste in your keys
#   GEMINI_API_KEY=...   Veo 3 (Gemini API)
#   ANTHROPIC_API_KEY=... Claude (prompt splitting)
```

`.env` is loaded automatically (via `python-dotenv`) and is **gitignored** — it is
never committed. Real environment variables, if set, take precedence over `.env`.

> **Veo model ID.** `config.VEO_MODEL` defaults to `veo-3.1-fast-generate-preview`.
> If a generate call 404s, list what your key can see and pick the matching
> `veo-*-fast` id:
> ```bash
> python -c "from google import genai; [print(m.name) for m in genai.Client().models.list()]"
> ```
> Alternatives are listed in `config.py`.

---

## Usage

```bash
# Build story 1 end-to-end (default scope), then review stories/1/1_final_vertical.mp4
python run_story.py

# A specific subset
python run_story.py 1 2 3

# All 25 (large Veo bill — see Cost)
python run_story.py --all

# Re-run only some steps (outputs are resumable / skippable)
python run_story.py 1 --skip voiceover split     # regenerate clips + re-edit only
```

You can hand-tune `stories/<n>/prompts.json` after step 2 and re-run with
`--skip voiceover split` to regenerate clips from your edited prompts.

Individual steps also run standalone, e.g.:
```bash
python generate_voiceover.py 1
python split_story_prompts.py 1 20
python generate_veo_clips.py 1
python edit_short.py 1
```

---

## Cost (why we start with story 1)

Veo 3 is metered per second. A ~3-minute story ≈ 180 s of generated video:

| Tier | Rate | Per story | All 25 |
|------|------|-----------|--------|
| **Fast (chosen)** | ≈ $0.15/s | **≈ $27** | ≈ $675 |
| Standard / Quality | ≈ $0.40/s | ≈ $72 | ≈ $1,800 |
| Lite / no-audio | ≈ $0.05/s | ≈ $9 | ≈ $225 |

Claude prompt-splitting and edge-tts are negligible by comparison. This is why the
default run is **story 1 only** — confirm quality and spend, then `--all`.

---

## Output layout

```
stories/
└── 1/
    ├── narration.mp3
    ├── narration.srt
    ├── prompts.json
    ├── clips/            01.mp4 … NN.mp4     (raw Veo clips)
    ├── clips_norm/       normalized + concat intermediate
    └── 1_final_vertical.mp4                  ← the finished Short
```

---

## Notes & next steps

- **Continuity** is enabled by default (`config.CONTINUITY = True`): the first clip
  is text-to-video, and every later clip is generated image-to-video from the
  previous clip's final frame, so shots flow into one another. If a clip fails, the
  chain resets and the next clip starts fresh. The split prompt also tells Claude to
  write shots that continue the same space/subject. Set `CONTINUITY = False` for
  independent b-roll shots (each generated on its own).
- **Captions:** `narration.srt` is produced per story. Upload it in YouTube Studio,
  or burn captions in a later ffmpeg pass if you want them on-screen.
- **Batching:** once story 1 looks right, run `python run_story.py --all` (mind the
  Veo bill) or feed a subset.
- **Tuning:** clip count (`CLIP_SECONDS`), music level (`BGM_VOLUME`), voice
  (`TTS_VOICE`/`TTS_RATE`), and Veo tier/resolution all live in `config.py`.
