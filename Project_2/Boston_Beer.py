import requests
import os
import json
# For displaying the data after
import pandas as pd
import csv
# Imports the Google Cloud client library
# https://cloud.google.com/natural-language/docs/reference/libraries#cloud-console
from google.cloud import language_v1

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

#Parameters
start_time = "2021-09-26T00:00:00.040Z"
end_time = "2021-03-31T00:00:00.000Z"
max_results = 25
keyword = "(#beer OR #brewery OR #craftbeer) (Boston OR Somerville OR Cambridge) lang:en -is:retweet"
example_text = "Hello World!"

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': keyword,
                'start_time':start_time,
                'max_results': max_results,
                }

# Instantiates a client
client = language_v1.LanguageServiceClient()



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

    #print(json.dumps(json_response, indent=4, sort_keys=True))

    df = pd.read_csv('response_python.csv')
    saved_column = df.text

    #For each text in the csv, perform sentiment analysis
    print("\n\n\n\n\n\n")   #Formatting
    for i in saved_column:
        #Google Natural Language Section
        document = language_v1.Document(content=i, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
        #Only Print if sentiment score is good, i.e. above 0.5?
        if (sentiment.score >= .3) & (sentiment.magnitude > 1):
            print("Text: {}".format(i))
            print("Sentiment: Score {}, Magnitude {}".format(sentiment.score, sentiment.magnitude))
            print("\n\n\n\n\n\n")


if __name__ == "__main__":
    main()
