#!/usr/bin/bash

find /moshpit/Music/Music -type f -iname "*.mp3" -printf '%h\n' | \
sort | uniq -c | awk '$1 < 3 { $1=""; print substr($0,2) }' | \
while IFS= read -r dir; do
  echo "== $dir =="
  find "$dir" -maxdepth 1 -type f -iname "*.mp3"
  echo
done

