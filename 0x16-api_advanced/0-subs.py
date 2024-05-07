#!/usr/bin/python3
"""This queries Reddit"""

import requests


def number_of_subscribers(subreddit):
    """This queries a subreddit and retrieve number of subcribers"""

    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Send a custom user-agent to avoid too many requests error
    headers = {'User-agent': 'My user Agent 1.0'}

    # Send a GET request to the reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request is successful and not a redirect
    if response.status_code == 200:
        # Parse JSON response to extract number of subcribers
        data = response.json().get('data', {})
        sub_count = data.get('subscribers', 0)
        return sub_count
    else:
        return 0
