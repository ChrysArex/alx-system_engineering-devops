#!/usr/bin/python3
"""the number of subscribers (not active users, total subscribers)
for a given subreddit
"""
import json
import requests


def number_of_subscribers(subreddit):
    """return the number of sebscribers or 0"""
    n = 0
    try:
        r = requests.get("https://www.reddit.com/r/{}/about.json".format(
                          subreddit),
                         headers={'User-agent': 'yourbot2'},
                         allow_redirects=False)
        return json.loads(r.text)["data"]["subscribers"]
    except (KeyError, json.decoder.JSONDecodeError):
        return 0
