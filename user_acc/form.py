from django.contrib.auth.forms import UserCreationForm

from .models import User
from . models import *
from django import forms
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

class CustomUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter username'}))
    # futsal = forms.CharField(label='Futsal', widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter futsal'}))
    email = forms.EmailField(label='Email Address', widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailAddress
        fields = '__all__'

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
class SocialAccountForm(forms.ModelForm):
    class Meta:
        model = SocialAccount
        fields = '__all__'

class SocialAppForm(forms.ModelForm):
    class Meta:
        model = SocialApp
        fields = '__all__'

class SocialTokenForm(forms.ModelForm):
    class Meta:
        model = SocialToken
        fields = '__all__'

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'



# creating class for contact form 
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'phone', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
