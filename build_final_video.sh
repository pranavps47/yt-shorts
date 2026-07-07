#!/bin/bash
# Build the final 16:9 1080p horror video for story #1.
# v2: narration sped to 1.3x → 2:24 total. Scenes rebuilt at 0.713× durations.
# BGM gets a midrange layer so it's audible on small speakers, mixed at 0.55.
set -euo pipefail

SRC="$HOME/Downloads/yt_broll"
DST="/Users/satyapranav/PycharmProjects/yt_reddit_horror"
SCENES="$DST/scenes"
NARRATION="$DST/story1_narration.mp3"
BGM="$DST/bgm_horror.mp3"
FINAL="$DST/story1_final.mp4"

mkdir -p "$SCENES"

SCALE_PAD="scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black"
ENC="-r 30 -c:v libx264 -pix_fmt yuv420p -preset veryfast -crf 22 -an -y"

echo "=== Scene 1: trim 10s → 5.7s ==="
ffmpeg -i "$SRC/01_hook.mp4" -t 5.7 -vf "$SCALE_PAD" $ENC "$SCENES/01.mp4" 2>&1 | tail -1

echo "=== Scene 2: trim 13s → 14.3s (slow PTS*1.10) ==="
ffmpeg -i "$SRC/02_apartment.mp4" -vf "setpts=PTS*1.10,$SCALE_PAD" $ENC "$SCENES/02.mp4" 2>&1 | tail -1

echo "=== Scene 3: trim 13.5s → 9.3s ==="
ffmpeg -i "$SRC/03_coming_home.mp4" -t 9.3 -vf "$SCALE_PAD" $ENC "$SCENES/03.mp4" 2>&1 | tail -1

echo "=== Scene 4: trim 26.5s → 12.1s ==="
ffmpeg -i "$SRC/04_white_door.mp4" -t 12.1 -vf "$SCALE_PAD" $ENC "$SCENES/04.mp4" 2>&1 | tail -1

echo "=== Scene 5: trim 47.5s → 8.6s ==="
ffmpeg -i "$SRC/05_staring.mp4" -t 8.6 -vf "$SCALE_PAD" $ENC "$SCENES/05.mp4" 2>&1 | tail -1

echo "=== Scene 6: slow 10.2s → 10.7s (PTS*1.05) ==="
ffmpeg -i "$SRC/06_measuring.mp4" -vf "setpts=PTS*1.05,$SCALE_PAD" $ENC "$SCENES/06.mp4" 2>&1 | tail -1

echo "=== Scene 7: loop 7.4s → 19.3s ==="
ffmpeg -stream_loop -1 -i "$SRC/07_keys.mp4" -t 19.3 -vf "$SCALE_PAD" $ENC "$SCENES/07.mp4" 2>&1 | tail -1

echo "=== Scene 8: trim 9.1s → 7.8s ==="
ffmpeg -i "$SRC/08_phone_calls.mp4" -t 7.8 -vf "$SCALE_PAD" $ENC "$SCENES/08.mp4" 2>&1 | tail -1

echo "=== Scene 9: loop 4.2s → 14.3s ==="
ffmpeg -stream_loop -1 -i "$SRC/09_neighbor.mp4" -t 14.3 -vf "$SCALE_PAD" $ENC "$SCENES/09.mp4" 2>&1 | tail -1

echo "=== Scene 10: trim 54.6s → 17.8s ==="
ffmpeg -i "$SRC/10_barricade.mp4" -t 17.8 -vf "$SCALE_PAD" $ENC "$SCENES/10.mp4" 2>&1 | tail -1

echo "=== Scene 11: trim 14.5s → 12.8s ==="
ffmpeg -i "$SRC/11_reddit.mp4" -t 12.8 -vf "$SCALE_PAD" $ENC "$SCENES/11.mp4" 2>&1 | tail -1

echo "=== Scene 12: loop 3.8s → 11.4s ==="
ffmpeg -stream_loop -1 -i "$SRC/12_outro.mp4" -t 11.4 -vf "$SCALE_PAD" $ENC "$SCENES/12.mp4" 2>&1 | tail -1

echo "=== Concat list ==="
> "$SCENES/concat.txt"
for n in 01 02 03 04 05 06 07 08 09 10 11 12; do
    echo "file '$SCENES/$n.mp4'" >> "$SCENES/concat.txt"
done

echo "=== Concatenating ==="
ffmpeg -f concat -safe 0 -i "$SCENES/concat.txt" -c copy -y "$SCENES/all_video.mp4" 2>&1 | tail -1

echo "=== Final mix: video + narration + BGM (BGM at 0.55) ==="
ffmpeg -i "$SCENES/all_video.mp4" -i "$NARRATION" -i "$BGM" \
  -filter_complex "[1:a]volume=1.0[narr];[2:a]volume=0.55[bgm];[narr][bgm]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[aout]" \
  -map 0:v -map "[aout]" -c:v copy -c:a aac -b:a 192k -shortest -y "$FINAL" 2>&1 | tail -1

echo ""
echo "=== DONE ==="
ls -la "$FINAL"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$FINAL"
