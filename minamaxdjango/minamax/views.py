from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from django.template import loader
from django.shortcuts import render


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, event_id):
    return HttpResponse("You're looking at question %s." % event_id)


def results(request, event_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % event_id)


def vote(request, event_id):
    return HttpResponse("You're voting on question %s." % event_id)
