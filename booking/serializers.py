from rest_framework import serializers
from .models import Book_futsal

from django.contrib.auth.forms import UserCreationForm

from .models import User
from .models import *
from django import forms
from .models import Futsal



class BookFutsalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_futsal
        fields = '__all__'

class FutsalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Futsal
        fields = '__all__'
