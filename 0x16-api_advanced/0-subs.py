#!/usr/bin/python3
"""Define the number_of_subscribers function"""
import json
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit"""
    headers = {'User-Agent': "myapp1"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    try:
        r = requests.get(url, headers, allow_redirects=False)
        return int(r.json().get("data").get("subscribers"))
    except AttributeError:
        return 0
