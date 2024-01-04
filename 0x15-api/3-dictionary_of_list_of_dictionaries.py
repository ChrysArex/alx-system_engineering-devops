#!/usr/bin/python3
""" Python script to export data in the CSV format.
"""
if __name__ == "__main__":
    import json
    import requests
    import sys
    tasks = []
    id_ = ""
    all_data = {}
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
    r = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    f_name = "todo_all_employees.json"
    with open(f_name, "w", encoding="utf-8") as f:
        for id_ in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            r1 = requests.get(
                    f'https://jsonplaceholder.typicode.com/users/{id_}'
                    )
            emp_name = r1.json().get("username")

            for i in range(starting_point.get(id_),
                           starting_point.get(id_) + 20):
                data = {
                        "username": emp_name,
                        "task": r[i].get("title"),
                        "completed": r[i].get("completed"),
                        }
                tasks.append(data)
            all_data[id_] = tasks
            tasks = []
        f.write(json.dumps(all_data))
