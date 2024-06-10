#!/bin/bash

SOURCE_DIR="/music/incoming"
DEST_DIR="/music/Music"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Check if id3v2 command is available
if ! command -v id3v2 &> /dev/null; then
    echo "id3v2 could not be found, please install it first."
    exit 1
fi

# Process each mp3 file in the source directory
find "$SOURCE_DIR" -type f -name "*.mp3" | while read -r FILE; do
    # Initialize variables
    ARTIST=""
    ALBUM=""
    TRACK=""
    TITLE=""

    # Extract ID3 tags
    while IFS= read -r line; do
        case "$line" in
            *TPE1*) ARTIST=$(echo "$line" | cut -d ':' -f 2- | xargs) ;;
            *TALB*) ALBUM=$(echo "$line" | cut -d ':' -f 2- | xargs) ;;
            *TRCK*) TRACK=$(echo "$line" | cut -d ':' -f 2- | xargs) ;;
            *TIT2*) TITLE=$(echo "$line" | cut -d ':' -f 2- | xargs) ;;
        esac
    done < <(id3v2 -R "$FILE")

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
    # mv "$FILE" "$NEW_FILE"
    echo "Moved: $FILE -> $NEW_FILE"
done

echo "All files processed."

