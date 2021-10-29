import requests
import os
import json
# For displaying the data after
import pandas as pd
import csv
# Imports the Google Cloud client library
# https://cloud.google.com/natural-language/docs/reference/libraries#cloud-console
from google.cloud import language_v1
# For UI generation: https://formulae.brew.sh/formula/python-tk@3.9
# https://www.tutorialspoint.com/how-to-create-hyperlink-in-a-tkinter-text-widget
import tkinter as tk
from tkHyperLinkManager import HyperlinkManager
import webbrowser
from functools import partial
import pytest


bearer_token = os.environ.get("BEARER_TOKEN")

#Parameters
start_time = "2021-09-26T00:00:00.040Z"
end_time = "2021-03-31T00:00:00.000Z"
max_results = 10
expansions = 'author_id'
tweet_fields = 'author_id'
user_fields = 'username,url'
keyword ='''
Hello World
'''

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': keyword,
                'max_results': max_results,
                'tweet.fields': tweet_fields,
                'user.fields' : user_fields,
                'expansions': expansions
                }

def callback(url):
   webbrowser.open_new_tab(url)

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

#Tests to see if the search returned an emnpty list, so asserts on an empty list.
def test_tweets():
    no_results_response = "{'meta': {'result_count': 0}}"
    local_tweet = connect_to_endpoint(search_url, query_params)
    assert str(local_tweet) == no_results_response

def main():
    print("Testing Twitter API via Pytest:")
    test_tweets()

if __name__ == "__main__":
    main()