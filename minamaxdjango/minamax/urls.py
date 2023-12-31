from django.urls import path
from .views import signup
from . import views
from django.contrib.auth.views import LoginView
from .views import custom_login

app_name = "minamax"
urlpatterns = [
    path("", views.index, name="index"),
    path('signup/', signup, name='signup'),
    path("profile/", views.profile, name="profile"),
    path('login/', custom_login, name='login'),
    path('logout/', LoginView.as_view(), name='logout'),
    path("<int:event_id>/", views.detail, name="detail"),
    path("<int:event_id>/results/", views.results, name="results"),
]