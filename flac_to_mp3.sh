#!/bin/sh

# convert flac files into mp3 and add them to itunes

cd /Volumes/backup/new_music
# ls

# find and convert flac files
# find ./x -name "*.flac" -exec ls -lah {} \;
find . -name "*.flac" -exec ffmpeg -n -i {} -ab 320k -map_metadata 0 -id3v2_version 3 {}.mp3 \;

