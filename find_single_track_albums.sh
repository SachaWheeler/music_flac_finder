#!/bin/bash

# Function to find directories with at least 1 and less than 3 mp3 files
find_directories_with_1_to_2_mp3() {
    # Loop through directories containing mp3 files
    while IFS= read -r dir; do
        # Count the number of mp3 files in the directory
        mp3_count=$(find "$dir" -maxdepth 1 -type f -name '*.mp3' | wc -l)

        # If the directory has at least 1 and less than 3 mp3 files, print its path
        if [ "$mp3_count" -ge 1 ] && [ "$mp3_count" -lt 3 ]; then
            echo "$dir"
        fi
    done < <(find "$1" -type d)
}

# Main script
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

directory="$1"

# Check if the directory exists
if [ ! -d "$directory" ]; then
    echo "Error: Directory '$directory' not found."
    exit 1
fi

# Find directories with at least 1 and less than 3 mp3 files
echo "Directories with at least 1 and less than 3 mp3 files:"
find_directories_with_1_to_2_mp3 "$directory"

