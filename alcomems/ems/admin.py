from django.contrib import admin

# Register your models here.

from .models import Dispatch, Vehicle

admin.site.register(Dispatch)
admin.site.register(Vehicle)
