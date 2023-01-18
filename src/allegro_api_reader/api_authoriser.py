import requests
import json
import time
import os
import webbrowser

with open('resources/client_id.txt') as f:
    CLIENT_ID = f.readline()
with open('resources/client_secret.txt') as f:
    CLIENT_SECRET = f.readline()
with open('resources/token_url.txt') as f:
    TOKEN_URL = f.readline()
with open('resources/code_url.txt') as f:
    CODE_URL = f.readline()


def get_code():
    try:
        payload = {'client_id': CLIENT_ID}
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        api_call_response = requests.post(CODE_URL, auth=(CLIENT_ID, CLIENT_SECRET),
                                          headers=headers, data=payload, verify=False)
        return api_call_response
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def get_access_token(device_code):
    try:
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        data = {'grant_type': 'urn:ietf:params:oauth:grant-type:device_code', 'device_code': device_code}
        api_call_response = requests.post(TOKEN_URL, auth=(CLIENT_ID, CLIENT_SECRET),
                                          headers=headers, data=data, verify=False)
        return api_call_response
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def await_for_access_token(interval, device_code):
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


def generate_token():
    code = get_code()
    result = json.loads(code.text)
    webbrowser.open(result['verification_uri_complete'])
    return await_for_access_token(int(result['interval']), result['device_code'])


def save_token_to_file(access_token):
    with open("resources/access_token.txt", "w") as file:
        file.write(access_token)


def read_token_form_file(path):
    with open(path) as file:
        access_token = file.readline()
        return access_token


def check_token():
    path = "resources/access_token.txt"
    if os.path.isfile(path):
        if os.path.getsize(path) > 0:
            return read_token_form_file(path)
        else:
            access_token = generate_token()
            save_token_to_file(access_token)
            return access_token
    else:
        access_token = generate_token()
        save_token_to_file(access_token)
        return access_token
