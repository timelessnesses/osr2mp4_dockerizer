import requests
import os

def send_release_to_github(name,description,access_token):
    resp = requests.post(
        'https://api.github.com/repos/{}/releases'.format(name),
        json={
            'tag_name': 'v{}'.format(description['version']),
            'name': 'v{}'.format(description['version']),
            'body': description['description'],
            'draft': False,
            'prerelease': False
        },
        headers={
            'Authorization': 'token {}'.format(access_token)
        }
    )
    if resp.status_code != 201:
        raise Exception('Failed to create release: {}'.format(resp.text))
    return resp.json()

send_release_to_github(
    os.environ['GITHUB_REPO'],
    {
        'version': os.environ['VERSION'],
        'description': os.environ['DESCRIPTION']
    },
    os.environ['GITHUB_ACCESS_TOKEN']
)