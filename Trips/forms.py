from django import forms
from .models import Trips

class TripForms(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ["title", "Budget", "destination", "depature_date", "return_date"]
