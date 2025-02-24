import sqlite3

conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()


create_game_table = """
CREATE TABLE IF NOT EXISTS game (
    gameID INTEGER PRIMARY KEY AUTOINCREMENT,
    numberOfPlayers INTEGER
);
"""

cursor.execute(create_game_table)

create_players_table = """
CREATE TABLE IF NOT EXISTS players (
    playerId INTEGER PRIMARY KEY AUTOINCREMENT,
    gameId INTEGER NOT NULL,
    playerName TEXT NOT NULL,
    finalScore INTEGER NOT NULL,
    FOREIGN KEY (gameId) REFERENCES game (gameID)
);
"""
cursor.execute(create_players_table)

#gameNumber = 2
noPlayers = 5

insertQueryGame = ("INSERT INTO game (numberOfPlayers)"
                   "VALUES  (?)")
cursor.execute(insertQueryGame, (noPlayers,) )

gameId = cursor.lastrowid



insertQueryPlayers = """
INSERT INTO players (gameId, playerName, finalScore)
VALUES (?, ?, ?)
"""

players = [(gameId, "Jonathan", 5),
           (gameId, "Nathan", 3),
           (gameId, "Jeffrey", 7)
           ]


cursor.executemany(insertQueryPlayers, players)

conn.commit()
conn.close()

