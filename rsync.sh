#!/bin/sh

cd ~/Downloads
# ls */* | grep -v mp3 | grep -v flac | grep -v part | less


find . -type f -name "*.cue" -delete
find . -type f -name "*.CUE" -delete
find . -type f -name "*.log" -delete
find . -type f -name "*.jpg" -delete
find . -type f -name "*.jpeg" -delete
find . -type f -name "*.JPG" -delete
find . -type f -name "*.txt" -delete
find . -type f -name "*.url" -delete
find . -type f -name "*.md5" -delete
find . -type f -name "*.docx" -delete
find . -type f -name "*.m3u" -delete
find . -type f -name "*.ffp" -delete
find . -type f -name "*.nfo" -delete
find . -type f -name "*.png" -delete
find . -type f -name "*.gif" -delete
find . -type f -name "*.pdf" -delete
find . -type f -name "Thumbs.db" -delete
find . -type f -name "*.rar" -delete

rmdir */*/*/*
rmdir */*/*
rmdir */*
rmdir *

rsync -zav --remove-source-files --prune-empty-dirs /home/sacha/Downloads/ happy@happy.local:/Volumes/backup/new_music/ --include "*/" --include="*.m4a" --include="*.mp3" --include="*.flac" --include="*.ogg" --exclude="*"

