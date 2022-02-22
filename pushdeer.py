import requests


def notify(title, message, group=None, **kwargs):
    data = {
        # 'text': title if len(title) <= 20 else title[:19] + u'\u2026',
        'text': title,
        'desp': message,
        'type': 'text'
    }

    if group:
        data['group'] = group
    # NOTE: Replace <key> with your key
    endpoint = "https://api2.pushdeer.com/message/push?pushkey=<key>"
    resp = requests.post(endpoint, data=data)

    resp.raise_for_status()
