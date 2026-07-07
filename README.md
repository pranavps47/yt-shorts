# yt_reddit_horror

Pipeline for turning AI-composed Reddit-style horror stories into narrated
YouTube videos (both 16:9 landscape and 9:16 vertical/Shorts).

## Contents

| Path | What it is |
|------|-----------|
| `build_yt_reddit_csv.py` | Generates the story dataset. 25 sub-5-min creepy stories written in the voice of r/nosleep, r/LetsNotMeet, r/shortscarystories, etc. |
| `yt_reddit_stories.csv` | The generated dataset. Columns: `No, Video Title, Video Description, Content, Modified Script`. |
| `generate_narration.py` | Reads story #1 from the CSV and synthesizes narration with `edge-tts` (voice `en-US-GuyNeural`, rate `-8%`). |
| `story1_script.txt` | The narration script for story #1. |
| `story1_production_guide.md` | Scene-by-scene production notes for story #1. |
| `story1_narration.mp3` / `.srt` | Synthesized narration audio + subtitle/timing track. |
| `bgm_horror.mp3` | Background music bed mixed under the narration. |
| `build_final_video.sh` | Builds the 16:9 1080p video: trims/scales b-roll into `scenes/`, concats, overlays narration + BGM → `story1_final.mp4`. |
| `build_vertical_video.sh` | Vertical 9:16 variant → `scenes_vertical/` → `story1_final_vertical.mp4`. |
| `scenes/`, `scenes_vertical/` | Per-scene clips + `concat.txt` + `all_video.mp4` intermediate. |
| `story1_final.mp4` / `story1_final_vertical.mp4` | Final rendered videos. |

## Pipeline

```
build_yt_reddit_csv.py  ──▶  yt_reddit_stories.csv
                                     │
generate_narration.py  ──▶  story1_narration.mp3 + .srt
                                     │
build_final_video.sh  ─────▶  story1_final.mp4          (16:9)
build_vertical_video.sh  ──▶  story1_final_vertical.mp4  (9:16)
```

## Requirements

- Python 3 with `edge-tts` (`pip install edge-tts`) for narration.
- `ffmpeg` on `PATH` for the video build scripts.
- Source b-roll clips in `~/Downloads/yt_broll/` (referenced by the build
  scripts as `$SRC`; not bundled here).

## Usage

```bash
python3 build_yt_reddit_csv.py      # regenerate the CSV
python3 generate_narration.py       # regenerate story #1 narration
./build_final_video.sh              # render 16:9
./build_vertical_video.sh           # render 9:16
```

> Note: the build scripts and `scenes/concat.txt` use absolute paths pointing
> at this project directory. If you move the project, update those paths.

## Shorts pipeline (per-story automation)

`shorts_pipeline/` automates the whole thing for **every** story in the CSV: it
generates 9:16 vertical YouTube Shorts with **Google Veo 3** b-roll, an `edge-tts`
voiceover, and the `bgm_horror.mp3` music bed. Each story's output lands in a
folder named after its number (`shorts_pipeline/stories/1/…`).

Pipeline per story: voiceover (edge-tts) → split into scene prompts (Claude) →
generate clips (Veo 3 Fast) → assemble (ffmpeg). See
[`shorts_pipeline/README.md`](shorts_pipeline/README.md) for the full plan,
prerequisites, cost, and usage. Quick start:

```bash
cd shorts_pipeline
pip install -r requirements.txt          # + ffmpeg on PATH
cp .env.example .env                       # then paste your GEMINI_API_KEY + ANTHROPIC_API_KEY
python run_story.py                        # builds story 1 (with shot-to-shot continuity) to review first
```
