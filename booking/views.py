
from datetime import timezone
import datetime
from http.client import PAYMENT_REQUIRED
import math
from django.shortcuts import render, redirect, get_object_or_404

from groupchat.models import UserGroups
from . form import *
from django.views import View
import requests
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Futsal
from django.db.models import Q
from django.shortcuts import render


# recommendation system
import requests
from math import radians, sin, cos, sqrt, atan2
from django.conf import settings

from .models import Futsal
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


# CRUD Operations for Breadcrumbs 

def beadcrumbs_list(request):
    beadcrumbs = Beadcrumbs.objects.all()
    return render(request, 'admin/booking/beadcrumbs/index.html', {'beadcrumbs': beadcrumbs})

def beadcrumbs_create(request):
    form = BeadcrumbsForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('beadcrumbs_list')
    return render(request, 'admin/booking/beadcrumbs/create.html', {'form': form})

def beadcrumbs_edit(request, pk):
    beadcrumbs = Beadcrumbs.objects.get(pk=pk)
    if request.method == 'POST':
        form = BeadcrumbsForm(instance=beadcrumbs)
        form = BeadcrumbsForm(request.POST, request.FILES, instance=beadcrumbs)
        if form.is_valid():
            form.save()
            return redirect('beadcrumbs_list')
    else:
        form = BeadcrumbsForm(instance=beadcrumbs)
    return render(request, 'admin/booking/beadcrumbs/update.html', {'form': form})

def beadcrumbs_delete(request, pk):
    beadcrumbs = get_object_or_404(Beadcrumbs, pk=pk)
    if request.method == 'POST':
        Beadcrumbs.delete()
        return redirect('beadcrumbs_list')
    return render(request, 'admin/booking/beadcrumbs/delete.html', {'beadcrumbs': beadcrumbs})



# CRUD operations for About start
def about_list(request):
    about = About.objects.all()
    return render(request, 'admin/booking/about/index.html', {'about': about})

def about_create(request):
    form = AboutForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('about_list')
    return render(request, 'admin/booking/about/create.html', {'form': form})

def about_edit(request, pk):
    about = About.objects.get(pk=pk)
    if request.method == 'POST':
        form = AboutForm(instance=about)
        form = AboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('about_list')
    else:
        form = AboutForm(instance=about)
    return render(request, 'admin/booking/about/update.html', {'form': form})

def about_delete(request, pk):
    about = get_object_or_404(About, pk=pk)
    if request.method == 'POST':
        about.delete()
        return redirect('about_list')
    return render(request, 'admin/booking/about/delete.html', {'about': about})


# CRUD operations for book futsal list 
def bookfutsal_list(request):
    bookfutsal = Book_futsal.objects.all()
    return render(request, 'admin/booking/bookfutsal/index.html', {'bookfutsal': bookfutsal})

def bookfutsal_create(request):
    form = BookFutsalForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('bookfutsal_list')
    return render(request, 'admin/booking/bookfutsal/create.html', {'form': form})

def bookfutsal_edit(request, pk):
    bookfutsal = Book_futsal.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookFutsalForm(instance=bookfutsal)
        form = BookFutsalForm(request.POST, request.FILES, instance=bookfutsal)
        if form.is_valid():
            form.save()
            return redirect('bookfutsal_list')
    else:
        form = BookFutsalForm(instance=bookfutsal)
    return render(request, 'admin/booking/bookfutsal/update.html', {'form': form})


def bookfutsal_delete(request, pk):
    bookfutsal = get_object_or_404(Book_futsal, pk=pk)
    if request.method == 'POST':
        bookfutsal.delete()
        return redirect('bookfutsal_list')
    return render(request, 'admin/booking/bookfutsal/delete.html', {'bookfutsal': bookfutsal})


#CRUD operations for  futsal start
def adminfutsal_list(request):
    futsal = Futsal.objects.all()
    return render(request, 'admin/booking/futsal/index.html', {'futsal': futsal})

def futsal_create(request):
    if request.method == 'POST':
        futsal = Futsal()
        futsal.name = request.POST['name']
        futsal.location = request.POST['location']
        futsal.owner = request.POST['owner']
        futsal.image = request.FILES.get('image')
        futsal.description = request.POST['description']
        futsal.price = request.POST['price']
        futsal.latitude = request.POST.get('latitude')
        futsal.longitude = request.POST.get('longitude')
        futsal.save()
        return redirect('futsal_list')
    else:
        return render(request, 'admin/booking/futsal/create.html')
    
def futsal_edit(request, pk):
    futsal = Futsal.objects.get(pk=pk)
    if request.method == 'POST':
        form = FutsalForm(instance=Futsal)
        form = FutsalForm(request.POST, request.FILES, instance=futsal)
        if form.is_valid():
            form.save()
            return redirect('futsal_list')
    else:
        form = FutsalForm(instance=futsal)
    return render(request, 'admin/booking/futsal/update.html', {'form': form})

def futsal_delete(request, pk):
    futsal = get_object_or_404(Futsal, pk=pk)
    if request.method == 'POST':
        futsal.delete()
        return redirect('futsal_list')
    return render(request, 'admin/booking/futsal/delete.html', {'futsal': futsal})


#CRUD for operations  details infromation of futsal start
def details_list(request):
    details = Details.objects.all()
    return render(request, 'admin/booking/details/index.html', {'details': details})

def details_create(request):
    form = DetailsForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('details_list')
    return render(request, 'admin/booking/details/create.html', {'form': form})

def details_edit(request, pk):
    details = Details.objects.get(pk=pk)
    if request.method == 'POST':
        form = DetailsForm(instance=details)
        form = DetailsForm(request.POST, request.FILES, instance=details)
        if form.is_valid():
            form.save()
            return redirect('details_list')
    else:
        form = DetailsForm(instance=details)
    return render(request, 'admin/booking/details/update.html', {'form': form})



