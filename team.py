import database as db
import helpers
from objects import TeamScore, Team

def db_team_to_team(row):
    return Team(row[0], row[1], row[2])

def is_team_unique(team):
    all_teams = db.get_all_teams()
    for row in all_teams:
        if (helpers.are_strings_matching(team.name, row[0])):
            return False
    return True

def is_team_code_unique(team):
    all_teams = db.get_all_teams()
    for row in all_teams:
        if (team.code == row[1]):
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

def get_team_by_passcode(code):
    all_teams = db.get_team_by_passcode(code)
    assert(len(all_teams) <= 1)
    if len(all_teams) == 0:
        return None
    team = db_team_to_team(all_teams[0])
    return team

def team_solved_puzzle(team, puzzle):
    db.update_team_score(team.name)
    db.update_team_solves(team.name, puzzle.get_url_path())

def is_puzzle_solved(team, puzzle):
    is_solved = db.get_team_puzzle_solve(team.name, puzzle.get_url_path())
    return True if is_solved[0] else False
