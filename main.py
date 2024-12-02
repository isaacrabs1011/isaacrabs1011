import time
import random


class Prompts:
    def __init__(self):
        self.prompts = []

    def getPrompt(self, name):
        prompt = input(f"{name}, give me a prompt: ")
        self.prompts.append(prompt)


class Player:
    def __init__(self):
        self.name = ''
        self.colour = ''
        self.shape = ''
        self.roster = []
        self.rounds = 0
        
    def setupPlayer(self):
        self.setName()
        # self.setColour()
        # self.setShape()

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
#
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
        self.score = 0
        self.prompts = Prompts()

    def setNumberOfPlayers(self):
        self.NoPlayers = int(input("How many players are playing? "))

    def setPlaylist(self):

        # giving stats + attribute to an initial list of songs
        # Artist, Genre
        self.playlist = [
            "Noid",
            "Bennie and The Jets",
            "Mojo Pin",
            "Daughter of a Cop",
            "Reincarnated"
        ]

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

        for item in self.players:
            self.prompts.getPrompt(item.name)

        Game.setPlaylist(self)
        Game.draft(self)

    def draft(self):

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

        for item in self.players:
            print(f"{item.name}:")
            item.displayRoster()
            print('\n')

    def vote(self):
        prompt = random.choice(self.prompts.prompts)
        players = random.choice(self.players) * 2

    def getNoPlayers(self):
        return self.NoPlayers

    def getPlaylist(self):
        return self.playlist

# main


startGame = input("Do you want to start a new game? (y/n) ")
startGame = startGame.lower()

if startGame == 'y':
    game = Game()
    game.setup()
    