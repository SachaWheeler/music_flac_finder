#!/bin/sh

MOUNT_POINT="/moshpit"
INCOMING_DIR="/home/sacha/incoming_music"

MUSIC_DEST_DIR="$MOUNT_POINT/Music/Automatically Add to Music.localized/"
TV_DEST_DIR="$MOUNT_POINT/tv/"
MOVIE_DEST_DIR="$MOUNT_POINT/movies/"


if mount | grep -q "on $MOUNT_POINT type fuse.sshfs"; then
    echo "Remote disk is mounted at $MOUNT_POINT."
else
    echo "Remote disk is NOT mounted at $MOUNT_POINT."
    sshfs -o allow_other happy@happy.local:/Volumes/moshpit $MOUNT_POINT
fi

# convert flacs to mp3
find "$INCOMING_DIR" -type f -name "*.flac" \
        -exec ffmpeg -n -i {} -ab 320k -map_metadata 0 -id3v2_version 3 {}.mp3 \;
find "$INCOMING_DIR" -type f -name "*.flac" \
        -exec rm {} \;

# move mp3s to MUSIC_DEST_DIR
find "$INCOMING_DIR" -type f -name "*.mp3" \
        -exec mv {} "$MUSIC_DEST_DIR" \;

# move TV shows
find "$INCOMING_DIR" -type f -regextype posix-egrep \
        -regex '.*S[0-9]{2}E[0-9]{2}.*\.(mp4|mkv|avi)' \
        -exec mv {} "$TV_DEST_DIR" \;

# and any other video files
find "$INCOMING_DIR" -type f -regextype posix-egrep \
        -regex '.*\.(mp4|mkv|avi)' \
        -exec mv {} "$MOVIE_DEST_DIR" \;

echo 'Done'
