#!/bin/sh

cd ~/Downloads
# ls */* | grep -v mp3 | grep -v flac | grep -v part | less

HOST='happy.local'
USER='happy'
# INCOMING_DIR='/Users/happy/Music/Music2023/Media.localized/incoming/'
INCOMING_DIR='/Volumes/moshpit/Music/incoming/'

rsync -zav --remove-source-files --prune-empty-dirs /home/sacha/Downloads/ $USER@$HOST:$INCOMING_DIR --include "*/" --include="*.m4a" --include="*.mp3" --include="*.flac" --include="*.ogg" --exclude="*"

ssh $USER@$HOST<<END_SSH
cd $INCOMING_DIR
pwd
ls

find . -name "*.flac" -exec ffmpeg -n -i {} -ab 320k -map_metadata 0 -id3v2_version 3 {}.mp3 \;

mv * ../"Automatically Add to Music.localized"

echo 'Done'
END_SSH
