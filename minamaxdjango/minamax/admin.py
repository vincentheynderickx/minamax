from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .models import Event
from .models import Possibility
from .models import Bet

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'points', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event)
admin.site.register(Possibility)
admin.site.register(Bet)
