grep -v 320\ kbps bitrates.txt | cut -d"|" -f3| cut -d"-" -f1,2 | sort | uniq -c | sort -rn | less
