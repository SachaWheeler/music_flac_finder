from plexapi.server import PlexServer
from credentials import PLEX_URL, PLEX_TOKEN

plex = PlexServer(PLEX_URL, PLEX_TOKEN)

# Get all sessions (i.e., currently playing)
sessions = plex.sessions()

if not sessions:
    print("No active sessions.")
    exit()

# Assume you want to like the first active media item
media = sessions[0]

# Optional: print now playing info
print(f"Now playing: {media.title} by {media.grandparentTitle}")

# Rate it 10/10, which Plex treats as "Like"
media.rate(10)

print("Track liked!")

