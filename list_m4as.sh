#!/bin/sh

find /home/sacha/happy_share/Music/ -name "*.m4a" | cut -d"/" -f 6,7 | uniq -c | sort -rn | less

