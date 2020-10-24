from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import pydub
import requests
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# Create your views here.
def index(request):
    context = {'name': 'Tanya Lai'}
    youtube(2,2)
    if request.method == 'POST':
        data = request.POST
        context['name'] = data.get('firstname')
    return render(request, 'lofi/index.html', context)

def youtube(queries, resultSize):
    # every request must specify settings.KEY
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=settings.KEY)

    request = youtube.search().list(
        part="snippet",
        maxResults=2,
        q="retrteiurtyewytueryr5o23"
    )
    response = request.execute()
    if response['pageInfo']['totalResults'] == 0:
        print('no results')
    
    print(response)
    return 1



def scrape(request):
    return 1

def make_lofi(request):
    return 1

