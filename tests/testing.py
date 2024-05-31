import pytest
from models.user import User
from models.todo import Todo

def test_user_in_fancode_city():
    user_data = {
        'id': 1,
        'name': 'Test User',
        'address': {'geo': {'lat': '0', 'lng': '10'}}
    }
    user = User(user_data)
    assert user.is_in_fancode_city(-40, 5, 5, 100)

def test_user_not_in_fancode_city():
    user_data = {
        'id': 2,
        'name': 'Test User',
        'address': {'geo': {'lat': '50', 'lng': '110'}}
    }
    user = User(user_data)
    assert not user.is_in_fancode_city(-40, 5, 5, 100)

def test_calculate_task_completion():
    todos_data = [
        {'userId': 1, 'completed': True},
        {'userId': 1, 'completed': False},
        {'userId': 1, 'completed': True}
    ]
    todos = [Todo(todo) for todo in todos_data]
    completion_percentage = Todo.calculate_task_completion(todos)
    assert completion_percentage == 66.66666666666666

@pytest.fixture
def user_data():
    return {'id': 1, 'name': 'Test User', 'address': {'geo': {'lat': '0', 'lng': '10'}}}

@pytest.fixture
def todos_data():
    return [
        {'userId': 1, 'completed': True},
        {'userId': 1, 'completed': False},
        {'userId': 1, 'completed': True}
    ]

def test_full_integration(user_data, todos_data, mocker):
    mocker.patch('api.users_api.fetch_users', return_value=[user_data])
    mocker.patch('api.todos_api.fetch_todos', return_value=todos_data)

    from main import main
    main()  
