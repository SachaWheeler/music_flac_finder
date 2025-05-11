from plexapi.server import PlexServer
from credentials import PLEX_URL, PLEX_TOKEN
import os

plex = PlexServer(PLEX_URL, PLEX_TOKEN)
music = plex.library.section("Music")

def find_tracks_missing_metadata():
    print("🔍 Scanning for tracks missing artist or album metadata...\n")
    results = []

    for track in music.searchTracks():
        artist = getattr(track, 'grandparentTitle', None)
        album = getattr(track, 'parentTitle', None)

        if not artist or not album or artist.lower() in ["", "unknown"] or album.lower() in ["", "unknown"]:
            try:
                filepath = track.media[0].parts[0].file
                results.append((track.title, artist, album, filepath))
            except Exception as e:
                results.append((track.title, artist, album, "[path error]"))

    if results:
        for title, artist, album, path in results:
            print(f"🎵 {title}")
            print(f"   Artist: {artist}")
            print(f"   Album:  {album}")
            print(f"   Path:   {path}\n")
        print(f"✅ Found {len(results)} tracks with missing metadata.")
    else:
        print("✅ No tracks with missing artist or album metadata found.")

if __name__ == "__main__":
    find_tracks_missing_metadata()

