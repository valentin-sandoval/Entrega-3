from django.contrib import admin

from .models import Reserva, Clase

# Register your models here.

admin.site.register(Reserva)
admin.site.register(Clase)