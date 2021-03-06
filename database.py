import sqlite3
import time

DATABASE_NAME = "puzzle_hunt.db"

'''
TEAMS

name   | username | code  | email
------------------------------------------------------
adv18  | adv18    | xyz   | advith.chelikani@gmail.com


TEAM_PUZZLES

name   | puzzle code 1  | puzzle code 2 | ...
---------------------------------------------------
adv18  | true           | false         | ...


TEAM_SCORES

name   | score  | last_solve
---------------------------------------------------
adv18  | 0      | 1540188384

PUZZLE_STATS

name      | solves | attempts
---------------------------------------------------
puzzle_1  | 2      | 12

'''

def create_databases():
    create_teams_database()
    create_team_puzzles_database()
    create_team_scores_database()
    create_puzzle_stats_database()


def create_teams_database():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS teams")
    c.execute('''CREATE TABLE teams
                (name text, username text, code text, email text)''')
    conn.commit()
    conn.close()

def create_team_puzzles_database():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS team_puzzles")
    c.execute('''CREATE TABLE team_puzzles
                (name text)''')
    conn.commit()
    conn.close()

def create_team_scores_database():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS team_scores")
    c.execute('''CREATE TABLE team_scores
                (name text, score number, last_solve real)''')
    conn.commit()
    conn.close()

def create_puzzle_stats_database():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS puzzle_stats")
    c.execute('''CREATE TABLE PUZZLE_STATS
                (name text, solves number, attempts number)''')
    conn.commit()
    conn.close()

def add_puzzles(puzzle_list):
    for puzzle in puzzle_list:
        add_puzzle(puzzle)

def add_puzzle(puzzle):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    # Add row to puzzle_stats
    # Add column to team_puzzles
    c.execute("INSERT INTO puzzle_stats VALUES (?, ?, ?)", (puzzle.get_url_path(), 0, 0))
    c.execute("ALTER TABLE team_puzzles ADD COLUMN {} boolean DEFAULT 0".format(puzzle.get_url_path()))
    conn.commit()
    conn.close()

def add_team(team):
    add_team_to_teams(team)
    add_team_to_puzzles(team)
    add_team_to_team_scores(team)

def add_team_to_teams(team):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO teams VALUES (?, ?, ?, ?)", (team.name, team.username, team.code, team.email))
    conn.commit()
    conn.close()

def add_team_to_puzzles(team):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO team_puzzles (name) VALUES (?)", (team.name,))
    conn.commit()
    conn.close()

def add_team_to_team_scores(team):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO team_scores VALUES (?, ?, ?)", (team.name, team.score, time.time()))
    conn.commit()
    conn.close()

def get_all_teams():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM team_scores ORDER BY score DESC, last_solve ASC")
    all_teams = c.fetchall()
    conn.close()
    return all_teams

def get_team_rank(team_name):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SET @i=0; SELECT id, name, score, @i:=@i+1 AS rank FROM ranking ORDER BY score DESC;")

def get_team_by_username(username):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM teams where username=?", (username,))
    all_teams = c.fetchall()
    print(all_teams)
    conn.close()
    return all_teams

def get_team_by_teamname(team_name):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM teams where name=?", (team_name,))
    all_teams = c.fetchall()
    print(all_teams)
    conn.close()
    return all_teams

def get_puzzles_stats():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM puzzle_stats")
    all_puzzle_stats = c.fetchall()
    conn.close()
    return all_puzzle_stats

def get_team_puzzles(team_name):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM team_puzzles WHERE name=?", (team_name,))
    puzzles = c.fetchall()
    conn.close()
    return puzzles

def get_team_puzzle_solve(team_name, puzzle_name):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT {} FROM team_puzzles WHERE name=?".format(puzzle_name), (team_name,))
    puzzle = c.fetchone()
    conn.close()
    return puzzle

def get_table_teams():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM teams")
    teams = c.fetchall()
    conn.close()
    return teams

def get_table_team_scores():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM team_scores")
    teams = c.fetchall()
    conn.close()
    return teams

def get_table_team_puzzles():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM team_puzzles")
    teams = c.fetchall()
    conn.close()
    return teams

def update_team_score(team_name):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("UPDATE team_scores SET score=score+1, last_solve=? WHERE name=?", (time.time(), team_name))
    conn.commit()
    conn.close()

def update_team_solves(team_name, puzzle_name):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("UPDATE team_puzzles SET {}=? WHERE name=?".format(puzzle_name), (True, team_name))
    conn.commit()
    conn.close()

def update_puzzle_solve(puzzle_name):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("UPDATE puzzle_stats SET solves=solves+1, attempts=attempts+1 WHERE name=?", (puzzle_name,))
    conn.commit()
    conn.close()

def update_puzzle_attempts(puzzle_name):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("UPDATE puzzle_stats SET attempts=attempts+1 WHERE name=?", (puzzle_name,))
    conn.commit()
    conn.close()

def update_username(team_name, username):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("UPDATE teams SET username=? WHERE name=?", (username, team_name))
    conn.commit()
    conn.close()

def update_email(team_name, email):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("UPDATE teams SET email=? WHERE name=?", (email, team_name))
    conn.commit()
    conn.close()

def update_code(team_name, code):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("UPDATE teams SET code=? WHERE name=?", (code, team_name))
    conn.commit()
    conn.close()

def delete_team(team_name):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM teams WHERE name=?", (team_name,))
    c.execute("DELETE FROM team_scores WHERE name=?", (team_name,))
    c.execute("DELETE from team_puzzles WHERE name=?", (team_name,))
    conn.commit()
    conn.close()
