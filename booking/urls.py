
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import bookfutsal_list
from .views import BookFutsal
from .views import*
from .views import  UserDashboard

urlpatterns = [

# CRUD for blog
    path('adminblogs/', views.blogs_list, name='blogs_list'),
    path('blogscreate/', views.blogs_create, name='blogs_create'),
    path('blogs/<int:pk>/edit/', views.blogs_edit, name='blogs_edit'),
    path('blogs/<int:pk>/delete/', views.blogs_delete, name='blogs_delete'),

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

# CRUD operations for reviewing team 
    path('adminreview/', views.adminreview_list, name='review_list'),
    path('reviewcreate/', views.review_create, name='review_create'),
    path('review/<int:pk>/edit/', views.review_edit, name='review_edit'),
    path('review/<int:pk>/delete/', views.review_delete, name='review_delete'),

# CRUD operations  for chat Message
    path('adminchatMessage/', views.adminchatMessage_list, name='chatMessage_list'),
    path('chatMessagecreate/', views.chatMessage_create, name='chatMessage_create'),
    path('chatMessage/<int:pk>/edit/', views.chatMessage_edit, name='chatMessage_edit'),
    path('chatMessage/<int:pk>/delete/', views.chatMessage_delete, name='chatMessage_delete'),

# CRUD operations for slider team list
    path('adminslider/', views.slider_list, name='slider_list'),
    path('slidercreate/', views.Slider_create, name='slider_create'),
    path('slider/<int:pk>/edit/', views.Slider_edit, name='slider_edit'),
    path('slider/<int:pk>/delete/', views.Slider_delete, name='slider_delete'),

# path('adminmatch/', views.match, name='adminmatch'),
    path('adminteam/', views.team, name='adminteam'),

  path('create-match/', views.create_match, name='create_match'),
    path('create-team/', views.create_team, name='create_team'),

    path('recommendation/', views.futsal_recommendation, name='futsal_recommendation'),
    path('location/', views.get_user_location, name='get_location'),
 
    path('booking/<int:booking_id>/download/', views.download_booking_info, name='download_booking_info'),
    path('booking/download/', views.download_booking_info, name='download_booking_info_no_id'),

## for user dashboard 

    path('UserDashboard', UserDashboard, name='UserDashboard'),
    
#book_futsal booking futsal 
    path('book_futsal/', views.BookFutsal.as_view(), name='book_futsal'),

    
    path('futsal/', views.futsal_list, name='futsal'),
    path('futsal/<int:pk>/', views.futsal_details, name='futsal_detail'),

    path('chatd/', views.chat_list, name='chat'),
    
    path('futsal/', views.futsal_details, name='futsal_detail'), 

    path('create_team/', views.CreateTeam.as_view(), name='create_team'),
    path('edit_team/<int:id>/', views.EditTeam.as_view(), name='edit_team'),
    path('team_detail/<int:team_id>/', views.teamsdetailss, name='team_detail'),

### Khalti Payment 
    path("khalti-request/<int:id>/", views.KhaltiRequestView.as_view(), name="khaltirequest"),
    path("khalti-verify/", views.KhaltiVerifyView.as_view(), name="khaltiverify"),
    path("payment-success/", views.payment_success, name="payment_success"),
    path("payment_page/", views.payment_page, name="payment_page"),
   
###booking futsal 
    path('bookings/<int:futsal_id>/', bookfutsal_list, name='bookings_by_futsal'),

## notifications 
    path('notificationMessage/', views.notificationMessage_list, name='Message_list'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   