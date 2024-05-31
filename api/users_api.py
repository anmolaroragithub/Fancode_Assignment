import requests

USERS_API_URL = "http://jsonplaceholder.typicode.com/users"

def fetch_users():
    response = requests.get(USERS_API_URL)
    response.raise_for_status()
    return response.json()
