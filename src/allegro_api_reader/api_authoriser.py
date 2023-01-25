import atexit

import requests
import json
import time
import os
import webbrowser

with open('resources/client_id.txt') as f:
    CLIENT_ID = f.readline()
with open('resources/client_secret.txt') as f:
    CLIENT_SECRET = f.readline()
CODE_URL = "https://allegro.pl/auth/oauth/device"
TOKEN_URL = "https://allegro.pl/auth/oauth/token"


def get_code() -> requests.Response:
    try:
        payload = {'client_id': CLIENT_ID}
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        api_call_response = requests.post(CODE_URL, auth=(CLIENT_ID, CLIENT_SECRET), headers=headers, data=payload, verify=False)
        return api_call_response
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_access_token(device_code: str) -> requests.Response:
    try:
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        data = {'grant_type': 'urn:ietf:params:oauth:grant-type:device_code', 'device_code': device_code}
        api_call_response = requests.post(TOKEN_URL, auth=(CLIENT_ID, CLIENT_SECRET), headers=headers, data=data, verify=False)
        return api_call_response
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def await_for_access_token(interval: int, device_code: str) -> str:
    while True:
        time.sleep(interval)
        result_access_token = get_access_token(device_code)
        token = json.loads(result_access_token.text)
        if result_access_token.status_code == 400:
            if token['error'] == 'slow_down':
                interval += interval
            if token['error'] == 'access_denied':
                break
        else:
            return token['access_token']


def generate_token() -> str:
    code = get_code()
    result = json.loads(code.text)
    webbrowser.open(result['verification_uri_complete'])
    return await_for_access_token(int(result['interval']), result['device_code'])


def save_token_to_file(access_token: str):
    with open("resources/access_token.txt", "w") as file:
        file.write(access_token)


def read_token_form_file(file_path: str) -> str:
    with open(file_path) as file:
        access_token = file.readline()
        return access_token


def check_token() -> str:
    file_path = "resources/access_token.txt"
    if os.path.getsize(file_path) > 0:
        return read_token_form_file(file_path)
    else:
        access_token = generate_token()
        save_token_to_file(access_token)
        return access_token


def clear_token_on_exit(file_path: str):
    with open(file_path, 'w') as file:
        file.write('')


atexit.register(clear_token_on_exit, 'resources/access_token.txt')
