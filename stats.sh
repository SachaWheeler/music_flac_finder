#!/bin/bash

TOTAL=$(wc -l bitrates.txt)
echo "total files: ${TOTAL}"

grep -v "not found" bitrates.txt | cut -d"|" -f2 | sort | uniq -c | sort -n -k2 | less
