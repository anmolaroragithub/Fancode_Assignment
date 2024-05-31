import requests

TODOS_API_URL = "http://jsonplaceholder.typicode.com/todos"

def fetch_todos(user_id):
    response = requests.get(f"{TODOS_API_URL}?userId={user_id}")
    response.raise_for_status()
    return response.json()
