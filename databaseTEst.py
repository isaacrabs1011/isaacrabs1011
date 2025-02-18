import sqlite3

conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()


create_game_table = """
CREATE TABLE IF NOT EXISTS game (
    gameID INTEGER PRIMARY KEY AUTOINCREMENT,
    gameName TEXT
);
"""

create_players_table = """
CREATE TABLE IF NOT EXISTS players (
    playerId INTEGER PRIMARY KEY AUTOINCREMENT,
    gameId INTEGER NOT NULL,
    playerName TEXT NOT NULL,
    finalScore INTEGER NOT NULL,
    FOREIGN KEY (gameId) REFERENCES game(gameID)
);
"""
cursor.execute(create_game_table)
cursor.execute(create_players_table)

gameNumber = 2
gameName = "Hello"

insertQueryGame = ("INSERT INTO game "
                   "VALUES (?)")
cursor.execute(insertQueryGame, "2")



insertQueryPlayers = """
INSERT INTO players (gameId, playerName, finalScore)
VALUES (?, ?, ?)
"""

players = [(gameNumber, "Jonathan", 5),
           (gameNumber, "Nathan", 3),
           (gameNumber, "Jeffrey", 7)
           ]


cursor.executemany(insertQueryPlayers, players)

conn.commit()
conn.close()

