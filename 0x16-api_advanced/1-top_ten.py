#!/usr/bin/python3
""" prints the titles of the first 10 hot posts listed for a given subreddit
"""
import json
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed"""
    n = 0
    try:
        r = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                         .format(subreddit),
                         headers={'User-agent': 'yourbot'},
                         allow_redirects=False)
        titles = json.loads(r.text)["data"]["children"]
        for e in titles[1:]:
            print(e["data"]["title"])
    except (KeyError, json.decoder.JSONDecodeError):
        print(None)
