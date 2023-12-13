#!/usr/bin/python3
"""
Module contains function that queries the Reddit API
and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""


import json
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit
    If not a valid subreddit, print None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "YourBot/1.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            posts = response.json()["data"]["children"]
            for post in posts:
                print(post["data"]["title"])
        except KeyError:
            print("Invalid subreddit. Please provide a valid subreddit.")
    else:
        print(None)
