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
        self.score = 0
        
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
            count += 1

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
            "Reincarnated",
            "Happy",
            "Feather",
            "Mercury",
            "06 Dreamin",
            "Nothing's Promised"
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
            p1vote = 0
            p2vote = 0

            print("\n")
            print("Choose one of these songs:")
            print(f"1. {p1song} ")
            print(f"2. {p2song}")
            print("\n")

            for thing in restOfPlayers:
                vote = int(input(f"{thing.name} pick a song, choose 1 or 2: "))
                if vote == 1:
                    p1vote += 1

                elif vote == 2:
                    p2vote += 1

            for i in range(3):
                print(".")
                print("..")
                print("...")

            print("The votes are in.")
            if p1vote >= p2vote:
                print(f"{p1.name} won with {p1vote} votes to {p2.name}'s {p2vote} votes. ")
                print("\n")

                p1.score += p1vote
                print(f"{p1.name}'s score: {p1.score}")
                print(f"{p2.name}'s score: {p2.score}")
                print("\n")

            elif p2vote >= p1vote:
                print(f"{p2.name} won with {p2vote} votes to {p1.name}'s {p1vote} votes. ")
                print("\n")

                p2.score += p2vote
                print(f"{p2.name}'s score: {p2.score}")
                print(f"{p1.name}'s score: {p1.score}")
                print("\n")

            elif p1vote == p2vote:
                print(f"{p2.name} and {p1.name} drew with each other with {p1vote} votes. ")
                print("\n")

                p1.score += p1vote
                p2.score += p2vote

                print(f"{p1.name}'s score: {p1.score}")
                print(f"{p2.name}'s score: {p2.score}")
                print("\n")

            p1.rounds += 1
            p2.rounds += 1

            count1 += 2
            count2 += 2

            if count2 > (self.NoPlayers-1):
                count2 = count2 - (self.NoPlayers)

            elif count1 > (self.NoPlayers-1):
                count1 = count1 - (self.NoPlayers)

            complete = []

            for player in self.players:
                if player.rounds == 2:
                    complete.append(True)
                else:
                    complete.append(False)

            if False in complete:
                pass
            else:
                finished = True




            # if count2 + 2 > len(self.players)-1:
            #     count2 = (count2 + 2) - len(self.players)-1
            #
            # elif count1 + 2 > len(self.players)-1:
            #     count1 = (count1 + 2) - (len(self.players)-1)
            #
            # else:
            #     count1 += 2
            #     count2 += 2
            #
            # if self.players[self.NoPlayers - 1].rounds == 2:
            #     finished = True


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
