#!/bin/sh

# convert flac files into mp3 and add them to itunes

cd /Volumes/backup/new_music

# Move original, NON-CONVERTED mp3s to iTunes dir
# find . -type f -and -name "*.mp3" -and ! -name "*.flac.mp3" -exec mv {} "/Users/happy/Music/Music2023//Media.localized/Automatically Add to Music.localized/" \;
find . -type f -name "*.mp3" -exec mv {} "/Users/happy/Music/Music2023//Media.localized/Automatically Add to Music.localized/" \;
# find . -type f -and -name "*.mp3" -and ! -name "*.flac.mp3" -exec ls -lah {} \;
# find ./x -name "*.mp3" -exec ls -lah {} \;

