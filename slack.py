from slackclient import SlackClient
import config

slack_token = config.SLACK_TOKEN
sc = SlackClient(slack_token)


def send_message(channel, message):
    sc.api_call(
      "chat.postMessage",
      channel=channel,
      text=message
    )


def log_guess(team, puzzle, guess):
    msg = "[GUESS] Team: `{}`, Puzzle: `{}`, Guess `{}`".format(team.name, puzzle.name, guess)
    sc.api_call("#log-guesses", msg)

def log_correct_answer(team, puzzle):
    msg = "[SOLVE] Team: `{}`, Puzzle: `{}`, CORRECT ANSWER!".format(team.name, puzzle.name)
    sc.api_call("#log-guesses", msg)

def log_team_registration(team):
    msg = "Team: `{}`, Email: `{}`, Passcode: `{}`".format(team.name, team.email, team.code)
    sc.api_call("#log-signups", msg)
