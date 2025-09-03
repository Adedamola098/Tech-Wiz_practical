from django.shortcuts import render
from .models import Trips

# Create your views here.
def Trip_list(request):
    trips = Trips.objects.all().order_by('depature_date')
    context = {
        "trips" : trips
    }
    return render(request, '')