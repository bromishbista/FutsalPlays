
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import  *
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path




urlpatterns = [
    # path('login/', LoginView, name='login'),
    # path('register/', RegisterView, name='register'),
    
    # path('index/', index, name='index'),
    # path('booking/', booking, name='booking'),
 

    # path('futsal/', views.futsal_list, name='futsal'),
    # path('futsal/<int:pk>/', views.futsal_details, name='futsal_detail'),

]