class Prompts:
    def __init__(self):
        self.prompts = []
        self.promptsPerPerson = 0  # This attribute will be the number of prompts each person submits to the game

    def setPromptsPerPerson(self):
        # Will set the number of prompts per person.
        ...

    def getPromptFromPlayer(self, player):
        # Gets a prompt from player. Will be called from the game so a player from the game can be used as an argument.
        ...


class Player:
    def __init__(self):
        self.name = ""
        self.roster = []
        self.initialRoster = []
        self.playerExists = False
        self.playerId = 0
        self.score = 0
        self.colour = ""
        self.shape = ""
        self.rounds = 0

    def setupPlayer(self):
        # Sets up the player's profile
        self.setName()
        self.setColour()
        self.setShape()

    def setName(self):
        self.name = input("What is your name? ")

    def setColour(self):
        self.colour = input("Choose a colour. ")

    def setShape(self):
        self.shape = input("Choose a shape. ")

    def displayRoster(self):
        # Displays the roster of the player at the time this method is called.
        count = 0
        for item in self.roster:  # Formats it in the form: 1. (song name)
            print(f"{count + 1}: {item}")
            count += 1

    def chooseSong(self):
        # When it comes to the drafting phase, the player will choose a song from
        ...


class Game:
    def __init__(self):
        self.players = []  # A list of all the instantiations of the player class. (i.e. all the player objects.)
        self.NoPlayers = 0  # The number of players in the game.
        self.noRounds = 0  # The ideal number of rounds in a game
        self.roundsPlayed = 0  # The number of rounds played currently.
        self.playlist = []  # An array containing all the songs in the playlist withdrawn from the Spotify API.
        self.playlistLink = ""  # The link to the Spotify playlist. Will be used when saving the game.
        self.defaultPlaylistLink = ""  # Default Playlist Link that will be used if the players don't want to enter one.
        self.prompts = Prompts()  # A Prompts Object is instantiated: COMPOSITION!!!
        self.songsPerPerson = 0  # The chosen amount of songs per person.
        self.leaderboard = []

    def setup(self):
        self.setNoPlayers()

        # Setting up players
        for i in range(self.NoPlayers):
            player = Player()  # Instantiates each player as an object of the Player Class.
            player.setupPlayer()  # Sets up the player.
            self.players.append(player)  # Appends the player object to the list of players.
            print('\n')

        # Setting up prompts
        self.prompts.setPromptsPerPerson()  # Sets the number of prompts per person.
        for player in self.players:
            for i in range(self.prompts.promptsPerPerson):
                self.prompts.getPromptFromPlayer(player.name)  # Gets the number of required prompts.

        self.setPlaylist()

        # Don't forget to ensure we have the right number of rounds, we have to do the following:
        self.noRounds = (self.NoPlayers * self.songsPerPerson) // 2

    def setNoSongsPerPerson(self):
        self.songsPerPerson = input("How many songs do you want to have per person? ")

        # There will be an algorithm to validate whether this number will be possible to use within the game.

    def setNoPlayers(self):
        self.NoPlayers = int(input("How many players are playing? "))
        while self.NoPlayers < 3:
            # Remember - the game needs to be played with at least 3 players
            self.NoPlayers = int(input("How many players are playing? "))

    def setPlaylist(self):
        defaultOrCustom = input(
            "Do you want to use the default Playlist or your own playlist?\nEnter 'd' for Default Playlist and any "
            "other button for Custom Playlist. ")

        defaultOrCustom = defaultOrCustom.lower()

        if defaultOrCustom == 'd':
            self.playlistLink = self.defaultPlaylistLink
            # SPOTIFY API EXTRACTS PLAYLIST HERE (USING THE CODE MENTIONED EARLIER).

        else:
            self.playlistLink = input("Go to your Spotify profile and choose one of your playlists. "
                                      "\nClick on the 3 dots and press share then Copy Link. "
                                      "\nPaste it here: ")
            # This asks the user for the link to their desired Spotify Playlist.

    def displayPlaylist(self):
        # Displays the playlist.
        count = 1
        for item in self.playlist:
            print(f'{count}: {item}')  # Displays it nicely.
            count += 1

    def draft(self):
        # This is where the drafting process mentioned earlier will happen.
        ...

    def vote(self):
        # The method which will be the voting phase
        ...

    def rearrangePlayers(self):
        # The method which will rearrange the players.
        ...

    def decideWinner(self):
        # Will add the required amount of points to the player with a song remaining in their roster.
        # It will then display the leaderboard
        self.displayLeaderboard()

    def displayLeaderboard(self):
        # Contains the INSERTION SORT which will be the algorithm to organise the playlist in descending order by score.
        ...

    def saveGame(self):
        # The method which will save the game.
        ...





