import database as db
import time
import sqlite3

def create_mock_teams():
    conn = sqlite3.connect(db.DATABASE_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO teams VALUES (?, ?, ?)", ("test team 1", "test1", "test1@gmail.com"))
    c.execute("INSERT INTO teams VALUES (?, ?, ?)", ("test team 2", "test2", "test2@gmail.com"))
    c.execute("INSERT INTO team_scores VALUES (?, ?, ?)", ("test team 1", 0, time.time()))
    c.execute("INSERT INTO team_scores VALUES (?, ?, ?)", ("test team 2", 0, time.time()))
    c.execute("INSERT INTO team_puzzles VALUES (?, ?, ?)", ("test team 1", False, False))
    c.execute("INSERT INTO team_puzzles VALUES (?, ?, ?)", ("test team 2", False, False))
    conn.commit()
    conn.close()
