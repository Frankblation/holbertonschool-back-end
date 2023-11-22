#!/usr/bin/python3
"""Exports TODO progress for an employee ID to a JSON file."""

import json
import requests
import sys


def export_to_json(employee_id, tasks):
    """Exports TODO progress to a JSON file."""

    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_request = requests.get(user_url).json()
    user_name = user_request.get('username')

    data = {
        "USER_ID": [
            {"task": task['title'], "completed": task['completed'], "username": user_name}
            for task in tasks
        ]
    }

    filename = f'{employee_id}.json'

    with open(filename, mode='w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f'Data exported to {filename}')


def get_user_tasks(employee_id):
    """Gets tasks for a given employee ID."""

    url = f'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': employee_id}
    todo_request = requests.get(url, params=params).json()

    return todo_request


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    tasks = get_user_tasks(employee_id)
    export_to_json(employee_id, tasks)
