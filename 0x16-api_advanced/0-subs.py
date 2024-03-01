#!/usr/bin/python3
"""the number of subscribers (not active users, total subscribers)
for a given subreddit
"""
import json
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers or 0"""
    n = 0
    try:
        r = requests.get("https://www.reddit.com/r/{}/about.json".format(
                          subreddit),
                         headers={'User-agent': 'ojij'},
                         allow_redirects=False)
        return int(json.loads(r.text)["data"]["subscribers"])
    except (KeyError, json.decoder.JSONDecodeError):
        return 0
