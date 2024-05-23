#!/bin/sh

find /home/sacha/happy_share/Music/ -name "* 1.m*" | grep -iv "pt "| grep -iv "part "| cut -d"/" -f6,7 | sort | uniq -c | sort -nr | less

