#!/usr/bin/env bash
# Ajoute la fin Bayto.tech (carte S'abonner + bayto.tech, voix audio/outro_bayto.mp3) à une vidéo déjà rendue.
# Usage : ./outro_concat.sh videos/outro/<nom>.json <video_source.mp4> <secondes_à_garder> <sortie.mp4>
#   <secondes_à_garder> = fin du dernier mot de la vidéo source + 0,6 s
set -e
spec="$1"; src="$2"; trim="$3"; out="$4"
mkdir -p out
tmp="out/_outro_$(basename "$spec" .json).mp4"
node render.mjs "$spec" "$tmp" --audio audio/outro_bayto.mp3
ffmpeg -v error -y -t "$trim" -i "$src" -i "$tmp" \
  -filter_complex "[0:a]aresample=44100[a0];[1:a]aresample=44100[a1];[0:v][a0][1:v][a1]concat=n=2:v=1:a=1[v][a]" \
  -map "[v]" -map "[a]" -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -movflags +faststart "$out"
echo "ok -> $out"
