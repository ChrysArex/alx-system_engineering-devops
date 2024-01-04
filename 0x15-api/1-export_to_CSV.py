#!/usr/bin/python3
""" Python script to export data in the CSV format.
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
    emp_name = r.json().get("username")
    r = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    f_name = id_ + ".csv"
    with open(f_name, "w", encoding="utf-8") as f:
        for i in range(starting_point.get(id_), starting_point.get(id_) + 20):
            first = '"{}","{}",'.format(r[i].get('userId'), emp_name)
            second = '"{}","{}"\n'.format(r[i].get('completed'),
                                          r[i].get('title'))
            f.write(first + second)
