from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from  user_acc.controller import authviews
from django.contrib.auth import views as auth_views
from . import views


from django.urls import path, include



urlpatterns = [
    path('register/', authviews.register, name="register"),
    path('login/', authviews.loginpage, name="login"),
    path('logout/', authviews.logoutpage, name="logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)