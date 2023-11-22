#!/usr/bin/python3
"""Exports TO Do progress for an employee ID to a CSV file."""

import csv
import requests
import sys


def export_to_csv(employee_id, tasks):
    """Exports TO DO progress to a CSV file."""

    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_request = requests.get(user_url).json()

    # Verify that the user ID in the response matches the expected employee ID
    if 'id' not in user_request or user_request['id'] != employee_id:
        print(f"Error: Employee with ID {employee_id} not found.")
        sys.exit(1)

    user_name = user_request.get('username')

    filename = f'{employee_id}.csv'
    tasks_list = []

    for task in tasks:
        task_dict = {
            "USER_ID": employee_id,
            "USERNAME": user_name,
            "TASK_COMPLETED_STATUS": str(task['completed']),
            "TASK_TITLE": task['title']
        }
        tasks_list.append(task_dict)

    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                "USER_ID",
                "USERNAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"])
        csv_writer.writeheader()  # Write CSV header
        csv_writer.writerows(tasks_list)

    print(f'Data exported to {filename}')
    print(f'Number of tasks in CSV:\
           {"OK" if len(tasks) == len(tasks_list) else "Incorrect"}')


def get_user_tasks(employee_id):
    """Gets tasks for a given employee ID."""

    url = f'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': employee_id}

    try:
        todo_request = requests.get(url, params=params).json()
    except requests.RequestException as e:
        print(f"Error fetching tasks from the API: {e}")
        sys.exit(1)

    return todo_request


if __name__ == "__main__":
    """Main entry point. Usage: python script.py <employee_id>"""
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print('Usage: python script.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    tasks = get_user_tasks(employee_id)
    export_to_csv(employee_id, tasks)
