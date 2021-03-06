class Team:
    def __init__(self, team_name, team_username, team_code, team_email, score=0):
        self.name = team_name
        self.username = team_username
        self.code = team_code
        self.email = team_email
        self.score = score

    def __repr__(self):
        return "Name: {}, Usenrame: {}, Code: {}, Email: {}, Score: {}".format(self.name, self.username, self.code, self.email, self.score)

class TeamScore:
    def __init__(self, team_name, score):
        self.name = team_name
        self.score = score

class Puzzle:
    def __init__(self, puzzle_name, puzzle_answer, solves=0, attempts=0):
        self.name = puzzle_name
        self.answer = puzzle_answer
        self.solves = solves
        self.attempts = attempts

    def get_url_path(self):
        url_path = "_".join(map(str.lower, self.name.split(" ")))
        return url_path

    def __repr__(self):
        return "Name: {}, Answer: {}, Solves: {}, Attempts: {}".format(self.name, self.answer, self.solves, self.attempts)
