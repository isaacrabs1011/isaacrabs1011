import random
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sqlite3

# Creating a cursor for my SQLite database.
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

# Creating and executing all the relevant tables for my database.
# 1. It will check if the table already exists.
# 2. If it doesn't, then it will create a table containing all the correct parameters in the database
# Tables: game, players, prompts, playerGame, playerGameRoster,

create_game_table = """
CREATE TABLE IF NOT EXISTS game ( 
    gameID INTEGER PRIMARY KEY AUTOINCREMENT,
    numberOfPlayers INTEGER NOT NULL,
    playlistLink TEXT NOT NULL,
    rounds INTEGER NOT NULL
);
"""

cursor.execute(create_game_table)

create_players_table = """
CREATE TABLE IF NOT EXISTS players (
    playerId INTEGER PRIMARY KEY AUTOINCREMENT,
    playerName TEXT NOT NULL
);
"""
cursor.execute(create_players_table)

create_prompts_table = """
CREATE TABLE IF NOT EXISTS prompts(
    promptID INTEGER PRIMARY KEY AUTOINCREMENT,
    gameId INTEGER NOT NULL,
    promptText TEXT NOT NULL,
    FOREIGN KEY (gameId) REFERENCES game(gameID)
)
"""
cursor.execute(create_prompts_table)

create_playerGame_table = """
CREATE TABLE IF NOT EXISTS playerGame(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gameID INTEGER NOT NULL,
    playerID INTEGER NOT NULL,
    playerScore INTEGER NOT NULL,
    FOREIGN KEY (gameID) REFERENCES game(gameID),
    FOREIGN KEY (playerID) REFERENCES players(playerId)
)
"""
cursor.execute(create_playerGame_table)

create_playerGameRoster_table = """
CREATE TABLE IF NOT EXISTS playerGameRoster(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
        gameID INTEGER NOT NULL,
        playerID INTEGER NOT NULL,
        playerSong TEXT NOT NULL,
        FOREIGN KEY (gameID) REFERENCES game(gameID),
        FOREIGN KEY (playerID) REFERENCES players(playerId)
)
"""
cursor.execute(create_playerGameRoster_table)


# Class which will store + manage all the prompts.
class Prompts:
    def __init__(self):
        self.prompts = []
        # Parameter which contains all the prompts.

    def getPrompt(self, name):
        # The 'name' parameter is the name of the user.

        prompt = input(f"{name}, give me a prompt: ")  # Input asking for the prompt.
        self.prompts.append(prompt)  # Appends the prompt given by the user to the list of prompts for the game.


# Class which will store + manage all information about a specific player.
class Player:
    def __init__(self):
        self.name = ''  # The name of the player.
        self.playerExists = False  # Used later in the program to determine whether a player exists in the database.
        self.playerId = None  # Declared as None but will change depending on whether the player already exists in
        # the database or if they need to be added.
        self.colour = ''  # Was created assuming a GUI would be created at some point.
        self.shape = ''  # Was created assuming a GUI would be created at some point.
        self.initialRoster = []  # By the end of the game the roster will be empty, but since I want to save the
        # roster the player used to win, I need to keep a record of what songs they had at the end of the drafting
        # phase and at the start of the voting phase.
        self.roster = []  # The roster that will actually be used in the voting stage.
        self.rounds = 0  # The number of rounds that the player has played. Modified during the voting stage.
        self.score = 0  # The score of the user.

    def setupPlayer(self, players, playerId):
        # This method sets up the entire player.

        self.setName(players, playerId)  # Will set the name of the user by determining whether the user
        # is already in the database.

        # self.setColour() - was created assuming the GUI would be made.
        # self.setShape() - was created assuming the GUI would be made.

    # def validateName(self, players): - This was supposed to be a part of a series of methods checking and testing
    # whether the user's inputs were valid or invalid.
    #     if self.name not in players:
    #         return True
    #
    #     else:
    #         print("This name is already taken")
    #         return False

    def setName(self, players, playerID):
        # Will set the player's name.
        # PlayerID isn't the playerID in the database, it's their index in the
        # self.players attribute list in the Game Class.

        chooseExistingPlayer = input("New player. Do you want to choose an existing player (y/n): ")
        # Input which will determine whether the user wants to choose someone already in the database.
        chooseExistingPlayer = chooseExistingPlayer.lower()  # Will make the user's input lowercase for simplicity.

        if chooseExistingPlayer == 'y':
            # This is what happens whether the user wants to choose a player already existing in the database.
            self.playerExists = True  # It automatically assumes that the player already exists in the database.
            targetName = input("What name do you want to look for? ")

            find_statement = '''
            SELECT * FROM players
            WHERE playerName LIKE (?)
            '''

            cursor.execute(find_statement, (targetName,))  # Will try to find whether this player actually exists.
            result = cursor.fetchall()  # 'result' will store the number of players in the database which have the
            # same name as the targetName. If 'result' is 0, it means the player doesn't exist in the database.

            while len(result) == 0:  # Will loop around until the user enters a valid name.
                print(f"There is no one in the database called {targetName}")  # Output message telling the user
                # whether this name exists.

                targetName = input("What name do you want to look for? ")
                find_statement = '''
                            SELECT * FROM players
                            WHERE playerName LIKE (?)
                            '''
                cursor.execute(find_statement, (targetName,))
                result = cursor.fetchall()

            selectStatement = """
            SELECT playerId, playerName FROM players WHERE playerName LIKE (?);
            """
            cursor.execute(selectStatement, (targetName,))  # Now that it's been determined that the player exists in
            # the database, the cursor will locate the details about this player.

            self.playerId, self.name = cursor.fetchone()  # self.playerId will store the playerId of the existing
            # player in the database. This will be used later when saving the game - so that you can associate 1
            # player with many games and 1 game with many players.

            print(f"Welcome back {self.name}!")  # A little message proving to the user that they've been recognised.

        else:
            self.name = input(f"Player {playerID}, enter your name... ")  # PlayerID (i.e. Player 1, Player 2) in the
            # local game itself not the database.

            self.playerId = None  # Maintains the self.playerId as None as they don't exist in the database, meaning
            # that they won't have a playerId in the database which in turn means that they will need to be added to
            # the database at the end of the game.

    def setColour(self):
        # Was created assuming the GUI would be made.
        self.colour = input("Choose a colour... ")

    def setShape(self):
        # Was created assuming the GUI would be made.
        self.shape = input("Choose a shape... ")

    def displayRoster(self):
        # Displays the roster of the player at the time this method is called.
        count = 0
        for item in self.roster:  # Formats it in the form: 1. (song name)
            print(f"{count + 1}: {item}")
            count += 1

    def chooseSong(self):
        # The user will choose a song from their roster which best fits the prompt that they've been given.
        # This method will return the song and will remove it from the player's roster.
        print(f"{self.name}, choose one of your songs: \n")
        self.displayRoster()  # Reminds the user of what songs are in their roster.

        songNumber = int(input(f"Pick a number, 1-{len(self.roster)} "))  # Asks for the position of their chosen
        # song instead of the name of the song. This is to avoid being unable to select a song containing funky
        # symbols or emojis or letters in another language.

        song = self.roster[songNumber - 1]  # The index in the list is going to be 1 smaller than the position shown
        # when the playlist is displayed.

        self.roster.remove(song)  # Removes the song from the player's roster
        return song  # Returns the song


