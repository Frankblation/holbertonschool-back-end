import requests
import sys


def get_employee_todo_progress(employee_id):
    url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{url}/users/{employee_id}"
    todo_url = f"{url}/todos"

    # Make API requests and check for success
    try:
        employee_data = requests.get(employee_url).json()
        employee_name = employee_data.get("name")

        todo_data = requests.get(todo_url,
                                 params={"userId": employee_id}).json()

        if not isinstance(todo_data, list):
            raise ValueError("Invalid response from the TODO API")

    except requests.RequestException as e:
        print(f"Error fetching data from the API: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error processing API response: {e}")
        sys.exit(1)

    completed_tasks = [t["title"] for t in todo_data if t["completed"]]
    number_done = len(completed_tasks)
    number_total = len(todo_data)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, number_done, number_total))
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
