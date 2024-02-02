from ast import Match
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.
from .form import *
from allauth.account.models import EmailAddress

from booking.models import Blog, Futsal, Book_futsal, Team, Testimonials, User, Review
from django.contrib.admin.views.decorators import staff_member_required
from calendar import month_name
from django.contrib.auth.decorators import login_required

@staff_member_required
def index(request):
    futsal_count = Futsal.objects.count()
    booking_count = Book_futsal.objects.count()
    user_count = User.objects.count()
    review_count = Review.objects.count()
    teams = Team.objects.count()
    match = Match.objects.count()
    blog = Blog.objects.count()
    testimonials = Testimonials.objects.count()
    futsal=Book_futsal.objects.all().order_by('-date')[:5]
    booked_futsal=Futsal.objects.all()
    book_futsal=[]
    futsaldata=[]
    
    for booking in booked_futsal:
        futsalcount=Book_futsal.objects.filter(futsal=booking).count()
        futsaldata.append(booking.name)
        book_futsal.append(futsalcount)

    print(futsaldata)
    print(book_futsal)

    context = {
        'futsal_count': futsal_count,
        'booking_count': booking_count,
        'user_count': user_count,
        'review_count': review_count,
        'teams':teams,
        'match':match,
        'blog':blog,
        'testimonials':testimonials,
        'futsals':futsal,
        'futsaldata':futsaldata,
        'book_futsal':book_futsal,
      

    }
    return render(request, 'admin/index.html', context)




# Original home view
def home(request):
    futsals = Futsal.objects.all() # Retrieve all Futsal objects
    context = {'futsals': futsals} # Create a context dictionary with 'futsals' key

    # Check if the user is authenticated
    if request.user.is_authenticated:
        team_status = Team.objects.filter(user=request.user)
    else:
        team_status = None
    context = {
    'team_status': team_status,
    'futsals': futsals,
    }
    return render(request, 'index.html', context)

#register page
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', context={'form': form})
    
#login page
def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("/")
    
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
           
            
            user = authenticate(request, username=name, password=passwd)
            
            if user is not None:
                login(request, user)
                messages.success(request, "logged in sucessfully")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("register")
        return render(request, "login.html")
    

    
#logout index
def logout_view(request):
    logout(request)
    return redirect('index')

#user portal start
def logout_view(request):
    logout(request)
    return redirect('signup')

def logout_view(request):
    logout(request)
    return redirect('/')

## Home view
def home(request):
    futsals = Futsal.objects.all()
    context = {'futsals': futsals}
    if request.user.is_authenticated:
        team_status = Team.objects.filter(user=request.user)
    else:
        team_status = None
    context = {
    'team_status': team_status,
    'futsals': futsals,
    }
    return render(request, 'index.html', context)

#redirect new home view
def home(request):
    # detail = Details.objects.all()
    # Slider = slider.objects.all()
    futsal = Futsal.objects.all()
    testimonials= Testimonials.objects.all()
    # beadcrumbs= Beadcrumbs.objects.all()
    if request.user.is_authenticated:
        team_status = Team.objects.filter(user=request.user)
    else:
        team_status = None
    context = {
        # 'detail':detail, 
        # 'Slider':Slider, 'futsal':futsal, 
        'testimonials':testimonials, 
        # 'beadcrumbs':beadcrumbs,
        'team_status': team_status,
        }
    
    return render(request, 'index.html', context)


from django.urls import reverse
# Custom login view for admin
def custom_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method == 'POST':
        print('post')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', reverse('index'))
            return redirect(next_url)
        else:
            print('Invalid credentials')
            # Add an error message to the template context
            context = {'error': 'Invalid credentials'}
            messages.error(request, 'Invalid credentials')
            return render(request, 'admin/login.html', context)
    else:
        print('hello')
        return render(request, 'admin/login.html')

#logout admin
@login_required
def custom_logout(request):
    logout(request)
    return render(request, 'admin/logout.html')


# CRUD Accounts Email Addresss for operations 
from django.shortcuts import render, get_object_or_404


def email_list(request):
    emailaddress = EmailAddress.objects.all()
    return render(request, 'admin/email/index.html', {'emailaddress': emailaddress})

def email_create(request):
    form = EmailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('email_list')
    return render(request, 'admin/email/create.html', {'form': form})

def email_edit(request, pk):
    email = EmailAddress.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmailForm(instance=email)
        form = EmailForm(request.POST, request.FILES, instance=email)
        if form.is_valid():
            form.save()
            return redirect('email_list')
    else:
        form = EmailForm(instance=email)
    return render(request, 'admin/email/edit.html', {'form': form})

def email_delete(request, pk):
    email = get_object_or_404(EmailAddress, pk=pk)
    if request.method == 'POST':
        email.delete()
        return redirect('email_list')
    return render(request, 'admin/email/delete.html', {'email': email})

# CRUD for groups lists
from django.contrib.auth.models import User, Group

def group_list(request):
    group = Group.objects.all()
    return render(request, 'admin/groups/index.html', {'group': group})

def group_create(request):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('group_list')
    return render(request, 'admin/groups/create.html', {'form': form})

def group_edit(request, pk):
    group = get_object_or_404(Group, pk=pk)
    form = GroupForm(request.POST or None, instance=group)
    if form.is_valid():
        form.save()
        return redirect('group_list')
    return render(request, 'admin/groups/edit.html', {'form': form})

def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('group_list')
    return render(request, 'admin/groups/delete.html', {'group': group})


# User lists CRUD operations 
def user_list(request):
    user = User.objects.all()
    return render(request, 'admin/users/index.html', {'user': user})

def user_create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'admin/users/create.html', {'form': form})

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'admin/users/edit.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'admin/users/delete.html', {'user': user})


# for match list of booking view admin match list 
def match_list(request):
    matches = Match.objects.all()
    return render(request, 'match_list.html', {'matches': matches})