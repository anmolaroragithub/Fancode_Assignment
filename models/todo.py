class Todo:
    def __init__(self, todo_data):
        self.user_id = todo_data['userId']
        self.completed = todo_data['completed']

    @staticmethod
    def calculate_task_completion(todos):
        if not todos:
            return 0
        completed_tasks = sum(1 for todo in todos if todo.completed)
        return (completed_tasks / len(todos)) * 100
