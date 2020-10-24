from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('request', views.request_lofi, name='request_lofi')
]
