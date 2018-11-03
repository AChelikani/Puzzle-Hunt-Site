from flask import Flask, render_template, request, url_for, redirect
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
import flask_login

app = Flask(__name__)
app.secret_key = b'_5da#yd2Las"F4Q8z/'
Bootstrap(app)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


db.create_databases()
puzzle.add_puzzles()
mock_db.create_mock_teams()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/puzzles")
def puzzles():
    by_solves = request.args.get("sort_by_solve")
    by_solved = request.args.get("sort_by_solved")
    print(by_solves)
    puzzle_solves = {}
    if flask_login.current_user.is_authenticated and flask_login.current_user.username != "admin":
        puzzle_solves = team.get_all_team_puzzles(flask_login.current_user.team)
    puzzles = puzzle.get_all_puzzles_with_stats(by_solves=by_solves)
    if by_solved:
        puzzles = list(filter(lambda x: not puzzle_solves[x.name], puzzles)) + list(filter(lambda x: puzzle_solves[x.name], puzzles))
    return render_template("puzzles.html", puzzles=puzzles, puzzle_solves=puzzle_solves)

@app.route("/puzzles/<puzzle_name>", methods=["GET", "POST"])
def puzzle_set(puzzle_name):
    pzl = puzzle.get_puzzle_at_path(puzzle_name)
    form = forms.PuzzleAnswerForm(request.form)
    url = helpers.resolve_puzzle_url(puzzle_name)
    error_msg = None
    if request.method == 'POST' and form.validate():
        tm = flask_login.current_user.team
        if (helpers.are_strings_matching(form.answer.data, pzl.answer)):
            is_solved = team.is_puzzle_solved(tm, pzl)
            if is_solved:
                error_msg = "Already solved!"
            else:
                team.team_solved_puzzle(tm, pzl)
                puzzle.puzzle_solved(pzl)
                slack.log_correct_answer(tm, pzl)
                error_msg = "Correct answer!"
        else:
            puzzle.puzzle_attempted(pzl)
            slack.log_guess(tm, pzl, form.answer.data)
            error_msg = "Incorrect answer!"
    form.answer.data = ""
    return render_template(url, form=form, error=error_msg)

@app.route("/scoreboard")
def scoreboard():
    return render_template("scoreboard.html", team_scores=team.get_all_teams_scores())

@app.route("/root", methods=['GET', 'POST'])
@flask_login.login_required
def root():
    if flask_login.current_user.username != "admin":
        return redirect(url_for("index"))
    form = forms.RootForm(request.form)
    if request.method == "POST":
        if request.args.get("tables"):
            table1 = db.get_table_teams()
            table2 = db.get_table_team_scores()
            table3 = db.get_table_team_puzzles()
            return helpers.pretty_print_tables(table1, table2, table3)
        if request.args.get("update"):
            resp = team.update_team(form.teamname.data, form.username.data, form.password.data, form.email.data, form.puzzle_name.data)
            return render_template("root.html", form=form, error=resp)
    return render_template("root.html", form=form)


@app.route("/team_info")
@flask_login.login_required
def team_info():
    return render_template("team_info.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = forms.RegistrationForm(request.form)
    error_msg = None
    if request.method == 'POST' and form.validate():
        tm = Team(form.name.data, form.username.data, hash(form.password.data), form.email.data)
        if not team.is_team_unique(tm):
            error_msg = "Team already exists!"
        elif not team.is_username_unique(tm):
            error_msg = "Username already exists!"
        else:
            db.add_team(tm)
            print("\n Adding Team\n Team: {}, Email: {}, Username: {}, Code: {}\n".format(tm.name, tm.email, tm.username, tm.code))
            slack.log_team_registration(tm)
            #mailgun.send_registration_email(tm.email, team_code)
            return render_template("completed_registration.html")
    return render_template("register.html", form=form, error=error_msg)

# Login and Logout
class User(flask_login.UserMixin):
    def __init__(self, team_username, team=None):
        self.username = team_username
        self.team = team

    def get_id(self):
        return self.username

@login_manager.user_loader
def user_loader(username):
    ####################
    #  FOR SUPER USER  #
    ####################
    if username == "admin":
        return User(username)
    tm = team.get_team_by_username(username)
    if not tm:
        return

    user = User(username, tm)
    return user


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    ####################
    #  FOR SUPER USER  #
    ####################
    if username == "admin" and request.form['password'] == "admin":
        return User(username)
    tm = team.get_team_by_username(username)
    if not tm:
        return

    user = User(username, tm)

    if helpers.hash_password(request.form['password']) == tm.code:
        return user
    return

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm(request.form)
    if request.method == 'GET':
        return render_template("login.html", form=form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        ####################
        #  FOR SUPER USER  #
        ####################
        if username == "admin" and form.password.data == "admin":
            flask_login.login_user(User(username))
            return redirect(url_for('index'))

        tm = team.get_team_by_username(username)
        if tm and heleprs.hash_password(form.password.data) == tm.code:
            user = User(username, tm)
            flask_login.login_user(user)
            return redirect(url_for('index'))

    return render_template("login.html", form=form, error="Invalid username/password!")

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
