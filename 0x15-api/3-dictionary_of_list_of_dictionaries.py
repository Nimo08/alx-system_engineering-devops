#!/usr/bin/python3
"""
Use REST API for a given employee ID to return
information about his/her TODO list progress
"""


import json
import requests
import sys


def todo_list_all():
    """
    Returns information about all employee's TODO list
    """
    url_users = 'https://jsonplaceholder.typicode.com/users'
    try:
        response = requests.get(url_users)
        response.raise_for_status()
        users = response.json()
        data = {}
        for user in users:
            employee_id = user['id']
            url_api = f'https://jsonplaceholder.typicode.com/'\
                      f'todos?userId={employee_id}'
            response_todo = requests.get(url_api)
            response_todo.raise_for_status()
            todo = response_todo.json()
            data[employee_id] = [
                    {
                        "username": user['username'],
                        "task": task['title'],
                        "completed": task['completed'],
                        }
                    for task in todo
                    ]
        return data
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


def export_json_all(data):
    """
    Export data in JSON format
    """
    file = "todo_all_employees.json"
    with open(file, 'w') as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    try:
        todo_info = todo_list_all()
        export_json_all(todo_info)
    except ValueError as e:
        print(e)
        sys.exit(1)
