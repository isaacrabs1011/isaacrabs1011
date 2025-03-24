import random


def rearrangePlayers(list):
    indexes = []
    newPlayers = []
    for i in range(0, len(list)):
        indexes.append(i)

    playerDictionary = {}
    for player in list:
        randomIndex = random.choice(indexes)
        playerDictionary[player] = randomIndex
        indexes.remove(randomIndex)

    for i in range(0, len(list)):
        for item in playerDictionary:
            if playerDictionary[item] == i:
                newPlayers.append(item)

    return newPlayers


print(rearrangePlayers(['Isaac', 'Jeff', 'Bob', 'Nathan']))
