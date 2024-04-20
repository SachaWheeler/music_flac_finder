#!/bin/bash

# Directory containing m4a files
directory="/home/sacha/happy_share/Music/Aimee Mann/Mental Illness"

# Find all m4a files recursively in the directory
find "$directory" -type f -name "*.m4a" -print0 | while IFS= read -r -d '' file; do
    # Get the filename without extension
    filename=$(basename -- "$file")
    filename_without_extension="${filename%.*}"

    # Convert m4a to mp3
    ffmpeg -i "$file" -ab 320k  "$directory/${filename_without_extension}.mp3"

    # Remove the original m4a file
    rm "$file"
done

