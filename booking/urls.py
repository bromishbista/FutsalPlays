
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views





urlpatterns = [
    # path('login/', LoginView, name='login'),
    # path('register/', RegisterView, name='register'),
    
    # path('index/', index, name='index'),
    # path('booking/', booking, name='booking'),
 

    # path('futsal/', views.futsal_list, name='futsal'),
    # path('futsal/<int:pk>/', views.futsal_details, name='futsal_detail'),

# CRUD for breadcrumbs operations 
    path('adminbeadcrumbs/', views.beadcrumbs_list, name='beadcrumbs_list'),
    path('beadcrumbscreate/', views.beadcrumbs_create, name='beadcrumbs_create'),
    path('beadcrumbs/<int:pk>/edit/', views.beadcrumbs_edit, name='beadcrumbs_edit'),
    path('beadcrumbs/<int:pk>/delete/', views.beadcrumbs_delete, name='beadcrumbs_delete'),

# CRUD for about start
    path('adminabout/', views.about_list, name='about_list'),
    path('aboutcreate/', views.about_create, name='about_create'),
    path('about/<int:pk>/edit/', views.about_edit, name='about_edit'),
    path('about/<int:pk>/delete/', views.about_delete, name='about_delete'),

# CRUD for bookfutsal    
    path('adminbookfutsal/', views.bookfutsal_list, name='bookfutsal_list'),
    path('bookfutsalcreate/', views.bookfutsal_create, name='bookfutsal_create'),
    path('bookfutsal/<int:pk>/edit/', views.bookfutsal_edit, name='bookfutsal_edit'),
    path('bookfutsal/<int:pk>/delete/', views.bookfutsal_delete, name='bookfutsal_delete'),


# CRUD for Futsal lists   
    path('adminfutsal/', views.adminfutsal_list, name='futsal_list'),
    path('futsalcreate/', views.futsal_create, name='futsal_create'),
    path('futsal/<int:pk>/edit/', views.futsal_edit, name='futsal_edit'),
    path('futsal/<int:pk>/delete/', views.futsal_delete, name='futsal_delete'),
    
# CRUD for Details lists for futsal   
    path('admindetails/', views.details_list, name='details_list'),
    path('detailscreate/', views.details_create, name='details_create'),
    path('details/<int:pk>/edit/', views.details_edit, name='details_edit'),
    path('details/<int:pk>/delete/', views.details_delete, name='details_delete'),

# CRUD for creating admin Match list
    path('adminmatch/', views.adminmatch_list, name='adminmatch_list'),
    path('adminmatchcreate/', views.adminmatch_create, name='adminmatch_create'),
    path('adminmatch/<int:pk>/edit/', views.adminmatch_edit, name='adminmatch_edit'),
    path('adminmatch/<int:pk>/delete/', views.adminmatch_delete, name='adminmatch_delete'),

# CRUD operations  for Team creating 
    path('adminteam/', views.team_list, name='team_list'),
    path('teamcreate/', views.team_create, name='team_create'),
    path('team/<int:pk>/edit/', views.team_edit, name='team_edit'),
    path('team/<int:pk>/delete/', views.team_delete, name='team_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)