# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.get_last_topics,
        name='test'
    ),

    url(
        regex=r'^get-current-topic/$',
        view=views.get_current_topic,
        name='get-current-topic'
    ),

    url(
        regex=r'^post-topic/$',
        view=views.post_topic,
        name='post-topic'
    ),

    url(
        regex=r'^get-score-topic/$',
        view=views.get_score_topic,
        name='get-score-topic'
    )





]
