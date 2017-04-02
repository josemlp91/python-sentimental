# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.TopicListAPIView.as_view(),
        name='topic-list'
    ),

    url(
        regex=r'^current-topic/$',
        view=views.LastTopicRetrieveAPIView.as_view(),
        name='current-topic'
    ),

    url(
        regex=r'^post-topic/$',
        view=views.PostTopicCreateAPIView.as_view(),
        name='post-topic'
    ),

    url(
        regex=r'^score-topic/$',
        view=views.GetScoreTopicAPI.as_view(),
        name='score-topic'
    )





]
