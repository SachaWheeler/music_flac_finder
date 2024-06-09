#!/bin/bash

# Check if a directory name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

root_dir="$1"

# Function to process each directory containing files ending with " 1.mp3"
process_directory() {
    local dir=$1
    local files=("$dir"/*\ 1.mp3)

    if [ ${#files[@]} -eq 0 ]; then
        return
    fi

    echo "Directory: $dir"
    echo "Files ending with ' 1.mp3':"
    ls "$dir"

    for file in "${files[@]}"; do
        newfile="${file// 1.mp3/.mp3}"
        mv "$file" "$newfile"
        echo "Renamed: $(basename "$file") to $(basename "$newfile")"
    done
}

# Main script
export -f process_directory

# Find directories containing files ending with " 1.mp3" beneath the specified root directory
dirs_with_files=$(find "$root_dir" -type f -name "* 1.mp3" -exec dirname {} \; | sort -u)

# Iterate through each directory and process them
while IFS= read -r dir; do
    process_directory "$dir"
done <<< "$dirs_with_files"

