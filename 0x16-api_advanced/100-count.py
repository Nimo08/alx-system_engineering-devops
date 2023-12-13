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


def count_words(subreddit, word_list, after='', res=None):
    """
     Prints a sorted count of given keywords (case-insensitive,
     delimited by spaces.
     If no posts match or the subreddit is invalid, print nothing.
    """
    if res is None:
        res = {}

    if not res:
        for word in word_list:
            if word.lower() not in res:
                res[word.lower()] = 0
    if after is None:
        sorted_res = sorted(res.items(), key=lambda q: (-q[1], q[0]))
        for word, count in sorted_res:
            if count > 0:
                print(f'{word}, {count}')
        return None

    user_agent = 'RedditBot'
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': user_agent}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            posts = response.json()['data']['children']
            next_after = response.json()['data']['after']

            for post in posts:
                title = post['data']['title']
                lower_word = [word.lower() for word in title.split(' ')]
                for word in res.keys():
                    res[word] += lower_word.count(word)
    except Exception:
        return None
    count_words(subreddit, word_list, after=next_after, res=res)
