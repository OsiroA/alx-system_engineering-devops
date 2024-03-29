#!/usr/bin/python3
'''
This gathers data from an API, and then uses it to creqate a todo
list progress function
'''
import requests
import sys


if __name__ == "__main__":
    '''This function does the requested task in the earlier comment'''
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    completed = [task for task in todos if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(task.get("title"))) for task in completed]
