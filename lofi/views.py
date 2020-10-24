from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import RequestMusicForm
from .models import UserInput
import pydub
import requests
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
base_url = "https://www.youtube.com/watch?v="

# Create your views here.
def index(request):
    context = {'name': 'Tanya Lai'}
    if request.method == 'POST':
        data = request.POST
        context['name'] = data.get('firstname')
    return render(request, 'lofi/index.html', context)

def youtube(queries, resultNum):
    # every request must specify settings.KEY
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=settings.KEY)
    
    # if person has typos, then use the suggested search requests for

    request = youtube.search().list(
        part="snippet",
        maxResults=10,
        q=queries,
    )
    response = request.execute()
    if response['pageInfo']['totalResults'] == 0:
        print(response)
        print('no results')
        return None
    else:
        if resultNum > len(response["items"]):
            resultNum = len(response["items"])
        return response["items"][resultNum - 1]["id"]["videoId"]

def scrape(request):
    return 1

def make_lofi(request):
    return 1


def request_lofi(request):
    if request.method == 'POST':
        form = RequestMusicForm(request.POST)
        if form.is_valid():
            article_url = form.cleaned_data['article_url']
            text = form.cleaned_data['text']
            freq_num = form.cleaned_data['freq_num']
            rand_video = form.cleaned_data['rand_video']
            has_url = False

            # checks to see if any blanks
            if not article_url:
                has_url = True

            if freq_num < 1 and freq_num > 9:
                freq_num = 3

            # TODO: call a function in our transformation file

            UserInput.objects.create(article_url=article_url, has_url=has_url, text="Done", freq_num=freq_num,
                                     rand_video=rand_video)

            # TODO: return to somewhere else
            videoId = youtube(text, freq_num)
            video = ""
            if videoId is not None:
                video = base_url + youtube(text, freq_num)
                print(video)
            else:
                print("problem")
    else:
        form = RequestMusicForm()
    # TODO: add HTML file
    return render(request, 'lofi/request_lofi.html', {
        'form': form
    })
