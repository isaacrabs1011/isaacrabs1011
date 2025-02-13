import sqlite3

conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()


create_player_table = """
CREATE TABLE IF NOT EXISTS player (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    colour TEXT NOT NULL,
    shape TEXT NOT NULL
);
"""

playername = "bosh"
playercolour = "red"
playershape = "square"

insertQuery = """
INSERT INTO player (name, colour, shape)
VALUES (?, ?, ?);
"""


cursor.execute(create_player_table)
cursor.execute(insertQuery, (playername, playercolour, playershape))
conn.commit()
conn.close()

