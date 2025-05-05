import os
import re
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TPE2  # TPE2 = Album Artist

# Path to your MP3 directory
mp3_dir = "/moshpit/Music/Music/Various Artists/Dazed And Confused"

# Regex to match filename pattern: track number, artist, title
pattern = re.compile(r'^(\d+)\s+(.+?)\s*-\s*(.+)\.mp3$', re.IGNORECASE)

for filename in os.listdir(mp3_dir):
    if filename.lower().endswith(".mp3"):
        match = pattern.match(filename)
        if match:
            track_number, artist, title = match.groups()
            filepath = os.path.join(mp3_dir, filename)

            try:
                audio = EasyID3(filepath)
            except Exception:
                audio = EasyID3()
                audio.save(filepath)
                audio = EasyID3(filepath)

            audio['tracknumber'] = track_number
            audio['artist'] = artist
            audio['title'] = title
            audio['albumartist'] = "Various Artists"
            audio.save(filepath)

            # Set AlbumArtist using full ID3 frame for compatibility
            id3 = ID3(filepath)
            id3.add(TPE2(encoding=3, text="Various Artists"))
            id3.save(filepath)

            print(f"Tagged: {filename}")
        else:
            print(f"Skipped (no match): {filename}")

