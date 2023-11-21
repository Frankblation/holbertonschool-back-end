#!/usr/bin/python3
"""Gather data from an api"""
import requests
import sys

def fetch_employee_todo_list(employee_id):
    """
    Fetches the TODO list for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing user data (dict) and TODO list (list).
               If the employee is not found, returns (None, None).
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f"{base_url}/{employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()

    if "id" not in user_data:
        print(f"No employee found with ID {employee_id}")
        return None, None

    todo_url = f"{base_url}/{employee_id}/todos"

    # Fetch TODO list for the user
    todo_response = requests.get(todo_url)
    todo_list = todo_response.json()

    return user_data, todo_list


def display_todo_progress(employee_id):
    """
    Displays the progress of completed tasks for a given employee.

    Args:
        employee_id (int): The ID of the employee.
    """
    user_data, todo_list = fetch_employee_todo_list(employee_id)

    if user_data is None or todo_list is None:
        return

    employee_name = user_data["name"]
    completed_tasks = [task for task in todo_list if task["completed"]]
    total_tasks = len(todo_list)

    print(
        f"Employee {employee_name} is done with tasks({len(completed_tasks)}/\
                                                      {total_tasks}): ")

    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        display_todo_progress(employee_id)
