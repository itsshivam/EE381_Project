from __future__ import unicode_literals
from django.contrib import admin
from .models import data

class data_admin(admin.ModelAdmin):
    list_display = ["username", "speed", "acceleration", "direction", "distance", "date", "timestamp"]
    list_display_links = ["username"]
    list_filter = ["username"]
    search_fields = ["username"]
    class Meta:
        model = data

admin.site.register(data, data_admin)
