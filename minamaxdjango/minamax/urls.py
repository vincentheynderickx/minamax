from django.urls import path
from .views import signup
from . import views

urlpatterns = [
    path("", views.index, name="index"),path('signup/', signup, name='signup'),
]