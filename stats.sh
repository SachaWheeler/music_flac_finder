#!/bin/bash

TOTAL=$(wc -l bitrates.txt)
echo "total files: ${TOTAL}"

NOT_FOUND=$(grep "not found" bitrates.txt | wc -l)
echo "no tag data: ${NOT_FOUND}"

grep -v "not found" bitrates.txt | cut -d":" -f2 | sort | uniq -c | sort -k2,2rn
