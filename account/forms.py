from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Registration Form - Using UserCreationForm
class RegistrationForms(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Login Form - Using AuthenticationForm (No need for custom fields)
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

# Custom Registration Form - Manual User Creation
class CustomRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    # Clean Password2 to ensure passwords match
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2

    # Clean Username to ensure it's unique
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")

        return username

    # Save the new user to the database
    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']

        user = User.objects.create_user(username=username, email=email, password=password)
        return user
