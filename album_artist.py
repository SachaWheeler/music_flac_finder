import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TPE2

music_dir = "/moshpit/Music/Music/Compilations/"

# Iterate over all files in the directory and its subdirectories
for root, dirs, files in os.walk(music_dir):
    print(root, dirs, files)
    for file in files:
        print("x", file)
        if file.endswith(".mp3"):
            file_path = os.path.join(root, file)
            try:
                # Load the MP3 file's ID3 tags
                audio = ID3(file_path)

                # Set the TPE2 tag to "Various Artists"
                audio['TPE2'] = TPE2(encoding=3, text="Various Artists")

                # Save the updated tag back to the file
                audio.save()
                print(f"Updated TPE2 for: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
            break
    break
