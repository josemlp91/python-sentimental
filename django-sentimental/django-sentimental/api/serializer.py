from rest_framework.serializers import ModelSerializer

from .models import TwitterSearchedTopics


class TopicSerializer(ModelSerializer):
  class Meta:
    model = TwitterSearchedTopics
    fields = [
        'topic'
    ]
