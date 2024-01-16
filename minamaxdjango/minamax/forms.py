# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from .models import Possibility
from .models import Bet


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]


class PossibilityResultForm(forms.ModelForm):
    class Meta:
        model = Possibility
        fields = ['result']
        RESULT_CHOICES = [("Win", "Win"), ("Lose", "Lose")]
        result = forms.ChoiceField(choices=RESULT_CHOICES)

class PossibilityResultForm(forms.ModelForm):
    class Meta:
        model = Possibility
        fields = ['result']
        RESULT_CHOICES = [("Win", "Win"), ("Lose", "Lose")]
        result = forms.ChoiceField(choices=RESULT_CHOICES)

class CustomLoginForm(AuthenticationForm):
    pass


class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ["id", "event", "possibility", "putting"]
