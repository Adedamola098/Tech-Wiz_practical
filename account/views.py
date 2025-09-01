from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForms, LoginForm, CustomRegistrationForm

# Registration view using CustomRegistrationForm
def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():  
            user = form.save()  
            login(request, user)  
            return redirect('dashboard')  
        else:
            return render(request, 'account/register.html', {'form': form})
    else:
        form = CustomRegistrationForm()  # Create a new blank form for GET request

    return render(request, 'account/register.html', {'form': form})  # Render the registration form


# Login view using LoginForm
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():  # Validate the form before accessing cleaned_data
            username = form.cleaned_data['username']  # Safe to access cleaned_data here
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:  # If the user exists, log them in
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard if login is successful
            else:
                form.add_error(None, 'Invalid username or password.')  # Add error if authentication fails
        else:
            form.add_error(None, 'Form is invalid, please check your inputs.')  # Handle invalid form case
    else:
        form = LoginForm()  # Create a blank form for GET request

    return render(request, 'account/login.html', {'form': form})  # Render the login form


# Logout view
def user_logout(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to the login page after logging out


# Dashboard view
def dashboard(request):
    return render(request, 'account/dashboard.html')  # Ensure this template exists and renders a dashboard
