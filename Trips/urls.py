from django.urls import path
from . import views


urlpatterns = [    
    path('', views.Trip_list, name='trip_list'),
    path('<int:pk>/', views.trip_detail, name='trip_detail'),
    path('create/', views.create_trip, name='create_trip'), 

     
]