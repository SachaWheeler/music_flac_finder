#!/bin/bash

# Path to the Compilations directory (replace this with the actual path)
music_dir="/moshpit/Music/Music/Various Artists/The Mack"

# Find all MP3 files recursively in the Compilations directory
find "$music_dir" -type f -name "*.mp3" | while read -r file; do
    # Set the TPE2 tag to "Various Artists"
    id3v2 --TPE2 "Various Artists" "$file"

    if [ $? -eq 0 ]; then
        echo "Updated TPE2 for: $file"
    else
        echo "Error updating $file"
    fi
done

