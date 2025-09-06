from django.db import models

# Trip model with necessary fields
class Trips(models.Model):
    title = models.CharField(max_length=100)  # Changed TextField to CharField for titles
    destination = models.CharField(max_length=200)  # Changed TextField to CharField for destinations
    depature_date = models.DateField()  # Date of departure
    return_date = models.DateField()  # Date of return
    budget = models.PositiveIntegerField(default=0)  # Trip budget
    image = models.ImageField(null=True, blank=True, upload_to="media/trip_images/")  # Store images in 'media/trip_images/'

    def __str__(self):
        return self.title  # Return the title when querying the trip
