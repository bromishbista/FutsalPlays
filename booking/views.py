
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

from django.shortcuts import render, get_object_or_404
from .models import Futsal, Book_futsal

# for userdashboard 
@login_required(login_url='login')
def UserDashboard(request):
    user_groups = UserGroups.objects.filter(members=request.user)
    futsal_bookings = Book_futsal.objects.filter(user=request.user)
    context = {'user_groups': user_groups, 'futsal_bookings': futsal_bookings}
    return render(request, 'UserDashboard.html', context)


# @login_required
# def bookedfutsal(request, futsal_id):
#     futsal = get_object_or_404(Futsal, pk=futsal_id)
#     booked_futsals = Book_futsal.objects.filter(futsal=futsal, user=request.user)
#     return render(request, 'futsal_detail.html', {'futsal': futsal, 'booked_futsals': booked_futsals})

# map Api 
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

#getting user locations

from django.shortcuts import render
from django.http import HttpResponse

def get_user_location(request):
    if request.method == 'GET':
        return render(request, 'get_location.html')
    elif request.method == 'POST':
        latitude = float(request.POST['latitude'])
        longitude = float(request.POST['longitude'])
        # TODO: Use latitude and longitude to find nearby Futsals
        return HttpResponse('Got location: {}, {}'.format(latitude, longitude))
    else:
        return HttpResponse('Method not allowed', status=405)

    
# recommending the futsal 
    
from django.shortcuts import render
from django.db.models import Q
from .models import Futsal

