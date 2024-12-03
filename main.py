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

    def chooseSong(self):
        print(f"{self.name}, choose one of your songs: \n")
        self.displayRoster()

        songNumber = int(input(f"Pick a number, 1-{len(self.roster)} "))
        song = self.roster[songNumber - 1]
        return song
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
        self.noRounds = 0
        self.playlist = []
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
        self.noRounds = noP * 2

        for i in range(noP):
            player = Player()
            player.setupPlayer()
            self.players.append(player)
            print('\n')

        for item in self.players:
            self.prompts.getPrompt(item.name)

        Game.setPlaylist(self)
        Game.draft(self)
        Game.vote(self)

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
        finished = False
        count1 = 0
        count2 = 1
        while not finished:
            p1 = self.players[count1]
            p2 = self.players[count2]

            restOfPlayers = []
            for item in self.players:
                if item != p1 and item != p2:
                    restOfPlayers.append(item)

            prompt = random.choice(self.prompts.prompts)

            print(f"It's {p1.name} vs {p2.name} \n")
            print("Your prompt is: \n")
            print(prompt, '\n')

            p1song = p1.chooseSong()
            p2song = p2.chooseSong()

            for thing in restOfPlayers:
                




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
