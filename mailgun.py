import requests
import config
from registration_email import registration_template

key = config.MAILGUN_API_KEY
sandbox = config.MAILGUN_SANDBOX
recipient = "advith.chelikani@gmail.com"

def send_registration_email(recipient, code):
    html_template = registration_template(code)
    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
    request = requests.post(request_url, auth=('api', key), data={
        'from': 'hello@example.com',
        'to': recipient,
        'subject': 'Arcane Puzzle Hunt Registration',
        'html': html_template
    })
    print('Status: {0}'.format(request.status_code))
    print('Body:   {0}'.format(request.text))


if __name__ == "__main__":
    pass
    #send_registration_email(recipient, registration_template("a1b2"))
