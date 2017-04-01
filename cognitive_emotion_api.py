# -*- coding: utf-8 -*-

import httplib, urllib, base64, json
import secret_config
from twitter import *

def get_twitter_search(search_query):
	twitter = Twitter(
		auth = OAuth(secret_config.twitter_config['api_key'],
		secret_config.twitter_config['access_secret'],
		secret_config.twitter_config['consumer_key'],
		secret_config.twitter_config['consumer_secret'])
	)

	query = twitter.search.tweets(q = search_query)
	tweets_array = []
	for result in query["statuses"]:
		tw = result["text"]
		tweets_array.append(tw)
	
	return tweets_array
		

def get_sentimental_score_from_twitter(twitter_array):

	sum_scores = 0
	count = 0
	score_average = 0
	for twitter_status in twitter_array:
		count += 1
		print twitter_status
		sum_scores += get_sentiment_score(twitter_status)

	if count > 0:	
		score_average = sum_scores / count	

	return score_average

def get_sentiment_score(text):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '{0}'.format(secret_config.cognitive_config['api_key']),
    }

    params = urllib.urlencode({})
    body = {"documents": [{"lenguage": "es", "id":1, "text": text}]}
    body = json.dumps(body)
    
    try:
	    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	    conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, body, headers)
	    response = conn.getresponse()
	    data = response.read()
	    data = json.loads(data)
	    score = data.get("documents")[0].get("score")
	    conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    print score
    return score

twitter_array = get_twitter_search("Ejemplo")
score_average = get_sentimental_score_from_twitter(twitter_array)

print "---------------------------"
print "AVERAGE"
print score_average
print "---------------------------"