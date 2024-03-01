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
        try:
            count = r.json().get("data").get("subscribers")
            return count
        except KeyError:
            return 0
    else:
        return 0
