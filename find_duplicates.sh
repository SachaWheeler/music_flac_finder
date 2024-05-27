#!/bin/bash

# Check if a directory name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

root_dir="$1"

# Function to process each subdirectory
process_directory() {
    local dir=$1
    declare -A count_map

    # Iterate through each mp3 file in the directory
    for file in "$dir"/*.mp3; do
        if [[ -f "$file" ]]; then
            # Extract the two-digit prefix
            prefix=$(basename "$file" | grep -oE '^[0-9]{2}')
            if [[ -n "$prefix" ]]; then
                count_map["$prefix"]=$((count_map["$prefix"] + 1))
            fi
        fi
    done

    # Check for any repeated prefixes
    for prefix in "${!count_map[@]}"; do
        if [[ ${count_map["$prefix"]} -ge 2 ]]; then
            echo "Directory: $dir, Repeated prefix: $prefix"
        fi
    done
}

# Find all subdirectories and process them
find "$root_dir" -type d | while read -r sub_dir; do
    process_directory "$sub_dir"
done

