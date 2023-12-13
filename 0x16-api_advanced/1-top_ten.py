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
    user_agent = 'RedditBot'
    url = f'https://www.reddit.com/r/{subreddit}/top.json'
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url=url, headers=headers,
                                allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(None)
        return

    if response.status_code == 200:
        subreddit_posts = response.json().get('data', {}).get('children', [])
        if subreddit_posts:
            for post in subreddit_posts:
                title = post['data'].get('title', 'Title not available')
                print(title)
    else:
        print(None)
