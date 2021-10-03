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


# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")



#Parameters
sentiment_score = 0
sentiment_magnitude = 0.1
start_time = "2021-09-26T00:00:00.040Z"
end_time = "2021-03-31T00:00:00.000Z"
max_results = 10
expansions = 'author_id'
tweet_fields = 'author_id'
user_fields = 'username,url'
keyword ='''
("Distraction Brewing Company" OR
"Democracy Brewing" OR
"Turtle Swamp Brewing" OR
"Dorchester Brewing Company" OR
"Aeronaut Brewery" OR
"Winter Hill Brewing" OR
"Jack’s Abby" OR
"Cambridge Brewing Company" OR
"Harpoon Brewery" OR
"Night Shift Brewing" OR
"Trillium Brewing Company"
"Downeast Cider" OR
"Artifact Cider"
)
lang:en
(is:retweet OR -is:retweet)
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

# Instantiates a client
client = language_v1.LanguageServiceClient()

# Function to sort the list of tuples by its second item
def Sort_Tuple(tup):
    # Taken from: https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-by-second-item/
    # Modified to invert sort order.
    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst-i-1):
            if (tup[j][1] < tup[j + 1][1]):
                temp = tup[j]
                tup[j]= tup[j + 1]
                tup[j + 1]= temp
    return tup

# Define a callback function
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


def main():
    json_response = connect_to_endpoint(search_url, query_params)

    #print(json.dumps(json_response, indent=4, sort_keys=True))
    #return

    df = pd.DataFrame(json_response['data'])
    df.to_csv('response_python.csv')
    df = pd.read_csv('response_python.csv')
    saved_column_text = df.text
    saved_column_author_id = df.author_id
    saved_column_tweet_id = df.id

    usernames = []
    for user in json_response["includes"]["users"]:
        usernames.append(user)


    output_breweries_list = []

    #For each text in the csv, perform sentiment analysis
    #print("\n\n\n\n")   #Formatting
    n = 0
    for i in saved_column_text:
        #Google Natural Language Section
        #print(i)
        local_username = "hello"
        local_tweet_id = saved_column_tweet_id[n]
        document = language_v1.Document(content=i, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
        #Only Print if sentiment score is above some threshold?
        if (sentiment.score >= sentiment_score) & (sentiment.magnitude > sentiment_magnitude):
            for each in usernames:
                #print(each)
                #print(each['id'])
                if (saved_column_author_id[n] == int(each['id'])):
                    #print("MATCH")
                    local_username = each['username']
                    #print(local_username)
            output_breweries_list.append(tuple((i,sentiment.score,sentiment.magnitude, local_username, local_tweet_id)))
            #print("Text: {}".format(i))
            #print("Sentiment: Score {}, Magnitude {}".format(sentiment.score, sentiment.magnitude))
            #print("\n\n\n\n")
        n = n+1
    sorted_breweries_list = Sort_Tuple(output_breweries_list)


    #for x in sorted_breweries_list:
        #print(x)

    #print("({})".format(", ".join(Sort_Tuple(output_breweries_list))))
    #GUI Business, learned from https://www.python-course.eu/tkinter_text_widget.php
    window = tk.Tk()
    window.title("Boston Beer Buddy")
    window.geometry("1075x800")
    S = tk.Scrollbar(window)
    T = tk.Text(window, height=len(sorted_breweries_list)*5, width=150)
    T.tag_configure('big', font=('Verdana', 16, 'bold'))
    T.tag_configure('tweet', font=('Verdana', 12))
    T.tag_configure('url', foreground='#0645AD',font=('Verdana', 12, 'italic'))
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.pack();
    hyperlink= HyperlinkManager(T)
    for x in sorted_breweries_list:
        hyperlink_text = "http://www.twitter.com/anyuser/status/{}".format(x[4])
        T.insert(tk.END, "Author: ", 'big')
        T.insert(tk.END, x[3], 'big')
        T.insert(tk.END, "\n")
        T.insert(tk.END, "Tweet: ",'tweet')
        T.insert(tk.END, x[0],'tweet')
        T.insert(tk.END, "\n")
        T.insert(tk.END, "Original Tweet: ", 'tweet')
        #Hyperlink learned from https://www.tutorialspoint.com/how-to-create-hyperlink-in-a-tkinter-text-widget
        T.insert(tk.END, hyperlink_text,hyperlink.add(partial(webbrowser.open,hyperlink_text)))
        T.insert(tk.END, "\n\n\n\n\n")
    window.mainloop()

if __name__ == "__main__":
    main()
