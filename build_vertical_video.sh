#!/bin/bash
# Build the 9:16 vertical (Shorts/mobile) version of story #1.
# Uses center-crop ("cover" scaling) so horizontal source clips fill 1080x1920
# without black bars — loses some side content but feels native to mobile.
set -euo pipefail

SRC="$HOME/Downloads/yt_broll"
DST="/Users/satyapranav/PycharmProjects/yt_reddit_horror"
SCENES_V="$DST/scenes_vertical"
NARRATION="$DST/story1_narration.mp3"
BGM="$DST/bgm_horror.mp3"
FINAL="$DST/story1_final_vertical.mp4"

mkdir -p "$SCENES_V"

# Scale to cover 1080x1920, then crop center → vertical without black bars.
COVER_CROP="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920"
ENC="-r 30 -c:v libx264 -pix_fmt yuv420p -preset veryfast -crf 22 -an -y"

echo "=== Scene 1: trim 10s → 5.7s [9:16] ==="
ffmpeg -i "$SRC/01_hook.mp4" -t 5.7 -vf "$COVER_CROP" $ENC "$SCENES_V/01.mp4" 2>&1 | tail -1

echo "=== Scene 2: slow 13s → 14.3s [9:16] ==="
ffmpeg -i "$SRC/02_apartment.mp4" -vf "setpts=PTS*1.10,$COVER_CROP" $ENC "$SCENES_V/02.mp4" 2>&1 | tail -1

echo "=== Scene 3: trim 13.5s → 9.3s [9:16] ==="
ffmpeg -i "$SRC/03_coming_home.mp4" -t 9.3 -vf "$COVER_CROP" $ENC "$SCENES_V/03.mp4" 2>&1 | tail -1

echo "=== Scene 4: trim 26.5s → 12.1s [9:16] ==="
ffmpeg -i "$SRC/04_white_door.mp4" -t 12.1 -vf "$COVER_CROP" $ENC "$SCENES_V/04.mp4" 2>&1 | tail -1

echo "=== Scene 5: trim 47.5s → 8.6s [9:16] ==="
ffmpeg -i "$SRC/05_staring.mp4" -t 8.6 -vf "$COVER_CROP" $ENC "$SCENES_V/05.mp4" 2>&1 | tail -1

echo "=== Scene 6: slow 10.2s → 10.7s [9:16] ==="
ffmpeg -i "$SRC/06_measuring.mp4" -vf "setpts=PTS*1.05,$COVER_CROP" $ENC "$SCENES_V/06.mp4" 2>&1 | tail -1

echo "=== Scene 7: loop 7.4s → 19.3s [9:16] ==="
ffmpeg -stream_loop -1 -i "$SRC/07_keys.mp4" -t 19.3 -vf "$COVER_CROP" $ENC "$SCENES_V/07.mp4" 2>&1 | tail -1

echo "=== Scene 8: trim 9.1s → 7.8s [9:16] ==="
ffmpeg -i "$SRC/08_phone_calls.mp4" -t 7.8 -vf "$COVER_CROP" $ENC "$SCENES_V/08.mp4" 2>&1 | tail -1

echo "=== Scene 9: loop 4.2s → 14.3s [9:16] ==="
ffmpeg -stream_loop -1 -i "$SRC/09_neighbor.mp4" -t 14.3 -vf "$COVER_CROP" $ENC "$SCENES_V/09.mp4" 2>&1 | tail -1

echo "=== Scene 10: trim 54.6s → 17.8s [9:16] ==="
ffmpeg -i "$SRC/10_barricade.mp4" -t 17.8 -vf "$COVER_CROP" $ENC "$SCENES_V/10.mp4" 2>&1 | tail -1

echo "=== Scene 11: trim 14.5s → 12.8s [9:16] ==="
ffmpeg -i "$SRC/11_reddit.mp4" -t 12.8 -vf "$COVER_CROP" $ENC "$SCENES_V/11.mp4" 2>&1 | tail -1

echo "=== Scene 12: loop 3.8s → 11.4s [9:16] ==="
ffmpeg -stream_loop -1 -i "$SRC/12_outro.mp4" -t 11.4 -vf "$COVER_CROP" $ENC "$SCENES_V/12.mp4" 2>&1 | tail -1

echo "=== Concat list ==="
> "$SCENES_V/concat.txt"
for n in 01 02 03 04 05 06 07 08 09 10 11 12; do
    echo "file '$SCENES_V/$n.mp4'" >> "$SCENES_V/concat.txt"
done

echo "=== Concatenating ==="
ffmpeg -f concat -safe 0 -i "$SCENES_V/concat.txt" -c copy -y "$SCENES_V/all_video.mp4" 2>&1 | tail -1

echo "=== Final mix: vertical video + narration + BGM ==="
ffmpeg -i "$SCENES_V/all_video.mp4" -i "$NARRATION" -i "$BGM" \
  -filter_complex "[1:a]volume=1.0[narr];[2:a]volume=0.55[bgm];[narr][bgm]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[aout]" \
  -map 0:v -map "[aout]" -c:v copy -c:a aac -b:a 192k -shortest -y "$FINAL" 2>&1 | tail -1

echo ""
echo "=== DONE ==="
ls -la "$FINAL"
echo "Duration:"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$FINAL"
echo "Resolution:"
ffprobe -v error -select_streams v -show_entries stream=width,height -of csv=p=0 "$FINAL"
