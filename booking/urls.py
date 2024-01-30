
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import  *

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('register/', RegisterView, name='register'),
    path('', index, name='index'),
    path('booking/', booking, name='booking'),

]