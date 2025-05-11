from plexapi.server import PlexServer
from credentials import PLEX_URL, PLEX_TOKEN
import os


plex = PlexServer(PLEX_URL, PLEX_TOKEN)
music = plex.library.section("Music")

def find_unknown_paths():
    print("🔍 Scanning for 'Unknown' tracks, albums, and artists...\n")

    def get_path(item):
        try:
            return item.media[0].parts[0].file
        except Exception as e:
            return f"[no path found] {e}"

    # Unknown Tracks
    unknown_tracks = music.searchTracks(title="Unknown")
    if unknown_tracks:
        print("🎵 Unknown Tracks:")
        for track in unknown_tracks:
            filepath = get_path(track)
            print(f"- {track.title} ({track.grandparentTitle} - {track.parentTitle})")
            print(f"  Path: {filepath}")
            print(f"  Dir:  {os.path.dirname(filepath)}\n")

    # Unknown Albums
    unknown_albums = music.searchAlbums(title="Unknown")
    if unknown_albums:
        print("💿 Unknown Albums:")
        for album in unknown_albums:
            try:
                filepath = album.tracks()[0].media[0].parts[0].file
                print(f"- {album.title} (Artist: {album.parentTitle})")
                print(f"  Path: {filepath}")
                print(f"  Dir:  {os.path.dirname(filepath)}\n")
            except:
                print(f"- {album.title} (Artist: {album.parentTitle}) [no media path found]")

    # Unknown Artists
    unknown_artists = music.searchArtists(title="Unknown")
    if unknown_artists:
        print("🎤 Unknown Artists:")
        for artist in unknown_artists:
            try:
                album = artist.albums()[0]
                filepath = album.tracks()[0].media[0].parts[0].file
                print(f"- {artist.title}")
                print(f"  Path: {filepath}")
                print(f"  Dir:  {os.path.dirname(filepath)}\n")
            except:
                print(f"- {artist.title} [no media path found]")

if __name__ == "__main__":
    find_unknown_paths()

