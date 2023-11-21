#!/usr/bin/python3
"""
Gather data from an API.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Arguments:
    <employee_id>: An integer representing the employee's ID.

Example:
    python3 0-gather_data_from_an_API.py 2
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        raise SystemExit("Error: Invalid or missing employee_id")

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    # Fetch TODO list for the user
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todo_data if task["completed"]]

    # Display the information
    print(f"Employee {user_data['name']} is done with tasks("
          f"{len(completed_tasks)}/{len(todo_data)}): ")
    for task in completed_tasks:
        print(f"\t{task['title']}")
