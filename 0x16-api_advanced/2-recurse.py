#!/usr/bin/python3
"""
Module contains a recursive function that queries the Reddit
API and returns a list containing the titles of all
hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import json
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
     Returns a list containing the titles of all hot
     articles for a given subreddit
     If no results are found for the given subreddit,
     the function should return None.
    """
    if hot_list is None:
        hot_list = []
    user_agent = 'RedditBot'
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': user_agent}
    params = {'after': after} if after else {}
    try:
        response = requests.get(url=url, headers=headers,
                                params=params, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None
    if response.status_code == 200:
        subreddit_posts = response.json().get('data', {})
        posts = subreddit_posts.get('children', [])

        for post in posts:
            title = post['data'].get('title', 'Title not available')
            hot_list.append(title)
        next_after = subreddit_posts.get('after')
        if next_after:
            recurse(subreddit, hot_list=hot_list, after=next_after)
    return hot_list
