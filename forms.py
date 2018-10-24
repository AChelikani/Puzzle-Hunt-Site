from wtforms import Form, BooleanField, StringField, PasswordField, validators


class RegistrationForm(Form):
    name = StringField("Team Name", [validators.DataRequired(), validators.Length(min=4, max=25)])
    email = StringField("Email", [validators.DataRequired(), validators.Length(min=6, max=35)])


class PuzzleAnswerForm(Form):
    answer = StringField("Answer")
    code = PasswordField("Team Passcode")
