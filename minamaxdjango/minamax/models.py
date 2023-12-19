from django.db import models


class Event(models.Model):
    event_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Bet(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
