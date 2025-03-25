import random

players = []
prompts = []
GameRoundsPlayed = 0
def rearrangePlayers(l):
    ...

NoPlayers = 0
noRounds = 0


finished = False
count1 = 0
count2 = 1
while not finished:
    p1 = players[count1]
    p2 = players[count2]

    restOfPlayers = []
    for item in players:
        if item != p1 and item != p2:
            restOfPlayers.append(item)

    prompt = random.choice(prompts)

    print(f"It's {p1} vs {p2} \n")
    print("Your prompt is: \n")
    print(prompt, '\n')

    p1song = p1.chooseSong()  # Assumes that p1 and p2 is an instantiation of a class.
    p2song = p2.chooseSong()
    p1vote = 0
    p2vote = 0

    print("\n")
    print("Choose one of these songs:")

    print(f"1. {p1song} ")
    print(f"2. {p2song}")
    print("\n")

    for player in restOfPlayers:
        vote = int(input(f"{player} pick a song, choose 1 or 2: "))
        if vote == 1:
            p1vote += 1

        elif vote == 2:
            p2vote += 1

    print("The votes are in.")  # Confirmation that voting is over for this round.

    if p1vote > p2vote:
        print(f"{p1} won with {p1vote} votes to {p2}'s {p2vote} votes. ")
        print("\n")

        p1.score += p1vote  # Player 1's game score increases by the number of votes they received in this round.
        print(f"{p1}'s score: {p1.score}")
        print(f"{p2}'s score: {p2.score}")
        print("\n")

    elif p2vote > p1vote:
        print(f"{p2} won with {p2vote} votes to {p1}'s {p1vote} votes. ")
        print("\n")

        p2.score += p2vote  # Player 2's game score increases by the number of votes they received in this round
        print(f"{p2}'s score: {p2.score}")
        print(f"{p1}'s score: {p1.score}")
        print("\n")

    elif p1vote == p2vote:  # If they both received the same number of votes.
        print(f"{p2} and {p1} drew with each other with {p1vote} votes. ")
        print("\n")

        p1.score += p1vote
        p2.score += p2vote  # Both players' scores increase.

        print(f"{p1}'s score: {p1.score}")
        print(f"{p2}'s score: {p2.score}")
        print("\n")

    p1.rounds += 1  # This changes the number of rounds each player has played.
    p2.rounds += 1

    count1 += 2  # Both counts are incremented twice to move onto the next duo of players in the players list.
    count2 += 2

    # This will check whether everyone has played the same number of rounds
    hasEveryonePlayed = []
    targetRounds = players[0].rounds

    for player in players:  # Loops through each player in the players list.
        if player.rounds == targetRounds:
            pass
        else:
            hasEveryonePlayed.append(False)

    if len(hasEveryonePlayed) == 0:
        rearrangePlayers(players)

    if count2 > (NoPlayers - 1):  # If count2 exceeds the number of players, it'll loop round to the beginning of the
        # self.players list to index 0 / index 1, depending on how much larger than (self.NoPLayers - 1) count2 will be.
        count2 = count2 - NoPlayers

    if count1 > (NoPlayers - 1):
        count1 = count1 - NoPlayers

    GameRoundsPlayed += 1
    if GameRoundsPlayed == noRounds:  # When the number of roundsPlayed is the number of rounds that
        # should have been played, the voting ends.
        finished = True
