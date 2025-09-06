from django.shortcuts import redirect, render
from .models import Trips
from .forms import TripForms
from django.contrib import messages

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
        # Log the form data to check if it's being sent correctly
        print(request.POST)

        # Using the TripForm ModelForm to handle validation and saving
        form = TripForms(request.POST)
        if form.is_valid():
            form.save()  # Save the trip to the database
            messages.success(request, "Trip created successfully!")  # Flash success message
            return redirect('trip_list')  # Redirect to the trip list
        else:
            # Log the errors if the form is invalid
            print(form.errors)

    else:
        form = TripForms()

    return render(request, 'trips/create_trip.html', {'form': form})
