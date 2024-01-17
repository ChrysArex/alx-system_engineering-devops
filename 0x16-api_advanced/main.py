#!/usr/bin/python3
"""
2-main
"""
import sys

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        print("resultat dans le main apres traitement : {}".format(result))
        if result is not None:
            print(len(result))
        else:
            print("None")