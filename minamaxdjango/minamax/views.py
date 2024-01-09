from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the bets index.")


def detail(request, event_id):
    return HttpResponse("You're looking at question %s." % event_id)


def results(request, event_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % event_id)


def vote(request, event_id):
    return HttpResponse("You're voting on question %s." % event_id)


from .models import Event


def index(request):
    latest_question_list = Event.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.event_text for q in latest_question_list])
    return HttpResponse(output)
