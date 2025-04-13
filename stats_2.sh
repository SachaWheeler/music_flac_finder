#!/bin/bash

TOTAL=$(wc -l bitrates.txt)
echo "total files: ${TOTAL}"

grep -E '\b1[0-9]{2}\b|\b200\b' bitrates.txt | cut -d"|" -f2 | sort | uniq -c | sort -n -k2 | less
