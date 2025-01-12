import argparse
import sys
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError

def set_id3_tags(file, artist=None, album_title=None, album_artist=None):
    try:
        # Load existing ID3 tags or create new ones
        try:
            tags = EasyID3(file)
        except ID3NoHeaderError:
            tags = EasyID3()

        # Update tags if arguments are provided
        if artist:
            tags['artist'] = artist
        if album_title:
            tags['album'] = album_title
        if album_artist:
            tags['albumartist'] = album_artist

        # Save changes
        tags.save(file)
        print(f"Updated tags for: {file}")
    except Exception as e:
        print(f"Error updating {file}: {e}")

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Edit ID3 tags for MP3 files.")
    parser.add_argument("-Artist", help="Set the artist name", type=str)
    parser.add_argument("-AlbumTitle", help="Set the album title", type=str)
    parser.add_argument("-AlbumArtist", help="Set the album artist", type=str)
    parser.add_argument("files", nargs="+", help="MP3 files to edit")

    # Parse arguments
    args = parser.parse_args()

    # Process each file
    for file in args.files:
        set_id3_tags(
            file,
            artist=args.Artist,
            album_title=args.AlbumTitle,
            album_artist=args.AlbumArtist
        )

if __name__ == "__main__":
    main()

