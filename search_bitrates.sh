#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <bitrate>"
    exit 1
fi

# Store the argument
ARG=$1

# Print the argument
echo "You provided: $ARG"

grep -v "$ARG kbps" bitrates.txt | cut -d"|" -f3| cut -d"-" -f1,2 | sort | uniq -c | sort -rn | less
