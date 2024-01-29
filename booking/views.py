

import math
from django.shortcuts import render, redirect, get_object_or_404
from groupchat.models import UserGroups

from django.views import View
import requests
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Futsal
from django.db.models import Q

# recommendation system
import requests
from math import radians, sin, cos, sqrt, atan2
from django.conf import settings

def get_user_location():
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key=REMOVED_GOOGLE_API_KEY" + settings.GOOGLE_MAPS_API_KEY
    response = requests.post(url)
    json_data = response.json()
    return json_data["location"]["lat"], json_data["location"]["lng"]

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1_r = radians(lat1)
    lon1_r = radians(lon1)
    lat2_r = radians(lat2)
    lon2_r = radians(lon2)
    dlon = lon2_r - lon1_r
    dlat = lat2_r - lat1_r
    a = sin(dlat / 2)**2 + cos(lat1_r) * cos(lat2_r) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance



def LoginView(request):
    return render(request, 'login.html')

def RegisterView(request):
    return render(request, 'register.html')

def get_recommendations():
    user_lat, user_lng = get_user_location()
    futsals = Futsal.objects.all()
    for futsal in futsals:
        futsal_lat, futsal_lng = futsal.location.split(',')
        distance = calculate_distance(float(user_lat), float(user_lng), float(futsal_lat), float(futsal_lng))
        futsal.distance = distance
    futsals = sorted(futsals, key=lambda x: x.distance)
    return futsals[:5] # Return top 5 recommended futsals

def index(request):
    futsals = Futsal.objects.all()
    context = {'futsals': futsals}
    return render(request, 'index.html', context)

def booking(request):
    return render(request, 'booking.html')

