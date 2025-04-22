#!/usr/bin/env python3
from plexapi.server import PlexServer
from credentials import PLEX_URL, PLEX_TOKEN

# Connect to Plex
plex = PlexServer(PLEX_URL, PLEX_TOKEN)

# Get the music library
music_library = plex.library.section("Music")

# Find tracks with 'unknown' in artist or album name (case-insensitive)
unknown_tracks = []

for track in music_library.searchTracks():
    artist = (track.originalTitle or track.grandparentTitle or "").strip()
    album = (track.parentTitle or "").strip()

    # Check case-insensitively if 'unknown' appears anywhere in the artist or album name
    if "unknown" in artist.lower() or "unknown" in album.lower():
        for media in track.media:
            for part in media.parts:
                file_path = part.file
                bitrate = media.bitrate  # Bitrate in kbps
                unknown_tracks.append((file_path, bitrate, track.title, artist, album))

# Display results
if unknown_tracks:
    print("Tracks with 'Unknown' in Artist or Album Name (Case-Insensitive):")
    for file_path, bitrate, title, artist, album in unknown_tracks:
        print(
            f"Path: {file_path}, Bitrate: {bitrate} kbps, Title: {title}, Artist: {artist}, Album: {album}"
        )
else:
    print("No tracks with 'Unknown' in artist or album name found.")
