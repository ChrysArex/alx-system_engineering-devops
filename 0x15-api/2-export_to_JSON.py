#!/usr/bin/python3
""" Python script to export data in the CSV format.
"""
if __name__ == "__main__":
    import json
    import requests
    import sys
    id_ = sys.argv[1]
    tasks = []
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
    emp_name = r.json().get("username")
    r = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    f_name = id_ + ".json"
    with open(f_name, "w", encoding="utf-8") as f:
        for i in range(starting_point.get(id_), starting_point.get(id_) + 20):
            data = {
                    "task": r[i].get("title"),
                    "completed": r[i].get("completed"),
                    "username": emp_name
                    }
            tasks.append(data)
        f.write(json.dumps({id_: tasks}))
