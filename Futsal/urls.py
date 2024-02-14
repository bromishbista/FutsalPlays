
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('user_acc.urls')),
#     path('', include('booking.urls')),
#     path('', include('allauth.urls')),
   
# ]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [
    path('', include('user_acc.urls')),
    path('', include('groupchat.urls')),
    path('', include('booking.urls')),
    path('', include('allauth.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
   
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)