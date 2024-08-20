#!/bin/bash

find /moshpit/Music/Music/ -type f -name '*.mp3' ! -regex '.*/[0-9].*\.mp3'  | cut -d"/" -f5,6 | uniq -c | sort -rn | less
