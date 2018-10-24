import random

CODE_LENGTH = 4

def resolve_puzzle_url(puzzle_name):
    return "puzzles/" + puzzle_name + ".html"

def are_strings_matching(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    return s1 == s2

def generate_team_code():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    code = ""
    for x in range(CODE_LENGTH):
        rand_int = random.randint(0,len(chars))
        code += chars[rand_int]
    return code
