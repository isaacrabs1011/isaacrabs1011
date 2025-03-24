playerName = ''
def displayPlaylist():
    ...
playlist = []
players = []


def draft(self):
    currentPlayer = 0

    while len(self.playlist) > 0:
        print(f"It's {players[currentPlayer].playerName}'s turn to pick a song.")
        displayPlaylist()

        songNumber = int(input(f"Pick a number 1-{len(playlist)} "))
        song = playlist[songNumber - 1]

        players[currentPlayer].roster.append(song)
        players[currentPlayer].initialRoster.append(song)
        playlist.remove(song)

        if currentPlayer == self.NoPlayers - 1:
            currentPlayer = 0
        else:
            currentPlayer += 1

    print("Here is everyone's roster: ")

    for item in players:
        print(f"{item.name}:")
        item.displayRoster()
        print('\n')