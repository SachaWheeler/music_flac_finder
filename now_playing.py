from plexapi.server import PlexServer
import time

# Configure your Plex details
PLEX_URL = "http://127.0.0.1:32400"
PLEX_TOKEN = "dQfP1K7DXj3emyx6zfh2"

# Connect to Plex
plex = PlexServer(PLEX_URL, PLEX_TOKEN)
prev_message = None

def get_low_bitrate_tracks():
    """Checks if any currently playing track is below 320 kbps."""
    global prev_message
    sessions = plex.sessions()

    for session in sessions:
        if session.player.title == "happy" and session.type == "track":
            track = session.title
            artist = session.grandparentTitle
            album = session.parentTitle
            bitrate = session.media[0].bitrate if session.media else None

            if bitrate and bitrate < 320:
                message = f"⚠️ Now Playing: {artist} - {track} ({bitrate} kbps) [LOW BITRATE]"
            else:
                message = f"🎵 Now Playing: {artist} - {track} ({bitrate} kbps)"
            if message != prev_message:
                print(message)
                prev_message = message

if __name__ == "__main__":
    while True:
        get_low_bitrate_tracks()
        time.sleep(10)  # Check every 10 seconds

