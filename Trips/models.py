from django.db import models

# Create your models here.
class Trips(models.Model):
    title = models.TextField(max_length=100)
    destination = models.TextField(max_length=200)
    depature_date = models.DateField()
    return_date = models.DateField()
    Budget = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to="media" )
    

def __str__(self):
    return self.title