#!/usr/bin/python3
'''
This gathers data from an API, and then uses it to creqate a todo
list progress function
'''
import csv
import requests
import sys


if __name__ == "__main__":
    '''This function does the requested task in the earlier comment'''
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Write the to-do list data to a CSV file named after the user ID
    with open("{}.csv".format(user_id), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # Write each to-do item to a row in the CSV file
        for todo in todos:
            # Extract the necessary data from the to-do item
            row = [user_id, username, todo.get("completed"), todo.get("title")]
            writer.writerow(row)
