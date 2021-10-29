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

#Code to upload API credentials:
#export GOOGLE_APPLICATION_CREDENTIALS="/Users/bmkuter/Downloads/ec601-327317-1968a8f61c7a.json"

#Parameters
sentiment_score = 0
sentiment_magnitude = 0.1
neutral_test_string = "Today is a Monday."
happy_test_string = "I love puppies and cuddles!"
bad_test_string =  "COVID sucks"
beer_test_string = "Beer, brewery, hoppy, sour, ale, belgian, cider, Trillium, tequila"

client = language_v1.LanguageServiceClient()

document = language_v1.Document(content=neutral_test_string, type_=language_v1.Document.Type.PLAIN_TEXT)
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
#Only Print if sentiment score is above some threshold?
#(sentiment.score >= sentiment_score) & (sentiment.magnitude > sentiment_magnitude):

print("Neutral String:\nScore: " + str(sentiment.score) + "   Magnitude: " + str(sentiment.magnitude))

document = language_v1.Document(content=happy_test_string, type_=language_v1.Document.Type.PLAIN_TEXT)
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

print("Happy String:\nScore: " + str(sentiment.score) + "   Magnitude: " + str(sentiment.magnitude))

document = language_v1.Document(content=bad_test_string, type_=language_v1.Document.Type.PLAIN_TEXT)
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

print("Bad String:\nScore: " + str(sentiment.score) + "   Magnitude: " + str(sentiment.magnitude))

document = language_v1.Document(content=beer_test_string, type_=language_v1.Document.Type.PLAIN_TEXT)
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

print("Beer String:\nScore: " + str(sentiment.score) + "   Magnitude: " + str(sentiment.magnitude))
