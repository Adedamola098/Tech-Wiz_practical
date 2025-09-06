from django.contrib import admin
from .models import Trips

# Register your models here.
@admin.register(Trips)
class TripAdmin(admin.ModelAdmin):
    list_display = ["title", "budget", "destination", "depature_date", "return_date"]
    search_fields = ["title", "destination", "budget"]
    list_filter = ["title", "destination"]

