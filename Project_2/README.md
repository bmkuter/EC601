**Benjamin Kuter**  
**Project 2**  
**EC601 - Fall 2021**  




**Phase 1(a):**  
To start I copied several of the python example codes for the Twitter API v2 through their github, looking for one that was able to very generally search twitter for Tweets containing some keywords. I added my bearer token to my local environment, and made sure to not include it in a GitHub push. This ended up being "recent_search.py". Within this I customized the example to look for keywords relating to Boston, Beer, and Fall. Unfortunately the "query" parameter doesn't seem to allow for conditional logic within the keywords (i.e. Boston ∧ Beer ∧ Fall). Instead of I query "Boston Beer Fall", it returns with any Tweet containing any of these...  

After writing the above paragraph I realised I must be missing something, as this type of Boolean search seems very important. After delving into the API even further, I think I have found a section of operators for keywords that enable the functionality I so desire [[here](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query#list)].  

I then added a *.csv function to export the JSON as a csv, so that it can later be made into a sortable list through Google's NLP.  

To prepare for adding Google's NLP, I changed the name of my aforementioned sample file to "Boston_Beer.py", and added include statements for the required Google NLP API.

After adding Google NLP API, the program now takes the text found for each tweet and saves to CSV (which acts as a way to format data into an easier format than JSON). This formatted text is then fed back into the program. Sentiment analysis is performed on each, and the analysis returned along with the original text. The tweet is only printed if generally positive (sentiment score >= .3) and the magnitude is greater than 1 (used to filter out spam messages and really lazy ads). 