def futsal_recommendation(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')

    if latitude and longitude:
        futsals = Futsal.objects.filter(Q(latitude__isnull=False) & Q(longitude__isnull=False))
        for futsal in futsals:
            distance = calculate_distance(latitude, longitude, futsal.latitude, futsal.longitude)
            futsal.distance = round(distance, 2)
        futsals = sorted(futsals, key=lambda futsal: futsal.distance)
        return render(request, 'futsal_recommendation.html', {'futsals': futsals})
    else:
        return render(request, 'get_location.html')

from decimal import Decimal
from geopy.distance import geodesic

def calculate_distance(latitude1, longitude1, latitude2, longitude2):
    # Convert the latitude and longitude parameters to Decimal objects
    latitude1 = Decimal(latitude1)
    longitude1 = Decimal(longitude1)
    latitude2 = Decimal(latitude2)
    longitude2 = Decimal(longitude2)

    # Calculate the distance between the two points using the geodesic function from the geopy module
    distance = geodesic((latitude1, longitude1), (latitude2, longitude2)).km
    return distance


def deg2rad(deg):
    return deg * (math.pi/180)

# index page
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

def bookfutsal_list(request, futsal_id):
    futsal = get_object_or_404(Futsal, pk=futsal_id)
    booked_futsals = Book_futsal.objects.filter(futsal=futsal)
    return render(request, 'admin/booking/bookfutsal/index.html', {'booked_futsals': booked_futsals})


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





def notificationMessage_list(request):
    top_10_messages = ChatMessage.objects.order_by('-timestamp')[:10]
    print('hello')
    return render(request, 'notification_messages.html', {'chatMessage': top_10_messages})



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
        chatMessage.delete()
        return redirect('chatMessage_list')
    return render(request, 'admin/booking/chatMessage/delete.html', {'chatMessage': chatMessage})



# matches pages    
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



# CRUD operations for  Futsal start


def futsal_list(request):
    futsals = Futsal.objects.all()
    searchedterm=request.GET.get('futsalsearch')
    if searchedterm:
        futsals = futsals.filter(Q(name__icontains=searchedterm)|Q(price__icontains=searchedterm)|Q(location__icontains=searchedterm)).distinct()
    return render(request, 'futsal.html', {'futsals': futsals})

def chat_list(request):
    futsals = Futsal.objects.all()
    searchedterm=request.GET.get('futsalsearch')
    if searchedterm:
        futsals = futsals.filter(Q(name__icontains=searchedterm)|Q(price__icontains=searchedterm)|Q(location__icontains=searchedterm)).distinct()
    return render(request, 'chat.html', {'futsals': futsals})

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Futsal, Review, ChatMessage
from .form import ReviewForm, ChatMessageForm

@login_required
def futsal_details(request, pk):
    futsal = get_object_or_404(Futsal, pk=pk)
    reviews = Review.objects.filter(futsal=futsal)
    chat_messages = ChatMessage.objects.filter(futsal=futsal).order_by('timestamp')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.futsal = futsal
            review.user = request.user
            review.save()
            messages.success(request, 'Review added successfully.')
            return redirect('futsal_detail', pk=futsal.pk)
        else:
            chat_form = ChatMessageForm(request.user, futsal, request.POST)
            if chat_form.is_valid():
                chat_message = chat_form.save(commit=False)
                chat_message.user = request.user
                chat_message.futsal = futsal

                chat_message.save()
                return redirect('futsal_detail', pk=futsal.pk)
    else:

        form = ReviewForm()
        chat_form = ChatMessageForm(request.user, futsal)
    print(futsal)
    futsalDetail=Book_futsal.objects.filter(futsal=futsal).order_by('-date')[:5]
    
    return render(request, 'futsal_detail.html', {'futsal': futsal,'futsalDetail': futsalDetail, 'reviews': reviews, 'form': form, 'chat_messages': chat_messages, 'chat_form': chat_form,})



#CRUD for  Match end
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


# CRUD for  Team list 

def team(request):
    if request.user.is_authenticated:
        team_status = Team.objects.filter(user=request.user)
    else:
        team_status= None
    team = Team.objects.all() 
    context = {
        'teams':team,
        'team_status': team_status,
            }

    return render(request, 'teams.html', context)


def teamsdetailss(request, team_id):
    if request.user.is_authenticated:
        team_status = Team.objects.filter(user=request.user)
    else:
        team_status= None
    team = Team.objects.get(id = team_id)
    context = {
        'teams':team,
        'team_status': team_status,
            }

    return render(request, 'teams-details.html', context)



# creating class for creating team 

class CreateTeam(View):
    def get(self, request):
        if request.user.is_authenticated:
            team_status = Team.objects.filter(user=request.user)
        else:
            team_status= None
        context = {
            'form': TeamForm(),
            'team_status': team_status,
        }
        return render(request, 'create_team.html', context)
    
    def post(self, request):
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        else:
            print('error arised', form.errors)
        return redirect('team')

# creating class for editing  team 

class EditTeam(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            team_status = Team.objects.filter(user=request.user)
        else:
            team_status= None
        data = Team.objects.get(id=id)
        context = {
            'form': TeamForm(instance=data),
            'team_status': team_status,
        }
        return render(request, 'edit_team.html', context)
    
    def post(self, reqeust, id):
        data = Team.objects.get(id=id)
        form = TeamForm(reqeust.POST, reqeust.FILES, instance=data)
        if form.is_valid():
            form.save()
        return redirect('team')

#  teams details 
def team_detail(request, team_id):
    if request.user.is_authenticated:
        team_status = Team.objects.filter(user=request.user)
    else:
        team_status= None

    team = Team.objects.get(id = team_id)
    context = {
        'team': team,
        'team_status': team_status,
        }
    return render(request, 'teams-details.html', context)



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Team, Match
from .form import TeamForm, MatchForm

@login_required
def create_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST, request.FILES)
        if form.is_valid():
            match = form.save(commit=False)
            match.save()
            messages.success(request, 'Match created successfully')
            return redirect('home')
    else:
        form = MatchForm()
    return render(request, 'create_match.html', {'form': form})

@login_required
def create_team(request):
    try:
        team = request.user.team
        messages.warning(request, 'You already have a team')
        return redirect('home')
    except Team.DoesNotExist:
        if request.method == 'POST':
            form = TeamForm(request.POST, request.FILES)
            if form.is_valid():
                team = form.save(commit=False)
                team.user = request.user
                team.save()
                messages.success(request, 'Team created successfully')
                return redirect('home')
        else:
            form = TeamForm()
        return render(request, 'create_team.html', {'form': form})



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Team, Match
from .form import TeamForm, MatchForm

@login_required
def create_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST, request.FILES)
        if form.is_valid():
            match = form.save(commit=False)
            match.save()
            messages.success(request, 'Match created successfully')
            return redirect('home')
    else:
        form = MatchForm()
    return render(request, 'create_match.html', {'form': form})

@login_required
def create_team(request):
    try:
        team = request.user.team
        messages.warning(request, 'You already have a team')
        return redirect('home')
    except Team.DoesNotExist:
        if request.method == 'POST':
            form = TeamForm(request.POST, request.FILES)
            if form.is_valid():
                team = form.save(commit=False)
                team.user = request.user
                team.save()
                messages.success(request, 'Team created successfully')
                return redirect('home')
        else:
            form = TeamForm()
        return render(request, 'create_team.html', {'form': form})

from django.contrib import messages

# # CRUD operation for booking  Futsal 

# class BookFutsal(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             team_status = Team.objects.filter(user=request.user)
#         else:
#             team_status = None
#         context = {
#             'form': BookFutsalForm(),
#             'team_status': team_status
#         }
#         return render(request, 'booking.html', context)

#     def post(self, request):
#         form = BookFutsalForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.user = request.user
#             instance.save()
#             book_id = instance.id
#             return redirect('/khalti-request/' + str(book_id))
#         else:
#             # Display validation errors as messages
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f"{field}: {error}")
#         return redirect('/book_futsal/')
    





#CRUD for book Futsal start

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


# payment khalti integration 

from .models import Book_futsal

