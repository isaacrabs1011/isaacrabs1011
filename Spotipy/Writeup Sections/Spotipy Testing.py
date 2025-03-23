import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID = '5143755320f74541986016c151d8b004'
SPOTIPY_CLIENT_SECRET = '8466dcc0498847eabf4cc3b83b6a0742'
SPOTIPY_REDIRECT_URI = 'http://localhost.callback'


auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
isaac = spotipy.Spotify(auth_manager=auth_manager)

playlist = isaac.playlist('https://open.spotify.com/playlist/1cI4JIuEyIYn3WB20lrPgW?si=df6ed83c6dc14c56')

songs = []
for item in playlist['tracks']['items']:
    track = item['track']
    songs.append(track['artists'][0]['name'] + ' - ' + track['name'])

print()
print()
print(f"The playlist length is {len(songs)}")

count = 1
for item in songs:
    print(f'{count}: {item}')
    count += 1
