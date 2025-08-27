from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForms
from .forms import LoginForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else :
            form = RegistrationForms()
            
    return render(request, 'account/Register.html')
            
            
            
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None :
                login(request, user)
                return redirect('dashboard'),
            else :
                form.add_error(None, 'Invalid username or password. ')
    else :
        form = LoginForm()            
        
    return render(request, 'account/login.html', {form : form})

def user_logout(request):
    logout(request)
    return redirect ('login')


