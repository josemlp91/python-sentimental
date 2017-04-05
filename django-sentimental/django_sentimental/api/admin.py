# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin

from .models import CognitiveServicesConfig, TwitterConfig, TwitterSearchedTopics, SentimentalScores

admin.site.register(CognitiveServicesConfig)
admin.site.register(TwitterConfig)

admin.site.register(TwitterSearchedTopics)
admin.site.register(SentimentalScores)
