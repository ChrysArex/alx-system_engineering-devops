#!/usr/bin/python3
"""the number of subscribers (not active users, total subscribers)
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers or 0"""
    r = requests.get("https://www.reddit.com/r/{}/about.json".format(
                        subreddit),
                     headers={'User-agent': 'ojij'},
                     allow_redirects=False)
    if r.status_code == 200:
        return r.json().get("data").get("subscribers")
    elif r.status_code == 404:
        return 0
