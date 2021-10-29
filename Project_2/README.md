**Benjamin Kuter**  
**Project 2**  
**EC601 - Fall 2021**  

**Use Boston_Beer.py**

**If the code doesn't work, make sure your environment variables are set up with the proper tokens for Google & Twitter's APIs.**

**User Stories:**

-I want to know what my current local beer scene is like!

-I want a currated list of the best breweries in town.

-I only want to know about breweries people have enjoyed.

-I want to know about new releases!

-I want to be able to see what else the author has mentioned.


**MVP:**

First and foremost we will need to interact with the Twitter API and return relevant local breweries. We also need a way to sort those to find which are strongly positive. This will require Google's Natural Language AI API. Finally we need some way to display the results. A simple dark-mode GUI should suffice here, which prints the results. Each result will also contain a hyperlink back to the original Tweet.

**Phase 1(a):**  
To start I copied several of the python example codes for the Twitter API v2 through their github, looking for one that was able to very generally search twitter for Tweets containing some keywords. I added my bearer token to my local environment, and made sure to not include it in a GitHub push. This ended up being "recent_search.py". Within this I customized the example to look for keywords relating to Boston, Beer, and Fall. Unfortunately the "query" parameter doesn't seem to allow for conditional logic within the keywords (i.e. Boston ∧ Beer ∧ Fall). Instead of I query "Boston Beer Fall", it returns with any Tweet containing any of these...  

After writing the above paragraph I realised I must be missing something, as this type of Boolean search seems very important. After delving into the API even further, I think I have found a section of operators for keywords that enable the functionality I so desire [[here](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query#list)].  

**Phase 2**
I then added a *.csv function to export the JSON as a csv, so that it can later be made into a sortable list through Google's NLP.  

To prepare for adding Google's NLP, I changed the name of my aforementioned sample file to "Boston_Beer.py", and added include statements for the required Google NLP API.

After adding Google NLP API, the program now takes the text found for each tweet and saves to CSV (which acts as a way to format data into an easier format than JSON). This formatted text is then fed back into the program. Sentiment analysis is performed on each, and the analysis returned along with the original text. The tweet is only printed if generally positive (sentiment score >= .3) and the magnitude is greater than 1 (used to filter out spam messages and really lazy ads).

Results are mixed, with tweets ranging from farmers markets to calls for political action. To fix this, as the goal of the project is to find beer releases, I have hardcoded breweries. This theoretically makes it harder to find new releases, but also curated lists have their benefits. I have also removed the retweet filter, once more enabling retweets. My thinking is that these could help lead to discovery through sentiment analysis.

To return the results to the user, a simple GUI is being created through Tkinter. These results will be ordered through a tuple-list sorting function found on geeksforgeeks, which was slightly altered to invert the search order.

After sorting, the username is paired with the user_id through a dictionary and original query parameters. This information, as well as the various scores and original text, are packed into a tuple. This is then printed through to my simple gui.

I decided it would be good to add a hyperlink back to the original tweet. To do this, I created another list for the original tweet IDs from the JSON, and appended these to the tuple for each tweet. I then created a generic twitter url ```http://www.twitter.com/anyuser/status/{}".format(x[4])``` that would take each ID and format into the proper URL. I then used a tkinter-related function found on [tutorialspoint](https://www.tutorialspoint.com/how-to-create-hyperlink-in-a-tkinter-text-widget) to insert hyperlinks into text fields instead of labels.

Optimisations can be made in the search-algorithms used for this project. I have not yet studied algorithms and was more interested in communicating with the various APIs. With O(n^2) the sort used to sort the tuples is pretty slow.

When running the code, one must set environment variables for Google Natural Language and for the Twitter API. This can be done for the Twitter API through line 19 of boston_beer.py, and through this [link](https://cloud.google.com/docs/authentication/getting-started) for Google's NLP. Specifically the "Setting the environment variable" section. As always, be mindful of required libraries. Specifically Pandas, aforementioned HyperlinkManager, webbrowser, etc. All libraries can be found in the top of Boston_Beer.py.  


**Project 3(a):**

Tests:

-What happens if there are no results? How does the program sort in this case? What does the GUI look like? If no results are returned, the program crashes while populating the data frame. I believe this is because is no data. To correct this, a the results JSON is compared to the known output when no results are found. If these match the terminal prints "No results!" and gracefully exits.  

-Test illustrating user story. What happens as the user interacts with the program?

-Twitter API test. Can we get the results we want?  How much noise is there? When tested with (through twitter_api_test.py), we can validate that our API bearer tokens are valid and working, with the expected zero results when random noise is searched for.  

-Google NLP test. Enter strings to see generally what words return. What kind of sentiments do our big keywords have? Beer, brewery, hoppy, sour, ale, belgian, cider, Trillium, tequila, etc. When testing the google api (google_api_test.py), we see expected results where the happy test string returns a high sentiment score of .9 and magnitude of .9, the bad string returns close to -1 with a magnitude of .8, and our neutral string returns a 0.0 for score and magnitude. Additionally this test shows our API key is valid and working, and the general syntax is correct. We introduced another string related to general beer terminology, which had a score of 0.5 and magnitude of 0.5, indicating that any tweets we are looking for may have an inherent positive bias.