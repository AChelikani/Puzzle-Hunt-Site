from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from objects import *
import forms
import database as db
import puzzle
import team

app = Flask(__name__)
Bootstrap(app)
db.create_databases()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/puzzles")
def puzzles():
    return render_template("puzzles.html", puzzles=puzzle.get_all_puzzles())


@app.route("/scoreboard")
def scoreboard():
    return render_template("scoreboard.html", team_scores=team.get_all_teams())

@app.route("/register", methods=["GET", "POST"])
def register():
    form = forms.RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        team = Team(form.name.data, form.code.data, form.email.data)
        db.add_team(team)
        return render_template("completed_registration.html")
    return render_template("register.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)
