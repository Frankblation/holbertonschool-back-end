#!/usr/bin/python3
"""Exports TODO progress for an employee ID to a CSV file."""

import csv
import requests
import sys


def export_to_csv(employee_id, tasks):
    """Exports TODO progress to a CSV file."""

    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_request = requests.get(user_url).json()
    user_name = user_request.get('username')

    filename = f'{employee_id}.csv'

    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in tasks:
            csv_writer.writerow(
                [employee_id, user_name,
                 str(task['completed']), task['title']])

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
    export_to_csv(employee_id, tasks)
