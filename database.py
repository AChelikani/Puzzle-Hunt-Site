import sqlite3
import time

DATABASE_NAME = "puzzle_hunt.db"

'''
TEAMS

name   | code | email                      | score
---------------------------------------------------
adv18  | xyz  | advith.chelikani@gmail.com | 0


TEAM_PUZZLES

name   | puzzle code 1  | puzzle code 2 | ...
---------------------------------------------------
adv18  | true           | false         | ...


TEAM_SCORE

name   | score  | last_solve
---------------------------------------------------
adv18  | 0      | 1540188384

'''

def create_databases():
    create_teams_database()
    create_team_puzzles_database()
    create_team_scores_database()


def create_teams_database():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS teams")
    c.execute('''CREATE TABLE teams
                (name text, code text, email text)''')
    conn.commit()
    conn.close()

def create_team_puzzles_database():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS team_puzzles")
    c.execute('''CREATE TABLE team_puzzles
                (name text, puzzle_1 boolean, puzzle_2 boolean)''')
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

def add_team(team):
    add_team_to_teams(team)
    add_team_to_puzzles(team)
    add_team_to_team_scores(team)

def add_team_to_teams(team):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO teams VALUES (?, ?, ?)", (team.name, team.code, team.email))
    conn.commit()
    conn.close()

def add_team_to_puzzles(team):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO team_puzzles VALUES (?, ?, ?)", (team.name, False, False))
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

def get_team_by_passcode(code):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM teams WHERE code=?", (code,))
    all_teams = c.fetchall()
    conn.close()
    return all_teams

def update_team_score(team_name):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("UPDATE team_scores SET score=score+1, last_solve=? WHERE name=?", (time.time(), team_name))
    conn.commit()
    conn.close()

def get_team_puzzle_solve(team_name, puzzle_name):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT {} FROM team_puzzles WHERE name=?".format(puzzle_name), (team_name,))
    puzzle = c.fetchone()
    conn.close()
    return puzzle

def update_team_solves(team_name, puzzle_name):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("UPDATE team_puzzles SET {}=? WHERE name=?".format(puzzle_name), (True, team_name))
    conn.commit()
    conn.close()
