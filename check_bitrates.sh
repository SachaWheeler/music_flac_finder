find /moshpit/Music/Music -type f -name "*.mp3" -exec bash -c '
for file; do
  bitrate=$(ffprobe -v error -select_streams a:0 -show_entries stream=bit_rate -of csv=p=0 "$file" | awk "{print int(\$1/1000)}")
  if (( bitrate < 320 )); then
    echo "Low bitrate: $bitrate kbps - $file"
  fi
done
' bash {} +

