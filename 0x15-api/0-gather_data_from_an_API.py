#!/usr/bin/python3
'''
This gathers data from an API, and then uses it to creqate a todo
list progress function
'''
import requests
import sys


def todoList(employee_id):
    '''This function does the requested task in the earlier comment'''
    api_url = 'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        
        response = requests.get(api_url)
        if response.status_code == 200:
            todos = response.json()
            completed_tasks = [todo for todo in todos if todo['completed']]
            employee_name = todos[0]['user']['name']
            total_tasks = len(todos)
            completed_task_count = len(completed_tasks)
            tasks_left = total_tasks - completed_task_count
            print('Employee {} is done with tasks ({}/{}):'.format(employee_name, completed_task_count, total_tasks))
            print('{} has completed {} tasks.'.format(employee_name, completed_task_count))
            print('{} has {} tasks left to do.'.format(employee_name, tasks_left))
        else:
            print("Failed to retrieve data. Status code: {}".format(response.status_code))
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))

if __name__ == '__main__':
    employee_id = int(input("Enter Employee ID: "))
    get_employee_todo_progress(employee_id)
