import spotipy  # Import the Spotipy library, which allows interaction with the Spotify API
from spotipy.oauth2 import SpotifyClientCredentials  # Import the authentication manager for client credentials flow

SPOTIPY_CLIENT_ID = '5143755320f74541986016c151d8b004'  # Your Spotify Client ID
SPOTIPY_CLIENT_SECRET = '8466dcc0498847eabf4cc3b83b6a0742'  # Your Spotify Client Secret
SPOTIPY_REDIRECT_URI = 'http://localhost.callback'  # Redirect URI (not used in client credentials flow)

# Authenticate with Spotify using client credentials flow (does not require user login)
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)  # Create a Spotify API client using the authenticated session

# Fetch playlist details using its Spotify URL (or ID)
playlist = sp.playlist('https://open.spotify.com/playlist/6GhmUa261lqAmWsod8A6vu?si=4d354f348327435b')

# Iterate through the playlist tracks and print artist and song name
for item in playlist['tracks']['items']:  # Loop through each track item in the playlist
    track = item['track']  # Extract track details
    print(track['artists'][0]['name'] + ' - ' + track['name'])  # Print the first artist's name and the track title
