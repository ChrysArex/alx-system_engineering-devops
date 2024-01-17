#!/usr/bin/python3
""" prints the titles of the first 10 hot posts listed for a given subreddit
"""
import json
import requests


def recurse(subreddit, after=None, hot_list=[]):
    """prints the titles of the first 10 hot posts listed"""
    params = {'limit': 25}
    result = None
    if after:
        params['after'] = after
    try:
        r = requests.get("https://www.reddit.com/r/{}/hot.json?"
                         .format(subreddit),
                         headers={'User-agent': 'yourbot'},
                         params=params,
                         allow_redirects=False)
        titles = json.loads(r.text)["data"]["children"]
        for e in titles[1:]:
            hot_list.append(e["data"]["title"])
        if json.loads(r.text)['data'].get('after'):
            after = json.loads(r.text)['data'].get('after')
            recurse(subreddit, after, hot_list)
        else:
            result = hot_list
            return result
    except KeyError:
        return None
