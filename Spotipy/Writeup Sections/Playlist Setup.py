players = []
songs = []
defaultPlaylistID = ""
playlist = []


def displayPlaylist():
    ...


defaultOrCustom = input("Do you want to use the default Playlist or your own playlist?\nEnter 'd' for Default "
                        "Playlist and any other button for Custom Playlist. ")

if defaultOrCustom == 'd':
    playlistLink = defaultPlaylistID
else:
    playlistLink = input("Enter playlist Link: ")

# SPOTIFY PLAYLIST EXTRACTS PLAYLIST

maxSongsPP = len(songs) // len(players)
print(f"There are {len(songs)} songs in the playlist, and {len(players)} players.")
print(f"The max amount of songs each player can have is {maxSongsPP}.")
songsPerPerson = int(input("How many songs should each player have? "))

while songsPerPerson > maxSongsPP:
    print(f"You can't have more than {maxSongsPP} songs per person.")
    songsPerPerson = int(input("How many songs should eac player have? "))

desiredPlaylistLength = songsPerPerson * len(players)
while len(playlist) > desiredPlaylistLength:
    playlist.pop(len(playlist) - 1)

displayPlaylist()  # Function which will display playlist.
