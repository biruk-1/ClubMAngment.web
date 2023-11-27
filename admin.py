# admin.py

from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date', 'event_location')
    search_fields = ['event_name', 'event_location']
