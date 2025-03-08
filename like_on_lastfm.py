from plexapi.server import PlexServer
import urllib.parse
import hashlib
import requests
from credentials import PLEX_URL, PLEX_TOKEN

# Last.fm API credentials
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
SESSION_KEY = "your_lastfm_session_key"

# Connect to Plex
plex = PlexServer(PLEX_URL, PLEX_TOKEN)

# Get currently playing track
sessions = plex.sessions()
for session in sessions:
    if session.player.title.lower() == "plexamp" and session.type == "track":
        artist = session.grandparentTitle  # Artist name
        track = session.title  # Track name

        # Construct API signature
        api_sig_str = f"api_key{API_KEY}artist{artist}methodtrack.lovesk{SESSION_KEY}track{track}{API_SECRET}"
        api_sig = hashlib.md5(api_sig_str.encode()).hexdigest()

        # Send request to love track
        params = {
            "method": "track.love",
            "api_key": API_KEY,
            "artist": artist,
            "track": track,
            "sk": SESSION_KEY,
            "api_sig": api_sig,
            "format": "json",
        }
        response = requests.post("https://ws.audioscrobbler.com/2.0/", data=params)

        if response.status_code == 200:
            print(f"❤️ Loved: {artist} - {track} on Last.fm")
        else:
            print("❌ Failed to love track:", response.text)
        break
else:
    print("No track playing in Plexamp")

