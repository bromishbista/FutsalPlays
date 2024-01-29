from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


from booking.models import Futsal, Book_futsal, User, Review
from django.contrib.admin.views.decorators import staff_member_required
from calendar import month_name

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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', context={'form': form})

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
    