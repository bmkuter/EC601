import requests
import os
import json
# For displaying the data after
import pandas as pd
import csv

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

#Parameters
start_time = "2021-09-18T00:00:00.040Z"
end_time = "2021-03-31T00:00:00.000Z"
max_results = 25
keyword = "(#beer OR #brewery OR #craftbeer) (Boston OR Somerville OR Cambridge) lang:en -is:retweet"

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': keyword,
                'start_time':start_time,
                'max_results': max_results,
                }


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


def main():
    json_response = connect_to_endpoint(search_url, query_params)

    df = pd.DataFrame(json_response['data'])
    df.to_csv('response_python.csv')

    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
