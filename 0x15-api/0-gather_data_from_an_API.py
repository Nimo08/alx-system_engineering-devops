#!/usr/bin/python3
"""
Use REST API for a given employee ID to return
information about his/her TODO list progress
"""


import requests
import sys


def todo_list(employee_id):
    """
    Returns information about an employee's TODO list
    """
    url_api = f'https://jsonplaceholder.typicode.com/'\
              f'todos?userId={employee_id}'
    try:
        # make GET request to todo list API endpoint
        response = requests.get(url_api)
        response.raise_for_status()
        todo = response.json()
        # make separate GET request to user endpoint for user info
        user_response = requests.get(f'https://jsonplaceholder.typicode.com/'
                                     f'users/{employee_id}')
        user_response.raise_for_status()
        user_info = user_response.json()
        employee_name = user_info['name']
        completed_tasks = []
        for task in todo:
            if task['completed']:
                completed_tasks.append(task)
        total_tasks = len(todo)
        completed_task_num = len(completed_tasks)
        print(f"Employee {employee_name} is done with tasks"
              f"({str(completed_task_num)}/{str(total_tasks)}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        todo_list(employee_id)
    except ValueError as e:
        print(e)
        sys.exit(1)
