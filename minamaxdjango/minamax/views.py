from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from .models import Event
from .models import CustomUser
from django.template import loader
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

def index(request):
    latest_event_list = Event.objects.order_by("-pub_date")[:5]
    context = {"latest_event_list": latest_event_list}
    return render(request, "minamax/index.html", context)


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "minamax/detail.html", {"event": event})


def results(request, event_id):
    response = "You're looking at the results of event %s."
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

    return render(request, 'minamax/signup.html', {'form': form})

@login_required
def profile(request):
    user = get_object_or_404(CustomUser, pk=request.user.pk)
    return render(request, "minamax/profile.html", {'user': request.user})

def custom_login(request, *args, **kwargs):
    return LoginView.as_view(template_name='minamax/login.html')(request, *args, **kwargs)