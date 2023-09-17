#!/bin/sh

#rsync -zav  --prune-empty-dirs --dry-run /home/sacha/Downloads/ happy@happy.local:/Volumes/backup/new_music/ --include "*/" --include="*.mp3" --include="*.flac" --include="*.ogg" --exclude="*"
rsync -zav --remove-source-files --prune-empty-dirs /home/sacha/Downloads/ happy@happy.local:/Volumes/backup/new_music/ --include "*/" --include="*.mp3" --include="*.flac" --include="*.ogg" --exclude="*"

