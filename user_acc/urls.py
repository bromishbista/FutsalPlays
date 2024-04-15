from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from  user_acc.controller import authviews
from django.contrib.auth import views as auth_views
from .views import custom_login, custom_logout
from . import views
from .views import ContactFormView
from django.urls import path, include

urlpatterns = [

# contact page 
    path('contact/', ContactFormView.as_view(), name='contact'),
#login
    path('admin/login/?next=/admin/', custom_login, name='custom_login'),
    
    path('login/', authviews.loginpage, name="login"),

#register
    path('register/', authviews.register, name="register"),
    
#index admin
    path('admin/', views.index, name='index'),
    path('admin/', admin.site.urls, name='index'),
   
#logout portal
    # path('logout/', logout_view, name="logout"),
    path('logout/', authviews.logoutpage, name="logout"),
    path('admin/logout/', custom_logout, name='custom_logout'),
    
#home 
    path('', views.home, name="home"),
    path('', views.home, name="home"),

# auth views urls
    path('register/', authviews.register, name="register"),
    path('login/', authviews.loginpage, name="login"),
    path('logout/', authviews.logoutpage, name="logout"),
    
#password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),

    
# crud email address operations 
    path('adminmail/', views.email_list, name='email_list'),
    path('create/', views.email_create, name='email_create'),
    path('<int:pk>/edit/', views.email_edit, name='email_edit'),
    path('<int:pk>/delete/', views.email_delete, name='email_delete'),
    
# crud group_lists
    path('admingroup/', views.group_list, name='group_list'),
    path('groupcreate/', views.group_create, name='group_create'),
    path('group/<int:pk>/edit/', views.group_edit, name='group_edit'),
    path('group/<int:pk>/delete/', views.group_delete, name='group_delete'),

# CRUD user lists 
    path('adminuser/', views.user_list, name='user_list'),
    path('usercreate/', views.user_create, name='user_create'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('user/<int:pk>/delete/', views.user_delete, name='user_delete'),

# match list path for booking
    path('match/', views.match_list, name='match_list'),

# crud site lists for user
    path('adminsite/', views.site_list, name='site_list'),
    path('sitecreate/', views.site_create, name='site_create'),
    path('site/<int:pk>/edit/', views.site_edit, name='site_edit'),
    path('site/<int:pk>/delete/', views.site_delete, name='site_delete'),

# crud fror social accounts
    path('adminsocialaccount/', views.socialaccount_list, name='socialaccount_list'),
    path('socialaccountcreate/', views.socialaccount_create, name='socialaccount_create'),
    path('socialaccount/<int:pk>/edit/', views.socialaccount_edit, name='socialaccount_edit'),
    path('socialaccount/<int:pk>/delete/', views.socialaccount_delete, name='socialaccount_delete'),
    
# crud for  social app
    path('adminsocialapp/', views.socialapp_list, name='socialapp_list'),
    path('socialappcreate/', views.socialapp_create, name='socialapp_create'),
    path('socialapp/<int:pk>/edit/', views.socialapp_edit, name='socialapp_edit'),
    path('socialapp/<int:pk>/delete/', views.socialapp_delete, name='socialapp_delete'),

 # crud fro social token lists 
    path('adminsocialtoken/', views.socialtoken_list, name='socialtoken_list'),
    path('socialtokencreate/', views.socialtoken_create, name='socialtoken_create'),
    path('socialtoken/<int:pk>/edit/', views.socialtoken_edit, name='socialtoken_edit'),
    path('socialtoken/<int:pk>/delete/', views.socialtoken_delete, name='socialtoken_delete'),

# CRUD for Contact
    path('admincontact/', views.contact_list, name='contact_list'),
    path('contactcreate/', views.contact_create, name='contact_create'),
    path('contact/<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('contact/<int:pk>/delete/', views.contact_delete, name='contact_delete'),
        
    ## for match create
    path('match/', views.match_list, name='match_list'),
    path('<int:pk>/', views.match_detail, name='match_detail'),
    
    path('new/', views.match_create, name='match_create'),
    path('<int:pk>/edit/', views.match_edit, name='match_edit'),

    path('search-list', views.fusallistAjax),
    path('searchfutsal', views.searchfutsal, name="searchfutsal"),
   

    path('teams/', views.teams, name="teams"),
    path('team/', views.teams, name="team"),
    path('chat/', views.chat, name="chat"),

    path('blogs/', views.blogs, name="blogs"),
    path('blog-detail/<str:blog_slug>', views.blog_detail, name="blog-detail"),

  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)