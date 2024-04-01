from ast import Match
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.
from .form import *
from allauth.account.models import EmailAddress

from booking.models import Blog, Details, Futsal, Book_futsal, Team, User, Review
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
    print(futsal)

    context = {
        'futsal_count': futsal_count,
        'booking_count': booking_count,
        'user_count': user_count,
        'review_count': review_count,
        'teams':teams,
        'match':match,
        'blog':blog,
        'futsals':futsal,
        'futsaldata':futsaldata,
        'book_futsal':book_futsal,
      

    }
    return render(request, 'admin/index.html', context)

from django.urls import reverse
# Custom login view for admin
def custom_login(request):
    print('hello')
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method == 'POST':
      
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
       
        return render(request, 'admin/login.html')    

# futsal list Ajax
from django.http import JsonResponse

def fusallistAjax(request):
    futsal = Futsal.objects.filter(status=0).values_list('name', 'price', 'location', flat=True)
    futsallist = list(futsal)
    return JsonResponse(futsallist, safe=False)
from django.db.models import Q
def searchfutsal(request):
   
    searchedterm = request.GET.get('futsalsearch')
    searched = request.GET.get('futsalcost')
    print(searchedterm)
    print(searchedterm)

    
    futsaldata = Futsal.objects.filter(Q(name__icontains=searchedterm)|Q(price__icontains=searched)).distinct()
    if futsaldata:
        return redirect('futsal')
    
    else:
        messages.info(request, "No futsal matched your search")
        return redirect(request.META.get('HTTP_REFERER'))

#teams in futsal
def teams(request):
    if request.user.is_authenticated:
        team_status = Team.objects.filter(user=request.user)
    else:
        team_status = None
    context = {
    'team_status': team_status,
    }
    return render(request, 'teams.html')

def teams(request):
    detail = Details.objects.all()
    teams = Team.objects.all()
    if request.user.is_authenticated:
        team_status = Team.objects.filter(user=request.user)
    else:
        team_status = None
    context = {'detail':detail,'teams':teams, 'team_status': team_status}
    return render(request, 'teams.html', context)




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
    print(context)
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
   
    futsal = Futsal.objects.all()
    if request.user.is_authenticated:
        team_status = Team.objects.filter(user=request.user)
    else:
        team_status = None
    context = {
        'team_status': team_status,
        }
    
    return render(request, 'index.html', context)




    
    
from django.views.decorators.http import require_POST
#logout admin
@require_POST
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


# CRUD for user site lists 
def site_list(request):
    site = Site.objects.all()
    return render(request, 'admin/sites/index.html', {'site': site})

def site_create(request):
    form = SiteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('site_list')
    return render(request, 'admin/sites/create.html', {'form': form})

def site_edit(request, pk):
    site = get_object_or_404(Site, pk=pk)
    form = SiteForm(request.POST or None, instance=site)
    if form.is_valid():
        form.save()
        return redirect('site_list')
    return render(request, 'admin/sites/update.html', {'form': form})

def site_delete(request, pk):
    site = get_object_or_404(Site, pk=pk)
    if request.method == 'POST':
        site.delete()
        return redirect('site_list')
    return render(request, 'admin/sites/delete.html', {'site': site})


# CRUD operations for social account list for users 
def socialaccount_list(request):
    socialaccount = SocialAccount.objects.all()
    return render(request, 'admin/socialaccounts/socialaccounts/index.html', {'socialaccount': socialaccount})

def socialaccount_create(request):
    form = SocialAccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('socialaccount_list')
    return render(request, 'admin/socialaccounts/socialaccounts/create.html', {'form': form})

def socialaccount_edit(request, pk):
    socialaccount = get_object_or_404(SocialAccount, pk=pk)
    form = SocialAccountForm(request.POST or None, instance=socialaccount)
    if form.is_valid():
        form.save()
        return redirect('socialaccount_list')
    return render(request, 'admin/socialaccounts/socialaccounts/update.html', {'form': form})

def socialaccount_delete(request, pk):
    socialaccount = get_object_or_404(SocialAccount, pk=pk)
    if request.method == 'POST':
        socialaccount.delete()
        return redirect('socialaccount_list')
    return render(request, 'admin/socialaccounts/socialaccounts/delete.html', {'socialaccount': socialaccount})

