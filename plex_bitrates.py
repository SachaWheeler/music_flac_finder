from plexapi.server import PlexServer

# Plex server details
PLEX_URL = "http://127.0.0.1:32400"
PLEX_TOKEN = "_iqZ4xQXCYy9UtYuMFpM"

# Connect to Plex
plex = PlexServer(PLEX_URL, PLEX_TOKEN)

# Fetch all music tracks
tracks = plex.library.section("Music").searchTracks()

# Extract relevant data (title, artist, album, play count, bitrate)
track_data = [
    {
        "title": track.title,
        "artist": track.grandparentTitle,  # Artist name
        "album": track.parentTitle,        # Album name
        "play_count": track.viewCount or 0,  # Default to 0 if None
        "bitrate": track.media[0].bitrate if track.media else None
    }
    for track in tracks
]

# Sort by play count (descending)
sorted_tracks = sorted(track_data, key=lambda x: x["play_count"], reverse=True)

# Print results
for track in sorted_tracks:
    print(f"{track['play_count']:>3} plays | {track['bitrate']} kbps | {track['artist']} - {track['album']} - {track['title']}")

