from tkinter import NO
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import  auth
from user_acc.form import CustomUserForm

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully!! Login to continues")
            return redirect('/login')
    context = {'form':form}
    return render(request, "register.html", context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("/")
   
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            print(request.POST)
            
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "logged in successfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("/login")
        return render(request, "login.html")


def logoutpage(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, "Logged out Sucessfully")
    return redirect("/")