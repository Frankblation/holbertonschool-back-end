#!/usr/bin/python3
"""
Gather Data From An API Module
"""

import requests
from sys import argv

def get_employee_todo_progress(employee_id):
    """
    Retrieve employee TODO list progress from the API.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # Fetch employee data
    employee_data = requests.get(url).json()
    employee_name = employee_data.get("name")

    # Fetch employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_data = requests.get(todo_url).json()

    # Count completed tasks
    completed_tasks = [task for task in todo_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)

    # Display information
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"{' ' * 5}{task['title']}")

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(argv[1])
        get_employee_todo_progress(employee_id)
