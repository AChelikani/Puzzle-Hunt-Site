import database as db
from objects import TeamScore, Team

def db_team_to_team(row):
    print(row)
    return Team(row[0], row[1], row[2])


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

def is_puzzle_solved(team, puzzle):
    is_solved = db.get_team_puzzle_solve(team.name, puzzle.get_url_path())
    print(is_solved)
