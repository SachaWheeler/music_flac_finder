#!/bin/bash

# Check if a directory is passed as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

# Directory to search for MP3 files
directory=$1

# Check if the provided directory exists
if [ ! -d "$directory" ]; then
  echo "Error: Directory '$directory' does not exist."
  exit 1
fi

# Loop through all MP3 files in the directory and its subdirectories
# find "$directory" -type f -name "*.mp3" -mtime +30 | while read -r file; do
find "$directory" -type f -name "*.mp3" | while read -r file; do
  # Use the file command to extract MP3 information
  info=$(file "$file")

  # Extract the bitrate from the file command output
  if [[ $info =~ ([0-9]+)\ kbps ]]; then
    bitrate="${BASH_REMATCH[1]}"
    echo "Bitrate: ${bitrate} kbps: $file "
  else
    echo "Bitrate information not found: $file "
  fi
done

