#!/bin/sh

# convert flac files into mp3 and add them to itunes

cd /home/sacha/happy_share/Music/Music2023/Media.localized/incoming
ls

# find and convert flac files
find . -name "*.flac" -exec ffmpeg -n -i {} -ab 320k -map_metadata 0 -id3v2_version 3 {}.mp3 \;
mv *.mp3 "Automatically Add to Music.localized"
mv *.flac ../removed/

