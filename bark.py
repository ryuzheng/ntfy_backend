import requests


def notify(title, message, group=None, **kwargs):
    data = {
        #'title': title if len(title) <= 20 else title[:19] + u'\u2026',
        'title': title,
        'body': message
    }

    if group:
        data['group'] = group
    # NOTE: Replace <website> with your website, <key> with your key
    endpoint = "https://<website>/<key>/"
    resp = requests.post(endpoint, data=data)

    resp.raise_for_status()
