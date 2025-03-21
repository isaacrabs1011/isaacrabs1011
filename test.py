chooseExistingPlayer = input("New player. Do you want to choose an existing player (y/n): ")
chooseExistingPlayer = chooseExistingPlayer.lower()

if chooseExistingPlayer == 'y':
    playerExists = True
    targetName = input("What name do you want to look for? ")
    find_statement = '''
    SELECT * FROM players
    WHERE playerName LIKE (?)
    '''

    cursor.execute(find_statement, (targetName,))
    result = cursor.fetchall()
    while len(result) == 0:
        print(f"There is no one in the database called {targetName
    targetName =
        input("What name do you want to look for? ")
        find_statement = '''
                    SELECT * FROM players
                    WHERE playerName LIKE (?)
                    '''
        cursor.execute(find_statement, (targetName,))
        result = cursor.fetchall()

        selectStatement = """
    SELECT playerId, playerName FROM players WHERE playerName LIKE (?);
    """
        cursor.execute(selectStatement, (targetName,))
        playerId, name = cursor.fetchone()
        print(f"Welcome back {name}
        else:
        name = input(f"Player {playerID}, enter your name... ")

        playerId = None
