from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from  user_acc.controller import authviews
from django.contrib.auth import views as auth_views
from .views import loginpage as custom_login, custom_logout
from . import views
from .views import loginpage, logout_view 
# from .views import custom_login


from django.urls import path, include



urlpatterns = [
    
#login
    path('admin/login/?next=/admin/', custom_login, name='custom_login'),
    path('login/', authviews.loginpage, name="login"),

#register
    path('register/', authviews.register, name="register"),
    
#index admin
    path('admin/', views.index, name='index'),
    path('admin/', admin.site.urls, name='index'),
   
#logout portal
    path('logout/', logout_view, name="logout"),
    path('logout/', authviews.logoutpage, name="logout"),
    path('admin/logout/', custom_logout, name='custom_logout'),
    
#home 
    path('', views.home, name="home"),
    path('', views.home, name="home"),
    
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

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)