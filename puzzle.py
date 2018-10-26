from objects import *
from puzzles.directory import *
import database as db

def get_all_puzzles():
    puzzle_list = []
    for puzzle in PUZZLES:
        pzl = Puzzle(puzzle[0], puzzle[1])
        puzzle_list.append(pzl)
    return puzzle_list

def get_puzzle_at_path(path):
    all_puzzles = get_all_puzzles()
    for puzzle in all_puzzles:
        if puzzle.get_url_path() == path:
            return puzzle
    return None

def add_puzzles():
    puzzles = get_all_puzzles()
    db.add_puzzles(puzzles)

def puzzle_solved(puzzle):
    db.update_puzzle_solve(puzzle.get_url_path())

def puzzle_attempted(puzzle):
    db.update_puzzle_attempts(puzzle.get_url_path())

def get_all_puzzles_with_stats():
    puzzles = get_all_puzzles()
    all_puzzle_stats = db.get_puzzles_stats()
    puzzle_index = 0
    for row in all_puzzle_stats:
        print(row)
        pzl = puzzles[puzzle_index]
        pzl.solves, pzl.attempts = row[1], row[2]
        puzzles[puzzle_index] = pzl
        puzzle_index += 1
    print(puzzles)
    return puzzles
