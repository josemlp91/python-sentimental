from django.utils import timezone

from django.db import models

class CognitiveServicesConfig(models.Model):
    api_key = models.CharField(max_length=32, verbose_name="Api Key")
    language = models.CharField(max_length=10, default="es", verbose_name="Language")

    class Meta:
        verbose_name = "Microsoft Cognitive Services Config"

    def __str__(self):
        return str(self.id)

class TwitterConfig(models.Model):
    username = models.CharField(max_length=255, verbose_name="Username")
    api_key = models.CharField(max_length=255, verbose_name="Api Key")
    access_secret = models.CharField(max_length=255, verbose_name="Access Secret")
    consumer_key = models.CharField(max_length=255, verbose_name="Consumer Key")
    consumer_secret = models.CharField(max_length=255, verbose_name="Consumer Secret")

    class Meta:
        verbose_name = "Twitter Services Config"

    def __str__(self):
        return self.username


class TwitterSearchedTopics(models.Model):
    topic = models.CharField(max_length=255, verbose_name="Topic")
    create_datetime = models.DateTimeField(auto_created=True, verbose_name="Create Datetime")

    class Meta:
        verbose_name = "Twitter Searched Topic"

    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_datetime = timezone.now()

        return super(TwitterSearchedTopics, self).save(*args, **kwargs)


class SentimentalScores(models.Model):
    create_datetime = models.DateTimeField(auto_created=True, verbose_name="Create Datetime")
    score = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Score")
    search = models.ForeignKey('TwitterSearchedTopics', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sentimental Score"

    def __str__(self):
        return "{0}: {1}".format(self.search.topic, self.score)

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_datetime = timezone.now()

        return super(SentimentalScores, self).save(*args, **kwargs)
