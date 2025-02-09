# ["ü"]="u"
# ["é"]="e"
# ["ñ"]="n"
# ["ö"]="o"
# ["à"]="a"
# ["ç"]="c"
find /moshpit/Music/Music/ -type f -name "*ì*" | while read -r file; do
    newfile=$(echo "$file" | sed 's/ì/i/g')
    mv "$file" "$newfile"
    echo "Renamed: $file -> $newfile"
done

