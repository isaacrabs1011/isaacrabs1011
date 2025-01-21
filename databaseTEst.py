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

insertQuery = """
INSERT INTO player (name, colour, shape)
VALUES ('isaac', 'orange', 'square');
"""


cursor.execute(create_player_table)
cursor.execute(insertQuery)
conn.commit()
conn.close()