class KhaltiRequestView(View):
    def get(self, request, id):
        book_futsal = Book_futsal.objects.get(id=id)
        total_price = book_futsal.duration * book_futsal.futsal.price
        context = {
            "book_futsal": book_futsal, "total_price":total_price
        }
        return render(request, "khaltipayment.html", context)



class KhaltiVerifyView(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")
        amount = request.GET.get("amount")
        o_id = request.GET.get("order_id")
        print(token, amount, o_id)

        url = "https://khalti.com/api/v2/payment/verify/"
        payload = {
            "token": token,
            "amount": amount
        }
        headers = {
            "Authorization": "REMOVED_KHALTI_SECRET_KEY"
        }

        try:
            book_obj = Book_futsal.objects.get(id=o_id)
            response = requests.post(url, payload, headers=headers)
            resp_dict = response.json()
            if resp_dict.get("idx"):
                success = True
                book_obj.success = True
                book_obj.save()
            
            else:
                success = False
            data = {"success": success}
            return JsonResponse(data)
        except Book_futsal.DoesNotExist:
            data = {"success": False}
            return JsonResponse(data)



def payment(request):
    context = {
    }
    return render(request, 'member/payment_page.html', context)

import json
def payment_page(request):

    url = "https://a.khalti.com/api/v2/epayment/initiate/"

    return_url = request.POST.get('return_url')
    purchase_order_id = request.POST.get('purchase_order_id')
    amount = request.POST.get('amount')
    email = request.POST.get('email')
    name = request.POST.get('name')

    print("p", purchase_order_id)
    print("R", return_url)
    print("A", amount)
    print("e", email)
    print("n", name)

    payload = json.dumps({
        "return_url": return_url,
        "website_url": "http://127.0.0.1:8000",
        "amount": amount,
        "purchase_order_id": purchase_order_id,
        "purchase_order_name": "test",
        "customer_info": {
            "name": name,
            "email": email,
            "phone": "9800000001"
        }
    })
    headers = {
        'Authorization': 'key e765b891d12449ceaa4cdfd14a27e47f',
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    new_res = json.loads(response.text)
    print(new_res)
    return redirect(new_res['payment_url'])

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def payment_success(request):
    # Sending email after successful payment
    # subject = 'Booking Confirmation'
    # html_message = render_to_string('mail.html', {'username': request.user.username})
    # plain_message = strip_tags(html_message) 
    # from_email = 'bromishbista2003@gmail.com'
    # to_emails = [request.user.email]
    
    send_email(request)
    
    context = {
        'message': 'Your payment has been completed successfully. Thank you for booking!'
    }
    return render(request, 'payment_success.html', context)
# 
def send_email(request):
    html_message = render_to_string('mail.html')
    plain_message = strip_tags(html_message)
    subject = 'Booking Confirmation'
    plain_message = 'Your payment has been completed successfully. Thank you for booking!'
    from_email = 'bromishbista2003@gmail.com'
    to_email = [request.user.email]

    send_mail(subject, plain_message, from_email, to_email, html_message=html_message)
    return render(request, 'mail.html')



# def send_html_email(request):
#     subject = 'Test HTML Email'
#     html_message = render_to_string('mail.html', {'username': 'John'})
#     plain_message = 'This is a sample plain text message.'
#     from_email = 'bromishbista2003@gmail.com'
#     to_emails = ['bromishbista2003@gmail.com']

#     send_mail(subject, plain_message, from_email, to_emails, html_message=html_message)

#     return HttpResponse('Email sent successfully!')
 

##### ticket generating 
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from xhtml2pdf import pisa

def download_booking_info(request, booking_id):
    # Get the booking information based on the booking_id parameter
    booking = Book_futsal.objects.get(id=booking_id)
    
    # Generate a PDF file
    template_path = 'booking_info.html'
    context = {'booking': booking}
    html = get_template(template_path).render(context)
    pdf_file = settings.MEDIA_ROOT + f'booking_info_{booking_id}.pdf'
    with open(pdf_file, 'wb') as pdf:
        pisa.CreatePDF(html, dest=pdf)
    
    # Serve the PDF file as a download
    with open(pdf_file, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="booking_info_{booking_id}.pdf"'
        return response


#CRUD for  blogs start
def blogs_list(request):
    blogs = Blog.objects.all()
    return render(request, 'admin/booking/blogs/index.html', {'blogs': blogs})

def blogs_create(request):
    form = BlogForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('blogs_list')
    return render(request, 'admin/booking/blogs/create.html', {'form': form})


def blogs_edit(request, pk):
    blogs = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        form = BlogForm(instance=blogs)
        form = BlogForm(request.POST, request.FILES, instance=blogs)
        if form.is_valid():
            form.save()
            return redirect('blogs_list')
    else:
        form = BlogForm(instance=blogs)
    return render(request, 'admin/booking/blogs/update.html', {'form': form})


def blogs_delete(request, pk):
    blogs = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blogs.delete()
        return redirect('blogs_list')
    return render(request, 'admin/booking/blogs/delete.html', {'blogs': blogs})
