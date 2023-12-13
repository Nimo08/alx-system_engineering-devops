#!/usr/bin/python3
"""
Module contains a function that queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import json
import requests


def number_of_subscribers(subreddit):
    """
    Function queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
    """
    user_agent = 'RedditBot'
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': user_agent}

    try:
        response = requests.get(url=url, headers=headers,
                                allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return 0
    if response.status_code == 200:
        subreddit_num = response.json().get('data', {})
        num_users = subreddit_num.get('subscribers', 0)
        return num_users
    else:
        return 0
