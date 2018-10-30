from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from objects import *
import forms
import database as db
import mock_database as mock_db
import puzzle
import team
import helpers
import mailgun
import slack

app = Flask(__name__)
Bootstrap(app)
db.create_databases()
puzzle.add_puzzles()
mock_db.create_mock_teams()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/puzzles")
def puzzles():
    return render_template("puzzles.html", puzzles=puzzle.get_all_puzzles_with_stats())

@app.route("/puzzles/<puzzle_name>", methods=["GET", "POST"])
def puzzle_set(puzzle_name):
    pzl = puzzle.get_puzzle_at_path(puzzle_name)
    form = forms.PuzzleAnswerForm(request.form)
    url = helpers.resolve_puzzle_url(puzzle_name)
    error_msg = None
    if request.method == 'POST' and form.validate():
        tm = team.get_team_by_passcode(form.code.data)
        if (tm):
            if (helpers.are_strings_matching(form.answer.data, pzl.answer)):
                is_solved = team.is_puzzle_solved(tm, pzl)
                if is_solved:
                    error_msg = "Already solved!"
                else:
                    team.team_solved_puzzle(tm, pzl)
                    puzzle.puzzle_solved(pzl)
                    print("Team: {}, Puzzle: {}, Correct Answer!".format(tm.name, pzl.name))
                    #slack.log_correct_answer(tm, pzl)
                    error_msg = "Correct answer!"
            else:
                puzzle.puzzle_attempted(pzl)
                #print("Team: {}, Puzzle: {}, Guess: {}".format(tm.name, pzl.name, form.answer.data))
                slack.log_guess(tm, pzl, form.answer.data)
                error_msg = "Incorrect answer!"
        else:
            error_msg = "Invalid passcode!"
    form.answer.data = ""
    return render_template(url, form=form, error=error_msg)

@app.route("/scoreboard")
def scoreboard():
    return render_template("scoreboard.html", team_scores=team.get_all_teams_scores())

@app.route("/register", methods=["GET", "POST"])
def register():
    form = forms.RegistrationForm(request.form)
    error_msg = None
    if request.method == 'POST' and form.validate():
        team_code = helpers.generate_team_code()
        while (not team.is_team_code_unique(team_code)):
            team_code = helpers.generate_team_code()
        tm = Team(form.name.data, team_code, form.email.data)
        if not team.is_team_unique(tm):
            error_msg = "Team already exists!"
        else:
            db.add_team(tm)
            print("\n Adding Team\n Team: {}, Code: {}\n".format(tm.name, tm.code))
            #slack.log_team_registration(tm)
            #mailgun.send_registration_email(tm.email, team_code)
            return render_template("completed_registration.html")
    return render_template("register.html", form=form, error=error_msg)


@app.route("/stars")
def stars():
    return render_template("stars.html")


if __name__ == "__main__":
    app.run(debug=True)
