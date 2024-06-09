#!/bin/bash

MUSIC_DIR="/home/sacha/happy_share"
SOURCE_DIR="$MUSIC_DIR/incoming"
DEST_DIR="$MUSIC_DIR/Music"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Check if id3info command is available
if ! command -v id3info &> /dev/null; then
    echo "id3info could not be found, please install it first."
    exit 1
fi

# Process each mp3 file in the source directory
find "$SOURCE_DIR" -type f -name "*.mp3" | while read -r FILE; do
    # Initialize variables
    ARTIST=""
    ALBUM=""
    TRACK=""
    TITLE=""

    # Extract ID3v1 tags using id3info
    while IFS= read -r line; do
        case "$line" in
            "=== TIT2"*) TITLE=$(echo "$line" | cut -d ':' -f 2- | xargs) ;;
            "=== TPE1"*) ARTIST=$(echo "$line" | cut -d ':' -f 2- | xargs) ;;
            "=== TALB"*) ALBUM=$(echo "$line" | cut -d ':' -f 2- | xargs) ;;
            "=== TRCK"*) TRACK=$(echo "$line" | cut -d ':' -f 2- | xargs) ;;
        esac
    done < <(id3info "$FILE")

    # Check if any tag is missing and handle it (e.g., skip the file)
    if [ -z "$ARTIST" ] || [ -z "$ALBUM" ] || [ -z "$TRACK" ] || [ -z "$TITLE" ]; then
        echo "Skipping $FILE due to missing tags"
        continue
    fi

    # Create the destination path
    DEST_PATH="$DEST_DIR/$ARTIST/$ALBUM"
    mkdir -p "$DEST_PATH"

    # Move the file to the new location
    NEW_FILE="$DEST_PATH/$TRACK $TITLE.mp3"
    mv "$FILE" "$NEW_FILE"
    echo "Moved: $FILE -> $NEW_FILE"
done

echo "All files processed."

