from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Trips
from .forms import TripForm

# View for listing all trips
def trip_list(request):
    trips = Trips.objects.all().order_by('depature_date')
    context = {
        "trips": trips
    }
    return render(request, 'Trips/trip_list.html', context)

# View for displaying details of a single trip
def trip_detail(request, pk):
    trip = Trips.objects.get(pk=pk)
    context = {
        'trip': trip
    }
    return render(request, 'Trips/trip_detail.html', context)

# View for creating a new trip
def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()  # Save the trip to the database
            messages.success(request, "Trip created successfully!")  # Success message
            return redirect('trip')  # Redirect to the trip list page
        else:
            print(form.errors)  # Print any form errors to the console
    else:
        form = TripForm()

    return render(request, 'Trips/create_trip.html', {'form': form})

def trip_delete(request, pk):
    trip = get_object_or_404(Trips, pk=pk)  # Fetch the trip by its primary key
    trip.delete()  # Delete the trip from the database
    messages.success(request, "Trip deleted successfully!")  # Success message
    return redirect('trip')  # Redirect to the trip list after deletion


def trip_edit(request, pk):
    # Fetch the trip using the primary key (pk)
    trip = get_object_or_404(Trips, pk=pk)

    if request.method == 'POST':
        form = TripForm(request.POST, request.FILES, instance=trip)
        if form.is_valid():
            form.save()  # Save the updated trip details to the database
            messages.success(request, "Trip updated successfully!")  # Show a success message
            return redirect('trip_detail', pk=trip.pk)  # Redirect to the trip detail page after successful update
        else:
            # Log the form errors to the console for debugging
            print(form.errors)
    else:
        # When the form is accessed via GET request, populate it with the existing trip data
        form = TripForm(instance=trip)

    return render(request, 'Trips/edit_trip.html', {'form': form})