# class Playlist:
#     def __init__(self, songs: list, title):
#         self.songs = songs
#         self.title = title
#         self.numberOfSongs = len(songs)
# 
#     def getSongs(self):
#         return self.songs
# 
#     def getTitle(self):
#         return self.title


class Player:
    def __init__(self):
        self.name = ''
        self.colour = ''
        self.shape = ''
        self.roster = []
        
    def setupPlayer(self):
        self.setName()
        self.setColour()
        self.setShape()

    def getName(self):
        return self.name

    def getColour(self):
        return self.colour

    def getShape(self):
        return self.shape
    
    def setName(self):
        self.name = input("Enter your name... ")
        
    def setColour(self):
        self.colour = input("Choose a colour... ")

    def setShape(self):
        self.shape = input("Choose a shape... ")

    def displayRoster(self):
        count = 0
        for item in self.roster:
            print(f"{count+1}: {item}")


# class Roster:
#     def __init__(self, roster):
#         self.startingOrder = roster
#         self.rankedOrder = []
# 
#     def rankOrder(self):
#         ...


class Game:

    def __init__(self):
        self.players = []
        self.NoPlayers = 0
        self.playlist = []

    def setNumberOfPlayers(self):
        self.NoPlayers = int(input("How many players are playing? "))

    def setPlaylist(self):
        # When fully working would use the Spotify API
        # In the meantime I'll just ask the user to enter some songs

        for i in range(3): #number needs to be divisible by the number of players so everyone has an equal number of songs
            song = input("name a song: ")
            self.playlist.append(song)

    def displayPlaylist(self):
        count = 1
        for item in self.playlist:

            print(f'{count}: {item}')
            count += 1

    def setup(self):
        Game.setNumberOfPlayers(self)
        noP = Game.getNoPlayers(self)

        for i in range(noP):
            player = Player()
            player.setupPlayer()
            self.players.append(player)
            print('\n')

        Game.setPlaylist(self)
        Game.draft(self)

    def draft(self): #my questionnaire will decide what kind of drafting this will be, but we'll use an NBA style for now

        currentPlayer = 0

        while len(self.playlist) > 0:
            playerName = self.players[currentPlayer].name
            print(f"\n")
            print(f"It's {playerName}'s turn to pick a song.")
            print("\n")
            self.displayPlaylist()
            print("\n")

            songNumber = int(input(f"Pick a number 1-{len(self.playlist)} "))
            song = self.playlist[songNumber-1]

            self.players[currentPlayer].roster.append(song)
            self.playlist.remove(song)

            if currentPlayer == self.NoPlayers - 1:
                currentPlayer = 0

            else:
                currentPlayer += 1

        print('\n')
        print("Here is everyone's roster: ")




    def getNoPlayers(self):
        return self.NoPlayers

    def getPlaylist(self):
        return self.playlist



    def scoring(self):
        ...

    # def checkNames(self, nom):
    #     for n in self.players:
    #         if nom == n.getName():
    #             return False
    #
    #     else:
    #         return True
    #
    # def checkColours(self):
    #     ...
    #
    # def checkShapes(self):
    #     ...


#main

startGame = input("Do you want to start a new game? (y/n) ")
startGame = startGame.lower()

if startGame == 'y':
    game = Game()
    game.setup()

