#!/usr/bin/python3
"""
Gather Data From An API Module
"""

import json
import requests


def get_all_employees_todo_progress():
    """
    API end route
    """
    url = "https://jsonplaceholder.typicode.com"
    users_url = f"{url}/users"
    todos_url = f"{url}/todos"

    all_employees_data = {}

    users_data = requests.get(users_url).json()

    # Fetch all todos for all users
    all_todos_data = requests.get(todos_url).json()

    for user in users_data:
        employee_id = user.get("id")
        if employee_id is not None:
            employee_name = user["username"]

            # Filter todos for the current user
            user_todos = [todo for todo in all_todos_data
                          if todo["userId"] == employee_id]

            tasks = []
            for task in user_todos:
                tasks.append({
                    "username": employee_name,
                    "task": task["title"],
                    "completed": task["completed"]
                })

            all_employees_data[str(employee_id)] = tasks

    json_file_path = "todo_all_employees.json"

    with open(json_file_path, mode='w') as json_file:
        json.dump(all_employees_data, json_file, indent=2)


if __name__ == "__main__":
    get_all_employees_todo_progress()
