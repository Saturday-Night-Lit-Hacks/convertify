from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import pydub
import requests

# Create your views here.
def index(request):
    context = {'name': 'Tanya Lai'}
    input()
    if request.method == 'POST':
        data = request.POST
        context['name'] = data.get('firstname')
        
    return render(request, 'lofi/index.html', context)

def input():
    print(settings.KEY)
    return 1



def scrape(request):
    return 1

def make_lofi(request):
    return 1

