from django.contrib import admin

from .models import Event
from .models import Possibility
from .models import Bet


admin.site.register(Event)
admin.site.register(Possibility)
admin.site.register(Bet)
