#!/usr/bin/env python
import subprocess
from plexapi.server import PlexServer
import time
from credentials import PLEX_URL, PLEX_TOKEN

# Connect to Plex
plex = PlexServer(PLEX_URL, PLEX_TOKEN)
# print(plex)
prev_message = None

def send_notification(title, message):
    """Send a desktop notification using notify-send."""
    subprocess.run(["notify-send", "-u", "normal", title, message])


def get_low_bitrate_tracks():
    """Checks if any currently playing track is below 320 kbps."""
    global prev_message
    sessions = plex.sessions()
    # print(sessions)

    for session in sessions:
        # print(session.player.title, session.type)
        if session.player.title == "happy" and session.type == "track":
            track = session.title
            artist = session.grandparentTitle
            album = session.parentTitle
            bitrate = session.media[0].bitrate if session.media else None

            like_status = "⭐" if session.userRating == 10.0 else "Not Liked"
            rating = session.userRating

            # print(track, artist, album, bitrate)

            if bitrate and bitrate < 320:
                message = f"⚠️  Now Playing: {artist} - {album} - {track} ({bitrate} kbps)"
                if message != prev_message:
                    send_notification("⚠️  Low Bitrate", f"{artist} - {album} - {track} ({bitrate} kbps)")
                    print("\a")
            else:
                message = f"🎵 Now Playing: {artist} - {track} ({bitrate} kbps) {like_status}"

            if message != prev_message:
                print(message)
                prev_message = message

if __name__ == "__main__":
    while True:
        get_low_bitrate_tracks()
        # print("x")
        time.sleep(10)  # Check every 10 seconds

