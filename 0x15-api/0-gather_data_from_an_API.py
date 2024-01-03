#!/usr/bin/python3
"""for a given employee ID, returns information about his/her
TODO list progress.
"""
if __name__ == "__main__":
    import requests
    import sys
    id_ = sys.argv[1]
    n_task = 0
    task_title = ""
    starting_point = {
            "1": 0,
            "2": 20,
            "3": 40,
            "4": 60,
            "5": 80,
            "6": 100,
            "7": 120,
            "8": 140,
            "9": 160,
            "10": 180
            }
    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{id_}')
    emp_name = r.json().get("name")
    r = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    for i in range(starting_point.get(id_), starting_point.get(id_) + 20):
        if r[i].get("completed") is True:
            n_task += 1
            task_title += "\t " + r[i].get("title") + '\n'
    print(f"Employee {emp_name} is done with tasks({n_task}/20):")
    print(task_title, end="")
