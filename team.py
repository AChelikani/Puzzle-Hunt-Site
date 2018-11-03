import database as db
import helpers
from objects import TeamScore, Team
import puzzle

def db_team_to_team(row):
    return Team(row[0], row[1], row[2], row[3])

def is_team_unique(team):
    all_teams = db.get_team_by_teamname(team.name)
    if not all_teams:
        return True
    return False

def is_username_unique(team):
    all_teams = db.get_team_by_username(team.username)
    if not all_teams:
        return True
    return False

def is_team_code_unique(team_code):
    all_teams = db.get_all_teams()
    for row in all_teams:
        if (team_code == row[1]):
            return False
    return True

def get_all_teams_scores():
    team_scores = []
    all_teams = db.get_all_teams()
    for row in all_teams:
        # name, score, last_solve
        team = TeamScore(row[0], row[1])
        team_scores.append(team)
    return team_scores

def get_team_by_username(username):
    all_teams = db.get_team_by_username(username)
    if not all_teams:
        return None
    assert(len(all_teams) <= 1)
    team = db_team_to_team(all_teams[0])
    return team

def get_all_team_puzzles(team):
    puzzles = puzzle.get_all_puzzles()
    all_puzzles = db.get_team_puzzles(team.name)
    is_solved = {}
    for row in all_puzzles:
        for x in range(1, len(row)):
            is_solved[puzzles[x-1].name] = row[x]
    return is_solved

def team_solved_puzzle(team, puzzle):
    db.update_team_score(team.name)
    db.update_team_solves(team.name, puzzle.get_url_path())

def is_puzzle_solved(team, puzzle):
    is_solved = db.get_team_puzzle_solve(team.name, puzzle.get_url_path())
    return True if is_solved[0] else False

def update_team(team_name, team_username, team_password, team_email, puzzle_name):
    # Team name must be specified because of validator in form
    resp = "Team {} ".format(team_name)
    if is_team_unique(Team(team_name, team_username, team_password, team_email)):
        return resp + "is not a valid team!"
    if (team_username == "X" and team_password == "X" and team_email == "X" and puzzle_name == "X"):
        db.delete_team(team_name)
        return resp + "deleted!"
    if team_username:
        db.update_username(team_name, team_username)
        resp += "username changed to {} ".format(team_username)
    if team_password:
        db.update_code(team_name, team_password)
        resp += " password changed to {} ".foramt(team_password)
    if team_email:
        db.update_email(team_name, team_email)
        resp += " email changed to {} ".format(team_email)
    if puzzle_name:
        db.update_team_solves(team_name, Puzzle(puzzle_name, "").get_url_path())
        db.update_team_score(team_name)
        resp += " Puzzle {} updated to solved ".format(puzzle_name)
    return resp
