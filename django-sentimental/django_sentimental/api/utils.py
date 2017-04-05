# -*- coding: utf-8 -*-

import httplib, urllib, base64, json
from django.core.exceptions import ObjectDoesNotExist
from twitter import *
from .models import CognitiveServicesConfig, TwitterConfig

##############################################################################################

def get_congitive_service_config():
    try:
        cognitive_service_config = CognitiveServicesConfig.objects.get(id=1)
    except ObjectDoesNotExist:
        raise ("No exite configuración asociada a la API Cognitiva de Microsoft")
    return cognitive_service_config


def get_twitter_config():
    try:
        twitter_config = TwitterConfig.objects.get(id=1)
    except ObjectDoesNotExist:
        raise ("No exite configuración asociada a la API Twitter")
    return twitter_config

##############################################################################################

def get_twitter_search(search_query):

    twitter_conf = get_twitter_config()
    twitter = Twitter(
        auth=OAuth(twitter_conf.api_key,
                   twitter_conf.access_secret,
                   twitter_conf.consumer_key,
                   twitter_conf.consumer_secret)
    )

    query = twitter.search.tweets(q=search_query)
    tweets_array = []
    for result in query["statuses"]:
        tw = result["text"]
        tweets_array.append(tw)
    # print tw

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

    cognitive_api_conf = get_congitive_service_config()
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '{0}'.format(cognitive_api_conf.api_key),
    }

    params = urllib.urlencode({})
    body = {"documents": [{"lenguage": "es", "id": 1, "text": text}]}
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
        raise ("[Errno {0}] {1}".format(e.errno, e.strerror))

    return score




