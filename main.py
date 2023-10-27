import os
import requests
from dotenv import load_dotenv


def refresh_token():
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    token_endpoint = os.getenv('API_TOKEN_ENDPOINT')

    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(
        token_endpoint,
        json=payload,
        headers={'Accept': 'application/json'}
    )

    return response.json()['access_token']


def send_post_request(url, params, token=''):
    response = requests.post(
        endpoint,
        json=params,
        headers={'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
    )

    if response.status_code == 401:
        token = refresh_token()
        send_post_request(url, params, token)
    else:
        print(response.content)


def send_get_request(url, token=''):
    response = requests.get(
        url,
        headers={'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
    )

    if response.status_code == 401:
        token = refresh_token()
        send_get_request(url, token)
    else:
        print(response.content)


if __name__ == '__main__':
    load_dotenv()

    endpoint = os.getenv('API_ENDPOINT')
    id = os.getenv('CLIENT_ID')

    payload = {'sensor_id': id, 'value': 1}
    send_get_request(url=endpoint)
