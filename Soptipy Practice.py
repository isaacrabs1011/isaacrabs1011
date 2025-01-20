import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID = '5143755320f74541986016c151d8b004'
SPOTIPY_CLIENT_SECRET = '8466dcc0498847eabf4cc3b83b6a0742'
SPOTIPY_REDIRECT_URI = 'http://localhost.callback'

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)
playlist = sp.playlist('https://open.spotify.com/playlist/6GhmUa261lqAmWsod8A6vu?si=4d354f348327435b')
for item in playlist['tracks']['items']:
    track = item['track']
    print(track['artists'][0]['name'] + ' - ' + track['name'])