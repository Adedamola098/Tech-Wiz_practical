from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class RegistrationForms(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
        
class LoginForm(AuthenticationForm):
    user = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)