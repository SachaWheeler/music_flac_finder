#!/bin/sh

find /moshpit/Music/Music/ -name "*.m4a" | cut -d"/" -f 6,7 | uniq -c | sort -rn | less

