from api.users_api import fetch_users
from api.todos_api import fetch_todos
from models.user import User
from models.todo import Todo
from utils.geolocation import FANCODE_CITY_LAT_MIN, FANCODE_CITY_LAT_MAX, FANCODE_CITY_LONG_MIN, FANCODE_CITY_LONG_MAX


def main():
    users_data = fetch_users()
    for user_data in users_data:
        user = User(user_data)
        if user.is_in_fancode_city(FANCODE_CITY_LAT_MIN, FANCODE_CITY_LAT_MAX, FANCODE_CITY_LONG_MIN, FANCODE_CITY_LONG_MAX):
            todos_data = fetch_todos(user.id)
            todos = []
            for todo in todos_data:
                todos.append(Todo(todo))
            completion_percentage = Todo.calculate_task_completion(todos)
            if completion_percentage > 10:
                print(f"User {user.name} (ID: {user.id}) in FanCode City has completed {round(completion_percentage,2)}% of their tasks.")
            else:
                print(f"User {user.name} (ID: {user.id}) in FanCode City has not met the completion criteria.")

if __name__ == "__main__":
    main()
