from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    points = models.IntegerField(default=0)


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    event_date = models.DateTimeField("date event")

    def __str__(self):
        return str(self.id) + " : " + self.event_text + " " + str(self.pub_date) + " "


class Possibility(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    description_text = models.CharField(max_length=200)
    quotation = models.FloatField(default=2.0)
    RESULT_CHOICES = [("Pending", "Pending"), ("Win", "Win"), ("Lose", "Lose")]
    result = models.CharField(max_length=10, choices=RESULT_CHOICES, default="Pending")

    def __str__(self):
        return self.event.event_text + " " + self.description_text


class Bet(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    possibility = models.ForeignKey(Possibility, on_delete=models.CASCADE)
    putting = models.FloatField(default=0.0)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.event_text + " " + " " + str(self.putting)