class Game:
    # The class that determines all factors of the game.
    def __init__(self):
        self.players = []  # A list of all the instantiations of the player class. (i.e. all the player objects.)
        self.NoPlayers = 0  # The number of players in the game.
        self.noRounds = 0  # The ideal number of rounds in a game
        self.roundsPlayed = 0  # The number of rounds played currently.
        self.playlist = []  # An array containing all the songs in the playlist withdrawn from the Spotify API.
        self.playlistLink = ""  # The link to the Spotify playlist. Will be used when saving the game.
        self.prompts = Prompts()  # Prompts are stored in a separate class but can be accessed from within the game.
        self.songsPerPerson = 0  # The chosen amount of songs per person.

    def setNoSongsPerPerson(self):
        # Sets the number of songs per person.
        print(f"Your playlist has {len(self.playlist)} songs.")  # Tells the user how many songs there are currently
        # in the playlist.
        print(f"There are {len(self.players)} players")  # Tells the user how many players there are in the game.
        print(
            f"I recommend playing with 10 songs per person, but the maximum you can play with is {len(self.playlist) // len(self.players)}")
        self.songsPerPerson = int(input("How many songs do you want each person to have in their roster? "))  # Asks
        # the user how many songs they want each player to have in their roster.

        nOsongsInPlaylist = self.songsPerPerson * len(self.players)  # Local variable which will automatically
        # calculate how many songs there must be in the playlist to ensure that every player gets the same amount.
        while len(self.playlist) > nOsongsInPlaylist:  # This while loop wil remove the excess songs in the playlist
            # to ensure that there are nOsongsInPlaylist.
            self.playlist.pop(len(self.playlist) - 1)

        print("\n")  # Whitespace so that it's easier to read.
        print("This is what your playlist looks like now:")
        time.sleep(1)  # Pauses the program for 1 second so that the game doesn't feel too fast-paced.
        self.displayPlaylist()  # Displays the updated playlist to the group of people.
        self.noRounds = len(self.playlist) // self.NoPlayers

    def setNumberOfPlayers(self):
        self.NoPlayers = int(input("How many players are playing? "))
        while self.NoPlayers < 3:  # It's impossible to have a game without 3 or more players. If Player 1 is playing
            # against Player 2, who is voting for the song that best fits the prompt?
            print("You have to have more than 3 players. ")
            self.NoPlayers = int(input("How many players are playing? "))  # Loops until the user states that there
            # are 3 or more players playing.

    def setPlaylist(self):
        # Sets the playlist for the current game.
        SPOTIPY_CLIENT_ID = '5143755320f74541986016c151d8b004'  # My Spotify ClientID.
        SPOTIPY_CLIENT_SECRET = '8466dcc0498847eabf4cc3b83b6a0742'  # My Spotify ClientSecret.
        SPOTIPY_REDIRECT_URI = 'http://localhost.callback'  # Would have been used for making the GUI.

        playlistID = input("Go to your Spotify profile and choose one of your playlists. \nClick on the 3 dots and press share then Copy Link. \nPaste it here: ")
        # This asks the user for the link to their desired Spotify Playlist.
        self.playlistLink = playlistID  # Stores the playlist link so that it can be saved later.
        auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)  # Authenticates my Spotify
        # Credentials using my Spotify Client ID and Client Secret.
        sp = spotipy.Spotify(auth_manager=auth_manager)  # Create a Spotify API client using the authenticated session.
        playlist = sp.playlist(playlistID)
        for item in playlist['tracks']['items']:  # Loop through each track item in the playlist
            track = item['track']  # Extract track details
            self.playlist.append(track['artists'][0]['name'] + ' - ' + track['name'])  # Print the first artist's
            # name and the track title

        print("\n")

    def displayPlaylist(self):
        # Displays the playlist.
        count = 1
        for item in self.playlist:
            print(f'{count}: {item}')  # Displays it nicely.
            count += 1

    def setup(self):
        # Links all the methods together. Uses procedural programming.
        self.setNumberOfPlayers()  # Sets the number of players in the game.
        self.noRounds = self.NoPlayers * 2  # Ensures that everyone plays the same number of rounds.

        for i in range(self.NoPlayers):
            player = Player()  # Instantiates a player as a player.
            players = self.players
            player.setupPlayer(players, i + 1)  # Sets up the player.
            self.players.append(player)  # Appends the player object to the list of players.
            print('\n')

        for item in self.players:
            self.prompts.getPrompt(item.name)  # Asks each player for a prompt.

        print("\n")

        self.setPlaylist()  # Calls the method that will set the playlist.
        self.setNoSongsPerPerson()  # Calls the method which will set the number of songs per person.

    def draft(self):
        # Where the main drafting process happens.
        currentPlayer = 0  # Initialises the currentPlayer variable to 0

        while len(self.playlist) > 0:  # Whilst there are still songs in the playlist, players will keep drafting
            # songs into their roster.
            playerName = self.players[currentPlayer].name  # Gets the current player's name so that they can get a
            # personalised message.
            print(f"\n")
            print(f"It's {playerName}'s turn to pick a song.")
            print("\n")
            time.sleep(1)  # Slows down the pace of the game so that it doesn't seem too quick.
            self.displayPlaylist()  # Displays the current playlist so the current player knows which songs are
            # available to choose.
            print("\n")

            songNumber = int(input(f"Pick a number 1-{len(self.playlist)} "))  # Display message.
            song = self.playlist[songNumber - 1]

            self.players[currentPlayer].roster.append(song)  # Puts the chosen song into the current player's roster.
            self.players[currentPlayer].initialRoster.append(song)  # Adds it to the initial roster as well.
            self.playlist.remove(song)  # Removes the song from the game playlist.

            if currentPlayer == self.NoPlayers - 1:  # Checks to see whether that's the last player in the list,
                # which would mean that the program loops back around to the first player in the players list.
                currentPlayer = 0

            else:
                currentPlayer += 1

        print('\n')
        print("Here is everyone's roster: ")

        for item in self.players:  # Displays everyone's roster.
            print(f"{item.name}:")
            item.displayRoster()
            print('\n')

    def vote(self):
        # Where the voting process happens.
        finished = False
        count1 = 0
        count2 = 1
        while not finished:
            p1 = self.players[count1]  # Player 1 is the player object at index count1.
            p2 = self.players[count2]  # Player 2 is the player object at index count2.

            restOfPlayers = []
            for item in self.players:
                # Will separate the rest of the players from the 2 players that are playing.
                if item != p1 and item != p2:
                    restOfPlayers.append(item)

            prompt = random.choice(self.prompts.prompts)  # Will select a random prompt for the match-up.

            print(f"It's {p1.name} vs {p2.name} \n")  # Display message
            print("Your prompt is: \n")
            print(prompt, '\n')

            p1song = p1.chooseSong()  # Player 1 chooses a song which best fits the prompt presented to them.
            p2song = p2.chooseSong()  # Player 2 chooses a song which best fits the prompt presented to them.
            p1vote = 0  # Initialises the number of votes Player 1 has received
            p2vote = 0  # Initialises the number of votes Player 2 has received

            print("\n")
            print("Choose one of these songs:")  # Displays the songs chosen for the prompt so that the voters can
            # clearly see their choice.

            print(f"1. {p1song} ")  # Displays the first song for the voters to see.
            print(f"2. {p2song}")  # Displays the second song for the voters to see.
            print("\n")

            for thing in restOfPlayers:  # Loops through the players not playing (i.e. the voters).
                vote = int(input(f"{thing.name} pick a song, choose 1 or 2: "))  # Asks the voters to choose a song 1
                # or 2.
                if vote == 1:  # If the voter chooses Player 1's song, p1vote increments.
                    p1vote += 1

                elif vote == 2:  # If the voter chooses Player 2's song, p2vote increments.
                    p2vote += 1

            time.sleep(1)

            print("The votes are in.")  # Confirmation that voting is over for this round.
            if p1vote > p2vote:  # If Player 1 received more votes than Player 2.
                print(f"{p1.name} won with {p1vote} votes to {p2.name}'s {p2vote} votes. ")
                print("\n")

                p1.score += p1vote  # Player 1's game score increases by the number of votes they received in this
                # round.
                print(f"{p1.name}'s score: {p1.score}")  # Display message showing both player's current score.
                print(f"{p2.name}'s score: {p2.score}")
                print("\n")

            elif p2vote > p1vote:  # If Player 2 received more votes than Player 1.
                print(f"{p2.name} won with {p2vote} votes to {p1.name}'s {p1vote} votes. ")
                print("\n")

                p2.score += p2vote  # Player 2's game score increases by the number of votes they received in this
                # round.
                print(f"{p2.name}'s score: {p2.score}")
                print(f"{p1.name}'s score: {p1.score}")
                print("\n")

            elif p1vote == p2vote:  # If they both received the same number of votes.
                print(f"{p2.name} and {p1.name} drew with each other with {p1vote} votes. ")
                print("\n")

                p1.score += p1vote
                p2.score += p2vote
                # Both players' scores increase.

                print(f"{p1.name}'s score: {p1.score}")
                print(f"{p2.name}'s score: {p2.score}")
                print("\n")

            p1.rounds += 1  # This changes the number of rounds each player has played.
            p2.rounds += 1

            count1 += 2  # Both counts are incremented twice to move onto the next duo of players in the players list.
            count2 += 2

            if count2 > (self.NoPlayers - 1):  # If count2 exceeds the number of players, it will loop round to the
                # beginning of the self.players list to either index 0 or index 1, depending on how much larger than
                # (self.NoPLayers - 1) count2 be.
                count2 = count2 - self.NoPlayers

            if count1 > (self.NoPlayers - 1):  # Same thing applies to count1.
                count1 = count1 - self.NoPlayers

            self.roundsPlayed += 1  # The number of roundsPlayed increases.
            if self.roundsPlayed == self.noRounds:  # When the number of roundsPlayed is the number of rounds that
                # should have been played, the voting ends.
                finished = True

    def decideWinner(self):
        print("Now we need to determine the winner.") # Display message
        self.displayLeaderboard()  # Calls the displayLeaderboard function.

    def displayLeaderboard(self):  # Displays the leaderboard at the end of the game.
        leaderboard = []  # The list containing the players in order of their score.
        for player in self.players:
            if len(leaderboard) == 0:  # If no one's in the leaderboard yet the player is added for the time being.
                leaderboard.append(player)

            else:
                count = 0
                while count < len(leaderboard) and player not in leaderboard:  # If the player isn't in the
                    # leaderboard yet then an algorithm will find where it should go into this.

                    if player.score > leaderboard[count].score:  # If the current player's score is larger than the
                        # score of the player in the leaderboard at index 'count', the current player gets inserted
                        # into the leaderboard at that index and pushes the other player along.
                        leaderboard.insert(count, player)
                    else:
                        count += 1

                if player not in leaderboard:  # If the current player's score is the smallest so far, it gets added
                    # to the bottom of the leaderboard.
                    leaderboard.append(player)

        for i in range(self.NoPlayers):  # Displays the leaderboard.
            print(f"{i + 1}. {leaderboard[i].name}: {leaderboard[i].score}")

    def getPlaylist(self):
        return self.playlist

    def turnPromptsSaveable(self, gameID):  # Will export the prompts in a format that can be stored in the SQL
        # Database.
        # The gameID is a parameter that will be given when saving the game.
        prompts = []
        for prompt in self.prompts.prompts:
            prompts.append((gameID, prompt))  # Makes it a tuple so that it can be saved.

        return prompts

    def saveGame(self):  # Where all the saving happens.
        doYouSave = input("Do you want to save this game? (y/n) ")  # Asks the user if they want to save.
        doYouSave = doYouSave.lower()

        if doYouSave == 'y':
            print("The following will be saved: \n"  # Lists all the things being saved.
                  "1. The game: \n"
                  "   - Number of Players \n"
                  "   - Link to Spotify Playlist \n"
                  "   - The prompts in the game. \n"
                  "2. The players: \n"
                  "   - Player Name \n"
                  "   - Player Song \n"
                  "   - Songs in the player's roster. \n"
                  )

            insertQueryGame = """
                        INSERT INTO game (numberOfPlayers, playlistLink, rounds)
                        VALUES  (?, ?, ?) 
            """
            # Initialises the insert query for the game table.

            cursor.execute(insertQueryGame, (self.NoPlayers, self.playlistLink, self.noRounds,))  # Executes the query.

            gameId = cursor.lastrowid  # Gets the game ID of this game so that it can be used to save other things.

            # Query for players
            insertQueryPlayers = """
                        INSERT INTO players (playerName)
                        VALUES (?)
            """

            # Query for game.
            insertQueryPlayerGame = """
                        INSERT INTO playerGame(gameID, playerID, playerScore)
                        VALUES (?,?,?)
            """

            # Query for the roster
            insertQueryPlayerGameRoster = """
                        INSERT INTO playerGameRoster(gameID, playerID, playerSong)  
                        VALUES (?,?,?)          
            """

            for player in self.players:  # Loops through each player in the game.
                if not player.playerExists:  # If the player isn't in the database yet, it adds them to it.
                    cursor.execute(insertQueryPlayers, (player.name,))  # Executes the player query.
                    player.playerId = cursor.lastrowid  # Gets the playerID for this new player.

                cursor.execute(insertQueryPlayerGame, (gameId, player.playerId, player.score,))  # Inserts player
                # into PlayerGame table.
                for song in player.initialRoster:  # For each player, it adds each song from their original roster
                    # individually into the database.
                    cursor.execute(insertQueryPlayerGameRoster, (gameId, player.playerId, song,))  # Roster query.

            insertQueryPrompts = """
                        INSERT INTO prompts (gameId, promptText)
                        VALUES (?, ?)
                        """

            prompts = self.turnPromptsSaveable(gameId)  # Turns the prompts into a savable format.

            cursor.executemany(insertQueryPrompts, prompts)  # Executes all the prompts.

            conn.commit()
            conn.close()  # Finishes the amendments to the database.


# main

startGame = input("Do you want to start a new game? (y/n) ")  # Asks confirmation of the user to start the game.
startGame = startGame.lower()  # simplifies it.

if startGame == 'y':
    game = Game()  # Instantiates the game object.
    game.setup()  # Begins the procedural programming.
    game.draft()  # Drafting phase.
    game.vote()  # Voting phase.
    game.decideWinner()  # Leaderboard phase.
    game.saveGame()  # Saves the game.