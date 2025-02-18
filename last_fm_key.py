import hashlib
import requests
import webbrowser

API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
USERNAME = "your_lastfm_username"

# Step 1: Get token
auth_url = f"https://www.last.fm/api/auth/?api_key={API_KEY}&cb=http://www.last.fm/callback"
webbrowser.open(auth_url)
print("Go to this URL and authorize:", auth_url)

# Step 2: After authorizing, get session key
TOKEN = input("Enter the token from Last.fm URL: ")

# Generate API signature
api_sig_str = f"api_key{API_KEY}methodauth.getSessiontoken{TOKEN}{API_SECRET}"
api_sig = hashlib.md5(api_sig_str.encode()).hexdigest()

# Request session key
params = {
    "method": "auth.getSession",
    "api_key": API_KEY,
    "token": TOKEN,
    "api_sig": api_sig,
    "format": "json",
}
response = requests.get("https://ws.audioscrobbler.com/2.0/", params=params)
session_key = response.json()["session"]["key"]

print("Your Last.fm session key:", session_key)

