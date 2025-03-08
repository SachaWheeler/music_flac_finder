from plexapi.server import PlexServer
from credentials import PLEX_URL, PLEX_TOKEN

# Connect to Plex
plex = PlexServer(PLEX_URL, PLEX_TOKEN)

# Get the music library
music_library = plex.library.section("Music")

# Retrieve all liked tracks
liked_tracks = [
    track for track in music_library.searchTracks()
    if track.userRating and track.userRating > 9  # Assuming 10 = Liked
]

# Filter and sort by play count
filtered_tracks = [
    {
        "title": track.title,
        "artist": track.artist().title if track.artist() else "Unknown",
        "bitrate": track.media[0].bitrate if track.media else 0,
        "play_count": track.viewCount if track.viewCount else 0,
    }
    for track in liked_tracks
    if track.media and track.media[0].bitrate < 320
]

# Sort by play count (most played first)
filtered_tracks.sort(key=lambda x: x["play_count"], reverse=True)

# Print results
for track in filtered_tracks[:30]:  # Show top 20 results
    print(f"{track['artist']} - {track['title']} | Bitrate: {track['bitrate']} kbps | Plays: {track['play_count']}")

