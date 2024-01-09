from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Event
from django.template import loader


def index(request):
    latest_event_list = Event.objects.order_by("-pub_date")[:5]
    context = {"latest_event_list": latest_event_list}
    return render(request, "minamax/index.html", context)

    # def index(request):
    latest_event_list = Event.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.event_text for q in latest_event_list])
    return HttpResponse(output)


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "minamax/detail.html", {"event": event})


def results(request, event_id):
    response = "You're looking at the results of event %s."
    return HttpResponse(response % event_id)
