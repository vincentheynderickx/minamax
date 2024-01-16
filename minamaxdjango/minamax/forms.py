# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, Bet


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]


class CustomLoginForm(AuthenticationForm):
    pass


class BetForm:
    class Meta:
        model = Bet
        fields = ["id", "event", "possibility", "putting", "username"]
