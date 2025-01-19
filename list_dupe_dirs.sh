#!/bin/bash

# Directory to search within
search_dir="/moshpit/Music/upgrades"

# Find all directory names and store them in an array
mapfile -t dir_names < <(find "$search_dir" -type d -exec basename {} \; | sort)

# Declare an associative array to track counts of directory names
declare -A dir_count

# Populate the associative array with directory names and their counts
for dir in "${dir_names[@]}"; do
    # Escape single and double quotes
    escaped_dir=$(echo "$dir" | sed "s/'//g; s/\"//g")
    ((dir_count["$escaped_dir"]++))
done

# Print duplicated directory names
echo "Duplicated directory names:"
for dir in "${!dir_count[@]}"; do
    if [ "${dir_count[$dir]}" -gt 1 ]; then
        echo "$dir (found ${dir_count[$dir]} times)"
    fi
done

