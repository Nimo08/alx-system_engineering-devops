#!/usr/bin/python3
"""
Module contains a recursive function that queries the Reddit
API, parses the title of all hot articles, and prints a
sorted count of given keywords (case-insensitive,
delimited by spaces.
Javascript should count as javascript, but java should not).
"""


import json
import requests


def count_words(subreddit, word_list, res=None, after=None):
    """
     Prints a sorted count of given keywords (case-insensitive,
     delimited by spaces.
     If no posts match or the subreddit is invalid, print nothing.
    """
    if res is None:
        res = {}

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json" \
              f"?limit=100&after={after}"

    headers = {"User-Agent": "Bot/1.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            posts = response.json()["data"]["children"]
            for post in posts:
                title = post["data"]["title"].lower()
                for word in word_list:
                    if word.lower() in title:
                        res[word] = res.get(word, 0) + \
                                    title.count(word.lower())
        except KeyError:
            print("Invalid subreddit.")
            return

        after = response.json()["data"].get("after")
        if after:
            count_words(subreddit, word_list, res, after)
        else:
            sorted_counts = sorted(res.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print()
