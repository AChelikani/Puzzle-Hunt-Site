from objects import *
from puzzles.directory import *

def get_all_puzzles():
    puzzle_list = []
    for puzzle in PUZZLES:
        pzl = Puzzle(puzzle[0], puzzle[1])
        puzzle_list.append(pzl)
    return puzzle_list
