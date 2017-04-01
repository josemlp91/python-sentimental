from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import TwitterSearchedTopics, SentimentalScores
from .utils import get_twitter_search, get_sentiment_score


@csrf_exempt
def post_topic(request):

    if request.method == 'GET':
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'})

    if request.POST.get("topic"):
        newtopic_str =request.POST.get("topic")
        newtopic_obj = TwitterSearchedTopics(topic=newtopic_str)
        newtopic_obj.save()

        return JsonResponse({'status': 'success', 'message': 'Topic has been change'})
    return JsonResponse({'status': 'error', 'message': 'Not topic sent'})


def get_current_topic(request):
    topic_item = TwitterSearchedTopics.objects.all().order_by('create_datetime').last()
    return JsonResponse({'status': 'success', 'topic': topic_item.topic})


def get_last_topics(request):
    topics = TwitterSearchedTopics.objects.all().order_by('create_datetime')

    topic_array =[]
    for topic_item in topics:
        topic_array.append(topic_item.topic)

    return JsonResponse({'status': 'success', 'topics': topic_array})


def get_score_topic(request):

    sum_scores = 0
    count = 0
    score_average = 0

    topic_item = TwitterSearchedTopics.objects.all().order_by('create_datetime').last()
    twitter_array = get_twitter_search(topic_item.topic)
    twitter_scoreded_set = []

    for twitter_item_text in twitter_array:
        count += 1
        item_score = get_sentiment_score(twitter_item_text)
        sum_scores += item_score

        twitter_item = {'text': twitter_item_text, 'score': item_score}
        twitter_scoreded_set.append(twitter_item)

    if count > 0:
        score_average = sum_scores / count

    scored_obj = SentimentalScores(score=score_average, search=topic_item)
    scored_obj.save()

    return JsonResponse({'status': 'success',
                         'topic': topic_item.topic,
                         'twitter_scored_set':twitter_scoreded_set,
                         'score_average':score_average})
