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

    #register
    path('register/', authviews.register, name="register"),
    
    #index admin
    path('admin/', views.index, name='index'),
    path('admin/', admin.site.urls, name='index'),
    path('admin/', admin.site.urls, name='index'),

    #logout portal
    path('login/', authviews.loginpage, name="login"),
    path('logout/', logout_view, name="logout"),
    path('logout/', authviews.logoutpage, name="logout"),
    path('admin/logout/', custom_logout, name='custom_logout'),

    #home 
    path('', views.home, name="home"),
    path('', views.home, name="home"),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)