def details_delete(request, pk):
    details = get_object_or_404(Details, pk=pk)
    if request.method == 'POST':
        details.delete()
        return redirect('details_list')
    return render(request, 'admin/booking/details/delete.html', {'details': details})

# CRUD operations for admin match start
def adminmatch_list(request):
    match = Match.objects.all()
    return render(request, 'admin/booking/match/index.html', {'match': match})

def adminmatch_create(request):
    form = MatchForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('adminmatch_list')
    return render(request, 'admin/booking/match/create.html', {'form': form})

def adminmatch_edit(request, pk):
    match = get_object_or_404(Match, pk=pk)
    form = MatchForm(request.POST, request.FILES or None, instance=match)
    if form.is_valid():
        form.save()
        return redirect('adminmatch_list')
    return render(request, 'admin/booking/match/update.html', {'form': form})

def adminmatch_delete(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        match.delete()
        return redirect('adminmatch_list')
    return render(request, 'admin/booking/match/delete.html', {'match': match})

# CRUD operation for list of team 
def team_list(request):
    team = Team.objects.all()
    return render(request, 'admin/booking/team/index.html', {'team': team})

def team_create(request):
    form = TeamForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('team_list')
    return render(request, 'admin/booking/team/create.html', {'form': form})

def team_edit(request, pk):
    team = get_object_or_404(Team, pk=pk)
    form = TeamForm(request.POST, request.FILES or None, instance=team)
    if form.is_valid():
        form.save()
        return redirect('team_list')
    return render(request, 'admin/booking/team/update.html', {'form': form})

def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'admin/booking/team/delete.html', {'team': team})


# CRUD operation for  review 
def adminreview_list(request):
    review = Review.objects.all()
    return render(request, 'admin/booking/review/index.html', {'review': review})

def review_create(request):
    if request.method == 'POST':
        review = Review()
        review.user = request.POST['user']
        review.futsal = request.POST['futsal']
        review.text = request.POST['text']
        review.rating = request.POST['rating']
        review.created_at = request.POST['created_at']
        review.save()
        return redirect('review_list')
    else:
        return render(request, 'admin/booking/review/create.html')

def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)
    form = ReviewForm(request.POST, request.FILES or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('review_list')
    return render(request, 'admin/booking/review/update.html', {'form': form})

def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('review_list')
    return render(request, 'admin/booking/review/delete.html', {'review': review})

# CRUD operations for creating chatMessage 
def adminchatMessage_list(request):
    chatMessage = ChatMessage.objects.all()
    return render(request, 'admin/booking/chatMessage/index.html', {'chatMessage': chatMessage})

def chatMessage_create(request):
    if request.method == 'POST':
        chatMessage = ChatMessage()
        chatMessage.user = request.POST['user']
        chatMessage.futsal = request.POST['futsal']
        chatMessage.message = request.POST['message']
        chatMessage.timestamp = request.POST['timestamp']
        chatMessage.save()
        return redirect('chatMessage_list')
    else:
        return render(request, 'admin/booking/chatMessage/create.html')

def chatMessage_edit(request, pk):
    chatMessage = get_object_or_404(ChatMessage, pk=pk)
    form = ChatMessageForm(request.POST, request.FILES or None, instance=chatMessage)
    if form.is_valid():
        form.save()
        return redirect('chatMessage_list')
    return render(request, 'admin/booking/chatMessage/update.html', {'form': form})

def chatMessage_delete(request, pk):
    chatMessage = get_object_or_404(ChatMessage, pk=pk)
    if request.method == 'POST':
        ChatMessage.delete()
        return redirect('chatMessage_list')
    return render(request, 'admin/booking/chatMessage/delete.html', {'chatMessage': chatMessage})

def match(request):
    if request.user.is_authenticated:
        team_status = Team.objects.filter(user=request.user)
    else:
        team_status= None

    match = Match.objects.all() 
    context = {'match':match,
            'team_status': team_status,
               }
    return render(request, 'matches.html', context)

#CRUD operation for  slider team list
def slider_list(request):
    Slider = slider.objects.all()
    return render(request, 'admin/booking/Slider/index.html', {'Slider': Slider})

def Slider_create(request):
    form = SliderForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('slider_list')
    return render(request, 'admin/booking/Slider/create.html', {'form': form})


def Slider_edit(request, pk):
    Slider = slider.objects.get(pk=pk)
    if request.method == 'POST':
        form = SliderForm(instance=Slider)
        form = SliderForm(request.POST, request.FILES, instance=Slider)
        if form.is_valid():
            form.save()
            return redirect('slider_list')
    else:
        form = SliderForm(instance=Slider)
    return render(request, 'admin/booking/Slider/update.html', {'form': form})


def Slider_delete(request, pk):
    Slider = get_object_or_404(slider, pk=pk)
    if request.method == 'POST':
        Slider.delete()
        return redirect('slider_list')
    return render(request, 'admin/booking/Slider/delete.html', {'Slider': Slider})


from django.contrib import messages

# CRUD operation for booking  Futsal 

class BookFutsal(View):
    def get(self, request):
        if request.user.is_authenticated:
            team_status = Team.objects.filter(user=request.user)
        else:
            team_status = None
        context = {
            'form': BookFutsalForm(),
            'team_status': team_status
        }
        return render(request, 'booking.html', context)

    def post(self, request):
        form = BookFutsalForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            book_id = instance.id
            return redirect("/khalti-request/" + str(book_id))
        else:
            # Display validation errors as messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
        return redirect('/book_futsal/')