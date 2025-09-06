from django.urls import path
from . import views


urlpatterns = [    
    path('', views.trip_list, name='trip'),
    path('<int:pk>/', views.trip_detail, name='trip_detail'),
    path('create/', views.create_trip, name='create_trip'),
    path('trips/<int:pk>/delete/', views.trip_delete, name='trip_delete'),
    path('trips/<int:pk>/edit/', views.trip_edit, name='trip_edit'),  # Edit trip



     
]