# CRUD operations for social app
def socialapp_list(request):
    socialapp = SocialApp.objects.all()
    return render(request, 'admin/socialaccounts/socialapps/index.html', {'socialapp': socialapp})

def socialapp_create(request):
    form = SocialAppForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('socialapp_list')
    return render(request, 'admin/socialaccounts/socialapps/create.html', {'form': form})

def socialapp_edit(request, pk):
    socialapp = get_object_or_404(SocialApp, pk=pk)
    form = SocialAppForm(request.POST or None, instance=socialapp)
    if form.is_valid():
        form.save()
        return redirect('socialapp_list')
    return render(request, 'admin/socialaccounts/socialapps/update.html', {'form': form})

def socialapp_delete(request, pk):
    socialapp = get_object_or_404(SocialApp, pk=pk)
    if request.method == 'POST':
        socialapp.delete()
        return redirect('socialapp_list')
    return render(request, 'admin/socialaccounts/socialapps/delete.html', {'socialapp': socialapp})



# CRUD operations for social token list 
def socialtoken_list(request):
    socialtoken = SocialToken.objects.all()
    return render(request, 'admin/socialaccounts/socialtokens/index.html', {'socialtoken': socialtoken})

def socialtoken_create(request):
    form = SocialTokenForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('socialtoken_list')
    return render(request, 'admin/socialaccounts/socialtokens/create.html', {'form': form})

def socialtoken_edit(request, pk):
    socialtoken = get_object_or_404(SocialToken, pk=pk)
    form = SocialTokenForm(request.POST or None, instance=socialtoken)
    if form.is_valid():
        form.save()
        return redirect('socialtoken_list')
    return render(request, 'admin/socialaccounts/socialtokens/update.html', {'form': form})

def socialtoken_delete(request, pk):
    socialtoken = get_object_or_404(SocialToken, pk=pk)
    if request.method == 'POST':
        socialtoken.delete()
        return redirect('socialtoken_list')
    return render(request, 'admin/socialaccounts/socialtokens/delete.html', {'socialtoken': socialtoken})


# CRUD operations for contact list form
def contact_list(request):
    contact = Contact.objects.all()
    return render(request, 'admin/contact/index.html', {'contact': contact})

def contact_create(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact_list')
    return render(request, 'admin/contact/create.html', {'form': form})

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('contact_list')
    return render(request, 'admin/contact/edit.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'admin/contact/delete.html', {'contact': contact})


# for match list of booking view admin match list 
def match_list(request):
    matches = Match.objects.all()
    return render(request, 'match_list.html', {'matches': matches})


# views.py match list for admin
from django.shortcuts import render, redirect, get_object_or_404
from booking.models import Match
from booking.form import MatchForm

def match_list(request):
    matches = Match.objects.all()
    return render(request, 'match_list.html', {'matches': matches})

def match_detail(request, pk):
    match = get_object_or_404(Match, pk=pk)
    return render(request, 'match_detail.html', {'match': match})

def match_create(request):
    if request.method == 'POST':
        form = MatchForm(request.POST, request.FILES)
        if form.is_valid():
    
            match = form.save()
            return redirect('match_detail', pk=match.pk)
        else:
            messages.error(request, 'Please correct the form errors below.')
    else:
        form = MatchForm()
    return render(request, 'match_form.html', {'form': form})

def match_edit(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        form = MatchForm(request.POST, request.FILES, instance=match)
        if form.is_valid():
        
            match = form.save()
            return redirect('match_detail', pk=match.pk)
    else:
        form = MatchForm(instance=match)
    return render(request, 'match_form.html', {'form': form})

# ContactForm view

from django.views.generic.edit import FormView
class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
def chat(request):
    
    return render(request, 'chat.html')




# CRUD for contact
def contact_list(request):
    contact = Contact.objects.all()
    return render(request, 'admin/contact/index.html', {'contact': contact})

def contact_create(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact_list')
    return render(request, 'admin/contact/create.html', {'form': form})

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('contact_list')
    return render(request, 'admin/contact/edit.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'admin/contact/delete.html', {'contact': contact})


def blogs(request):
    blogs = Blog.objects.order_by('-created_at')
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs.html', context)

def blog_detail(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    context = {
        'blog': blog
    }
    return render(request, 'blog_detail.html', context)
    