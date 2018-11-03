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
    send_message("#log-guesses", msg)

def log_correct_answer(team, puzzle):
    msg = "[SOLVE] Team: `{}`, Puzzle: `{}`, CORRECT ANSWER!".format(team.name, puzzle.name)
    send_message("#log-guesses", msg)

def log_team_registration(team):
    msg = "Team: `{}`, Email: `{}`".format(team.name, team.email)
    send_message("#log-signups", msg)
