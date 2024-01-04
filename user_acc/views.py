from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


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
    