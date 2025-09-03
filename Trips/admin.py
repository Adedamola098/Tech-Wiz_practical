from django.contrib import admin
from .models import Trips

# Register your models here.
@admin.register(Trips)
class TripAdmin(admin.ModelAdmin):
    list_display = ["title", "Budget", "destination", "depature_date", "return_date"]
    search_fields = ["title", "destination", "Budget"]
    list_filter = ["title", "destination"]

