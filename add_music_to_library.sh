#!/bin/sh

mv /home/sacha/incoming_music/* /moshpit/Music/incoming/
cd /moshpit/Music
find ./incoming/ -name "*.flac" -exec ffmpeg -n -i {} -ab 320k -map_metadata 0 -id3v2_version 3 {}.mp3 \;
find ./incoming/ -name "*.opus" -exec ffmpeg -n -i {} -ab 320k -map_metadata 0 -id3v2_version 3 {}.mp3 \;
find ./incoming/ -name "*.m4a" -exec ffmpeg -n -i {} -ab 320k -map_metadata 0 -id3v2_version 3 {}.mp3 \;
find ./incoming/ -name "*.mp3" -exec mv {} "Automatically Add to Music.localized"  \;
rm -rf incoming/*
