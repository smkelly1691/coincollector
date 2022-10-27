from django.contrib import admin
from .models import Coin, Appraising, Show

# Register your models here.
admin.site.register(Coin)
admin.site.register(Appraising)
admin.site.register(Show)