class Team:
    def __init__(self, team_name, team_code, team_email, score=0):
        self.name = team_name
        self.code = team_code
        self.email = team_email
        self.score = score

    ''' Return (bool, errors) '''
    def validate(self):
        # Validate name has min length
        # Validate code has min length
        # Validate email is a valid email
        return true, []

class TeamScore:
    def __init__(self, team_name, score):
        self.name = team_name
        self.score = score

class Puzzle:
    def __init__(self, puzzle_name, puzzle_answer):
        self.name = puzzle_name
        self.answer = puzzle_answer
