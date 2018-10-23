class Team:
    def __init__(self, team_name, team_code, team_email, score=0):
        self.name = team_name
        self.code = team_code
        self.email = team_email
        self.score = score

    def __repr__(self):
        return "Name: {}, Code: {}, Email: {}, Score: {}".format(self.name, self.code, self.email, self.score)

class TeamScore:
    def __init__(self, team_name, score):
        self.name = team_name
        self.score = score

class Puzzle:
    def __init__(self, puzzle_name, puzzle_answer):
        self.name = puzzle_name
        self.answer = puzzle_answer

    def get_url_path(self):
        url_path = "_".join(map(str.lower, self.name.split(" ")))
        return url_path

    def __repr__(self):
        return "Name: {}, Answer: {}".format(self.name, self.answer)
