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
    user_agent = 'RedditBot'
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url=url, headers=headers,
                                params={'after': after}, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None
    if response.status_code == 200:
        subreddit_posts = response.json().get('data', {})
        posts = subreddit_posts.get('children', [])

        for post in posts:
            title = post['data'].get('title', '').lower()
            for word in word_list:
                word_lower = word.lower()
                if (
                    f' {word_lower} ' in f' {title} ' or
                    f' {word_lower}.' in f' {title} ' or
                    f' {word_lower}!' in f' {title} ' or
                    f' {word_lower}_' in f' {title} '
                   ):
                    res[word_lower] = res.get(word_lower, 0) + 1
        after = subreddit_posts.get('after')
        if after:
            count_words(subreddit, word_list, res=res, after=after)
        sorted_res = sorted(res.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_res:
            print(f'{word}: {count}')
    return res
