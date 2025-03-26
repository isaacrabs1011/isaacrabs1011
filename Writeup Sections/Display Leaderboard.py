def displayLeaderboard(players):
    leaderboard = []
    for player in players:
        if len(leaderboard) == 0:
            leaderboard.append([player, players[player]])

        else:
            count = 0
            while count < len(leaderboard) and [player, players[player]] not in leaderboard:
                if players[player] > leaderboard[count][1]:
                    leaderboard.insert(count, [player, players[player]])
                else:
                    count += 1

            if [player, players[player]] not in leaderboard:
                leaderboard.append([player, players[player]])

    for i in range(len(players)):
        print(f"{i + 1}. {leaderboard[i][0]}: {leaderboard[i][1]}")


displayLeaderboard({'Isaac': 2,
                    'Nathan': 1,
                    'Bob': 4,
                    'Jeff': 0})
