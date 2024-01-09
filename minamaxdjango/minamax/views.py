from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import Http404
from django.http import HttpResponse
from .models import Event
from django.template import loader
from django.shortcuts import render
from .forms import CustomUserCreationForm


def index(request):
    latest_question_list = Event.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    try:
        question = Event.objects.get(pk=question_id)
    except Event.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, event_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % event_id)


def vote(request, event_id):
    return HttpResponse("You're voting on question %s." % event_id)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})