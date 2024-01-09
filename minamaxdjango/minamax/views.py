from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Event
from django.template import loader
from django.shortcuts import render


def index(request):
    latest_event_list = Event.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.event_text for q in latest_event_list])
    return HttpResponse(output)


def detail(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    return render(request, "minamax/detail.html", {"question": event})


def results(request, event_id):
    response = "You're looking at the results of event %s."
    return HttpResponse(response % event_id)
