from django.contrib.auth.forms import UserCreationForm

from .models import User
from .models import *
from django import forms
from allauth.account.models import EmailAddress

from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

class CustomUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter username'}))
    futsal = forms.CharField(label='Futsal', widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter futsal'}))
    email = forms.EmailField(label='Email Address', widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['username', 'futsal', 'email', 'password1', 'password2']