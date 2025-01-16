import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


class Prompts:
    """
    A class for all the prompts
    """
    def __init__(self):
        self.prompts = []

    def getPrompt(self, name):
        """
        :param name: The name of the person who is making the prompt.
        :return: Appends the user's prompt to the list of prompts.
        Gives a confirmation message as well.

        """
        prompt = input(f"{name}, give me a prompt: ")
        self.prompts.append(prompt)


class Player:
    """
    A class to store information about a player.
    """
    def __init__(self):
        self.name = ''
        self.colour = ''
        self.shape = ''
        self.roster = []
        self.rounds = 0
        self.score = 0
        
    def setupPlayer(self):
        """
        Sets up the player's information.
        """
        self.setName()
        # self.setColour()
        # self.setShape()
    
    def setName(self):
        self.name = input("Enter your name... ")
        
    def setColour(self):
        self.colour = input("Choose a colour... ")

    def setShape(self):
        self.shape = input("Choose a shape... ")

    def displayRoster(self):
        """
        Displays the user's roster at that moment in time.
        """
        count = 0
        for item in self.roster:
            print(f"{count+1}: {item}")
            count += 1

    def chooseSong(self):
        """
        User chooses one of the songs from their roster.
        :return: The song they want to choose for the 'battle'.
        """
        print(f"{self.name}, choose one of your songs: \n")
        self.displayRoster()

        songNumber = int(input(f"Pick a number, 1-{len(self.roster)} "))
        song = self.roster[songNumber - 1]
        return song


class Game:
    """
    A class that structures out the game.
    """
    def __init__(self):
        self.players = []
        self.NoPlayers = 0
        self.noRounds = 0
        self.playlist = []
        self.prompts = Prompts()

    def setNumberOfPlayers(self):
        self.NoPlayers = int(input("How many players are playing? "))

    def setPlaylist(self):
        """
        This playlist will be replaced by the user's spotify playlist. This is where I'd integrate the Spotify API
        """
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
        """
        Just shows everyone what the current playlist looks like.
        """
        count = 1
        for item in self.playlist:

            print(f'{count}: {item}')
            count += 1

    def setup(self):
        """
        This is the method that links everything together.
        Playlist -> Draft -> Vote -> Winner
        """
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

        self.setPlaylist()
        self.draft()
        self.vote()
        self.decideWinner()

    def draft(self):
        """
        This is where each player drafts songs to their roster.
        """
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
        """
        This is used for the players to vote for their favourite songs.
        """
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
                count2 = count2 - self.NoPlayers

            elif count1 > (self.NoPlayers-1):
                count1 = count1 - self.NoPlayers

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

    def decideWinner(self):
        print("Now we need to determine the winner.")
        self.displayLeaderboard()

    def displayLeaderboard(self):
        players = []
        for player in self.players:
            if len(players) == 0:
                players.append(player)

            else:
                count = 0
                while count < len(players) and player not in players:
                    if player.score > players[count].score:
                        players.insert(count, player)
                    else:
                        count += 1

                if player not in players:
                    players.append(player)

        for i in range(self.NoPlayers):
            print(f"{i+1}. {players[i].name}: {players[i].score}")

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
