from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RequestMusicForm
from .models import UserInput
import pydub
from .youtube import *
from .extract import *
from django.contrib import messages

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
base_url = "https://www.youtube.com/watch?v="

# Create your views here.
def index(request):
    context = {'name': 'Tanya Lai'}
    if request.method == 'POST':
        data = request.POST
        context['name'] = data.get('firstname')
    return render(request, 'lofi/index.html', context)

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
            
            if not freq_num or (freq_num < 1 and freq_num > 9):
                freq_num = 3

            # UserInput.objects.create(article_url=article_url, has_url=has_url, text="Done", freq_num=freq_num,
            # rand_video=rand_video)
            videoId = ""

            if article_url:
                videoId = article_request(article_url, freq_num, rand_video)
            elif text:
                videoId = text_request(text, freq_num, rand_video)
            else:
                messages.error(request, 'Please enter an article url or some text.')
                return render(request, "lofi/request_lofi.html", {
                    'form': form
                })

            if videoId is not None:
                video = base_url + videoId
                print(video)
            else:
                print("problem")

            # TODO: return to somewhere else
            return redirect('/playback')
    else:
        form = RequestMusicForm()
    # TODO: add HTML file
    return render(request, 'lofi/request_lofi.html', {
        'form': form
    })

def playback(request):
    return render(request, 'lofi/playback.html', {})
