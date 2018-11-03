from wtforms import Form, BooleanField, StringField, PasswordField, validators


class RegistrationForm(Form):
    name = StringField("Team Name", [validators.DataRequired(), validators.Length(min=4, max=35)])
    email = StringField("Email", [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
    username = StringField("Username", [validators.DataRequired(),  validators.NoneOf(["admin"]), validators.Length(min=4, max=20)])
    password = PasswordField("Password", [validators.DataRequired(), validators.Length(min=4, max=35)])


class PuzzleAnswerForm(Form):
    answer = StringField("Answer")

class LoginForm(Form):
    username = StringField("Username")
    password = PasswordField("Password")

class RootForm(Form):
    teamname = StringField("Team Name", [validators.DataRequired()])
    username = StringField("Username")
    password = PasswordField("Password")
    email = StringField("Email")
    puzzle_name = StringField("Puzzle Name")
