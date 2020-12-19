from django.conf import settings
import requests

def authenticate(username, password):
    # Authenticate username and password using specified API
    url = settings.AUTH_API
    header = {
        'Content-Type': 'application/json'
    }
    payload = {
        "username": username,
        "password": password
    }
    try:
        response = requests.post(url=url, json=payload, headers=header)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    # print(response.json())