from django.urls import path
from .views import group_chat, post_message
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('groups/<int:group_id>/chat/', group_chat, name='group_chat'),
    path('groups/<int:group_id>/chat/post/', post_message, name='post_message'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)