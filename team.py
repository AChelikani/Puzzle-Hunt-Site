import database as db
from objects import TeamScore

def get_all_teams():
    team_scores = []
    all_teams = db.get_all_teams()
    for row in all_teams:
        # name, score, last_solve
        team = TeamScore(row[0], row[1])
        team_scores.append(team)
    return team_scores
