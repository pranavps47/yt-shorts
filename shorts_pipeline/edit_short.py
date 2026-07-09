"""Step 4 — assemble the final 9:16 Short with ffmpeg.

Takes the generated clips + narration + background music and produces:
    stories/<n>/<n>_final_vertical.mp4

Pipeline:
  1. Normalize every clip to 1080x1920, 30fps, no audio (Veo's audio is dropped).
  2. Concatenate the clips in order.
  3. Mix narration (full volume) with looped background music (ducked), and cut
     the final video to the narration's length.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

import config

# Cover-scale to fill 1080x1920 then centre-crop (clips are already 9:16, so this
# just standardizes resolution/fps across clips before concat).
COVER_CROP = f"scale={config.TARGET_W}:{config.TARGET_H}:force_original_aspect_ratio=increase,crop={config.TARGET_W}:{config.TARGET_H}"
ENC = ["-r", "30", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "veryfast", "-crf", "22", "-an", "-y"]


def _run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def edit(story_no: int) -> Path:
    out_dir = config.story_dir(story_no)
    clips_dir = out_dir / "clips"
    narration = out_dir / "narration.mp3"
    final = out_dir / f"{story_no}_final_vertical.mp4"

    clips = sorted(clips_dir.glob("*.mp4"))
    if not clips:
        raise FileNotFoundError(f"No clips in {clips_dir} — run generate_veo_clips first")
    if not narration.exists():
        raise FileNotFoundError(f"{narration} missing — run generate_voiceover first")
    if not config.BGM_PATH.exists():
        raise FileNotFoundError(f"Background music not found at {config.BGM_PATH}")

    norm_dir = out_dir / "clips_norm"
    norm_dir.mkdir(exist_ok=True)

    print(f"[edit] story #{story_no}: normalizing {len(clips)} clips to "
          f"{config.TARGET_W}x{config.TARGET_H}")
    norm_clips: list[Path] = []
    for clip in clips:
        norm = norm_dir / clip.name
        _run(["ffmpeg", "-i", str(clip), "-vf", COVER_CROP, *ENC, str(norm)])
        norm_clips.append(norm)

    # Concatenate normalized clips (all share codec/params → stream copy).
    concat_txt = norm_dir / "concat.txt"
    concat_txt.write_text("".join(f"file '{c}'\n" for c in norm_clips), encoding="utf-8")
    all_video = norm_dir / "all_video.mp4"
    _run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", str(concat_txt), "-c", "copy", "-y", str(all_video)])

    # After -shortest the cut runs min(video, narration). If that's over the
    # Shorts cap, speed the whole thing up (video + audio in sync) so it fits —
    # no scene is dropped. Voice pitch is preserved via atempo.
    content_dur = min(config.audio_duration_seconds(all_video),
                      config.audio_duration_seconds(narration))
    speed = config.shorts_speedup(content_dur)

    # Mix narration (full) + looped BGM (ducked); cut final to the narration length.
    print(f"[edit] mixing narration + music -> {final.name}")
    audio_mix = (
        f"[1:a]volume={config.NARRATION_VOLUME}[narr];"
        f"[2:a]volume={config.BGM_VOLUME}[bgm];"
        f"[narr][bgm]amix=inputs=2:duration=first:normalize=0[mix]"
    )
    if speed > 1.0:
        print(f"[edit]   {content_dur:.1f}s > {config.SHORTS_MAX_SECONDS:.0f}s cap "
              f"-> speeding {speed:.3f}x to ~{content_dur / speed:.1f}s")
        filter_complex = (f"[0:v]setpts=PTS/{speed:.6f}[v];"
                          f"{audio_mix};[mix]{config.atempo_chain(speed)}[aout]")
        vcodec, vmap = ["-c:v", "libx264", "-pix_fmt", "yuv420p",
                        "-preset", "veryfast", "-crf", "20"], "[v]"
    else:
        filter_complex = f"{audio_mix};[mix]anull[aout]"
        vcodec, vmap = ["-c:v", "copy"], "0:v"
    _run([
        "ffmpeg",
        "-i", str(all_video),
        "-i", str(narration),
        "-stream_loop", "-1", "-i", str(config.BGM_PATH),
        "-filter_complex", filter_complex,
        "-map", vmap, "-map", "[aout]",
        *vcodec, "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        "-shortest", "-y", str(final),
    ])

    dur = config.audio_duration_seconds(final)
    print(f"[edit] done: {final} ({dur:.1f}s, {config.TARGET_W}x{config.TARGET_H})")
    return final


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Assemble the final vertical Short")
    ap.add_argument("story_no", type=int)
    args = ap.parse_args()
    edit(args.story_no)
