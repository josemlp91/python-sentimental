from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from .serializer import TopicSerializer
from .models import TwitterSearchedTopics, SentimentalScores
from .utils import get_twitter_search, get_sentiment_score



class PostTopicCreateAPIView(CreateAPIView):
    queryset = TwitterSearchedTopics.objects.all()
    serializer_class = TopicSerializer

class TopicListAPIView(ListAPIView):
    queryset = TwitterSearchedTopics.objects.all()
    serializer_class = TopicSerializer


class LastTopicRetrieveAPIView(APIView):
    def get(self, request, format=None):
        topic_item = TwitterSearchedTopics.objects.all().order_by('create_datetime').last()
        return JsonResponse({'status': 'success', 'topic': topic_item.topic})

    def post(self, request, format=None):
        return JsonResponse({'status': 'error', 'message': 'Method do not allowed'})


class GetScoreTopicAPI(APIView):

    def get(self, request, format=None):

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

    def post(self, request, format=None):
        return JsonResponse({'status': 'error', 'message': 'Method do not allowed'})
