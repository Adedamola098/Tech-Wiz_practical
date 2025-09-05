from django.shortcuts import redirect, render
from .models import Trips
from .forms import TripForms

# Create your views here.
def Trip_list(request):
    trips = Trips.objects.all().order_by('depature_date')
    context = {
        "trips" : trips
    }
    return render(request, 'Trips/Create-Trip.html', context)

def trip_detail(request, pk):
    trips = Trips.objects.get(pk=pk)
    context = {
         'trip': trips
    }
    return render(request, 'Trips/trip_detail.html', context)

def trip(request):
    trips = Trips.objects.all().order_by('depature_date')
    context = {
         'trip': trips
    }
    return render (request, 'Trips/trips.html', context )

def create_trip(request):
    if request.method == 'POST':
        form = TripForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trip')  # Redirect to the list after creating a new trip
    else:
        form = TripForms()

    return render(request, 'Trips/create_trip.html', {'form': form})
