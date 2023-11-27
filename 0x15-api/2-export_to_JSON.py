#!/usr/bin/python3
"""
Use REST API for a given employee ID to return
information about his/her TODO list progress
"""


import json
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
        user_id = user_info['id']
        username = user_info['name']
        completed_tasks = []
        for task in todo:
            if task['completed']:
                completed_tasks.append(task)
        return {
                'user_id': user_id,
                'username': username,
                'total_tasks': len(todo),
                'tasks': todo,
                'user_info': user_info
                }
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


def export_json(employee_id, total_tasks, tasks, user_info):
    """
    Export data in JSON format
    """
    file = f"{employee_id}.json"
    data = {
            employee_id: [
                {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": user_info['username'],
                    }
                for task in tasks
                ]
            }
    with open(file, 'w') as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        todo_info = todo_list(employee_id)
        export_json(employee_id, todo_info['total_tasks'],
                    todo_info['tasks'], todo_info['user_info'])
    except ValueError as e:
        print(e)
        sys.exit(1)
