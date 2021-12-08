from django.contrib import admin
from myevents.models import *
# Register your models here.
@admin.register(Event)
class Event(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields]