from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests, 'pages/Home.html')

def about(requests):
    return render(requests, 'pages/About.html')

def Contact(requests):
    return render(requests, 'pages/Contact.html')