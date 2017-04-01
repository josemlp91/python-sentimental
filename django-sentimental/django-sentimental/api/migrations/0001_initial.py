# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SentimentalScores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_created=True, verbose_name=b'Create Datetime')),
                ('score', models.DecimalField(decimal_places=2, max_digits=4, verbose_name=b'Score')),
            ],
            options={
                'verbose_name': 'Sentimental Scores',
            },
        ),
        migrations.CreateModel(
            name='TwitterSearchedTopics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_created=True, verbose_name=b'Create Datetime')),
                ('topic', models.CharField(max_length=255, verbose_name=b'Topic')),
            ],
            options={
                'verbose_name': 'Twitter Searched Topics',
            },
        ),
    ]
