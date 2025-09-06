from django import forms
from .models import Trips

class TripForm(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['title', 'destination', 'depature_date', 'return_date', 'budget', 'image']
