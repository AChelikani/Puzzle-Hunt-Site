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
                (name text, puzzle1 boolean, puzzle2 boolean)''')
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
    add_team_to_team_scores(team)

def add_team_to_teams(team):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO teams VALUES (?, ?, ?)", (team.name, team.code, team.email))
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
    c.execute("SELECT * FROM team_scores ORDER BY score, last_solve")
    all_teams = c.fetchall()
    conn.close()
    return all_teams

def is_team_unique(team):
    pass
