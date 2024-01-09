from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse
from .models import Event
from .models import CustomUser
from django.template import loader
from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

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

@login_required
def profile(request):
    user = get_object_or_404(CustomUser, pk=request.user.pk)
    return render(request, "profile.html", {'user': request.user})

def custom_login(request, *args, **kwargs):
    return LoginView.as_view(template_name='login.html')(request, *args, **kwargs)