import sqlite3

conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()


create_game_table = """
CREATE TABLE game (
    gameID INTEGER PRIMARY KEY AUTOINCREMENT
);
"""

create_players_table = """
CREATE TABLE players (
    playerId INTEGER PRIMARY KEY AUTOINCREMENT,
    gameId INTEGER NOT NULL,
    playerName TEXT NOT NULL,
    finalScore INTEGER NOT NULL,
    FOREIGN KEY (gameId) REFERENCES game(gameID)
);
"""

insertQueryGame = """
INSERT INTO game (gameId)
VALUES (?);
"""

insertQueryPlayers = """
INSERT INTO players (playerID, gameId, playerName, finalScore)
VALUES (?)
"""

gameNumber = 1
players = [(1, gameNumber, "Jonathan", 5),
           (2, gameNumber, "Nathan", 3),
           (3, gameNumber, "Jeffrey", 7)
           ]


cursor.execute(create_players_table)
cursor.execute(create_game_table)
cursor.execute(insertQueryGame, 1)
cursor.execute(insertQueryPlayers, players[0])

conn.commit()
conn.close()

