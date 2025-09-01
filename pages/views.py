from django.shortcuts import render

# Create your views here.
def home(requests):
<<<<<<< HEAD
    return render(requests, 'pages/Home.html')

def about(requests):
    return render(requests, 'pages/About.html')

def Contact(requests):
    return render(requests, 'pages/Contact.html')
=======
    return render(requests, 'pages/home.html')
   
>>>>>>> 4ef053d5deb0f34dc12aff003d38d0b86cff1c37
