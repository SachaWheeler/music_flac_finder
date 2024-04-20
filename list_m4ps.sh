#!/bin/sh

find /home/sacha/happy_share/Apple\ Music/ -name "*.m4p" | cut -d"/" -f 6,7 | uniq -c | sort -rn | less

