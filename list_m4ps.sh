#!/bin/sh

find ~/happy_share/Music/Music2023/Media.localized/Apple\ Music/ -name "*.m4p" | cut -d"/" -f 9,10 | uniq -c | sort -rn | head -40

