#!/usr/bin/python3
'''
This gathers data from an API, and then uses it to creqate a todo
list progress function
'''


import requests
import sys


def todoList(employee_id):
    '''This function does the requested task in the earlier comment'''
    # Define the API endpoint URL
    api_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        # Send a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            todos = response.json()

            # Filter completed tasks
            completed_tasks = [todo for todo in todos if todo['completed']]

            # Get employee name
            employee_name = todos[0]['user']['name']

            # Calculate progress
            total_tasks = len(todos)
            completed_task_count = len(completed_tasks)
            tasks_left = total_tasks - completed_task_count

            # Display progress information
            print(f'Employee {employee_name} is done with tasks ({completed_task_count}/{total_tasks}):')
            print(f'{employee_name} has completed {completed_task_count} tasks.')
            print(f'{employee_name} has {tasks_left} tasks left to do.')
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    employee_id = int(input("Enter Employee ID: "))
    get_employee_todo_progress(employee_id)
