from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from .models import Possibility
from .models import CustomUser
from .models import Event
from .models import Bet
from django.template import loader
from .forms import CustomUserCreationForm, BetForm
from .forms import CustomUserCreationForm
from .forms import PossibilityResultForm
from django.contrib.auth.views import LoginView


def index(request):
    latest_event_list = Event.objects.order_by("-pub_date")[:5]
    context = {"latest_event_list": latest_event_list}
    return render(request, "minamax/index.html", context)


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    possibilities_list = Possibility.objects.filter(event=event)
    context = {"possibilities_list": possibilities_list, "event": event}
    return render(request, "minamax/detail.html", context)


def results(request, event_id):
    response = "You're looking at the results of event %s."
    return HttpResponse(response % event_id)


def vote(request, event_id):
    return HttpResponse("You're voting on question %s." % event_id)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("minamax:index")
    else:
        form = CustomUserCreationForm()
    return render(request, "minamax/signup.html", {"form": form})


@login_required
def profile(request):
    user = get_object_or_404(CustomUser, pk=request.user.pk)
    return render(request, "minamax/profile.html", {"user": request.user})


def custom_login(request, *args, **kwargs):
    return LoginView.as_view(template_name='minamax/login.html')(request, *args, **kwargs)

@user_passes_test(lambda u: u.is_staff)
def change_result(request, possibility_id):
    possibility = get_object_or_404(Possibility, pk=possibility_id)
    if possibility.result != "Pending":
        raise Http404("Result is not pending")
    if request.method == 'POST':
        form = PossibilityResultForm(request.POST, instance=possibility)
        if form.is_valid():
            if possibility.result == "Win":
                bets = Bet.objects.filter(possibility=possibility)
                for bet in bets:
                    user = bet.username
                    user.points += possibility.quotation * bet.putting
                    user.save()
            form.save()
    else:
        form = PossibilityResultForm(instance=possibility)

    return render(request, "minamax/change_result.html", {"form": form, "possibility": possibility, "possibility_id": possibility.id})
    return LoginView.as_view(template_name="minamax/login.html")(
        request, *args, **kwargs
    )


@login_required
def to_bet(request):
    if request.method == "POST":
        form = BetForm(request.POST)
        if form.is_valid():
            bet = form.save(commit=False)
            bet.username = request.user
            user = bet.username
            user.points += -bet.putting
            bet.save()
            user.save()
            return redirect("../")
    else:
        form = BetForm()

    return render(request, "minamax/to_bet.html", {"form": form})
