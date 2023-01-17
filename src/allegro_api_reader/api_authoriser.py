import requests
import json

with open('resources/client_id.txt') as f:
    CLIENT_ID = f.readline()
with open('resources/client_secret.txt') as f:
    CLIENT_SECRET = f.readline()
with open('resources/token_url.txt') as f:
    TOKEN_URL = f.readline()


def get_access_token():
    try:
        data = {'grant_type': 'client_credentials'}
        access_token_response = requests.post(TOKEN_URL, data=data, verify=False,
                                              allow_redirects=False, auth=(CLIENT_ID, CLIENT_SECRET))
        tokens = json.loads(access_token_response.text)
        access_token = tokens['access_token']
        return access_token
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
