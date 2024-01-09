from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Event
from django.template import loader
from django.shortcuts import render


def index(request):
    latest_question_list = Event.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    try:
        question = Event.objects.get(pk=question_id)
    except Event.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "minamax/detail.html", {"question": question})


def results(request, event_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % event_id)


def vote(request, event_id):
    return HttpResponse("You're voting on question %s." % event_id)
