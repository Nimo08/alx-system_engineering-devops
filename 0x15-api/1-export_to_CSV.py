#!/usr/bin/python3
"""
Use REST API for a given employee ID to return
information about his/her TODO list progress
Export data to CSV format
"""


import csv
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
                'completed_tasks': completed_tasks
                }
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        todo_list_info = todo_list(employee_id)
        with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in todo_list_info['completed_tasks']:
                csv_writer.writerow([
                        str(todo_list_info['user_id']),
                        todo_list_info['username'],
                        str(task['completed']),
                        task['title']
                    ])
    except ValueError as e:
        print(e)
        sys.exit(1)
