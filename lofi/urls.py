from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('request', views.request_lofi, name='request_lofi'),
    path('playback/<int:video_id>', views.playback, name='playback'),
]
