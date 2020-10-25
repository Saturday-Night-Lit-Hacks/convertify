from django.conf import settings
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import random
import requests
import os
import youtube_dl
from pydub import AudioSegment
import subprocess
from pydub.playback import play
import math
from honeycomb.settings import BASE_DIR
import os


def youtube(queries, resultNum, rand):
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

    # support for randomized case
    if rand:
        resultNum = random.randint(1, 9)

    response = request.execute()
    videos = [result["id"]["videoId"] for result in response["items"] if result["id"].get("videoId") is not None]
    if len(videos) == 0:
        print('no results')
        return None
    else:
        if resultNum > len(videos):
            resultNum = len(videos)
        return videos[resultNum - 1]

def youtubedl(url):
    video_id = url[32:]
    def download_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting')
            # Create the new .wav filename
            audio_file = d["filename"]

    ydl_opts = {
        'format': 'm4a/bestaudio',
        'outtmpl': "lofi/static/lofi/downloads/%(id)s.%(ext)s",  
        'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'wav',
        }],
        'ffmpeg_location': os.path.join(BASE_DIR, 'ffmpeg_stuff'),
        'progress_hooks': [download_hook],
        'download': False,
    }

    ydl = youtube_dl.YoutubeDL(ydl_opts)

    with ydl:
        vid_info = ydl.extract_info(url, download=False)
        # keeping copy of filname
        video_id = vid_info.get('id')
        filename = "lofi/static/lofi/downloads/" + video_id + ".wav"

        duration = vid_info.get('duration')
        start = (duration * 1000) - (1.5 * 60 * 1000)
        end = duration * 1000
        ydl.download([url])

        print('Converting to Lo-Fi')
        beat = AudioSegment.from_wav(filename)[start:end] + 15
        reverser = beat.low_pass_filter(500)
        reverser = reverser.high_pass_filter(4500)
        print("low passed")
        # pick random number [1, 14]
        resultNum = random.randint(1, 14)
        drums = AudioSegment.from_wav('beat'+ str(resultNum) +'.wav')
        print(len(drums))
        print(len(beat))
        bop = drums
        loop_times = 1
        if len(beat) > len(drums):
            loop_times = math.ceil(len(beat) / (len(drums)))
            for x in range(0, loop_times):
                bop = bop + drums
        print(loop_times)
        print(len(bop))
        bop = bop - 15
        # how to get length of drums, then loop that many times
        reverser = bop.overlay(reverser)
        # mono
        print("overlayed")
        # print("high passed")
        reverser = reverser.fade_in(3000).fade_out(3000)
        print("faded")

        # chunk = duration / 10.0 * 1000
        # chunked = []
        # chunkStart = 0
        # chunkEnd = chunkStart + chunk
        # for i in range(0,10):
        #     chunked.append(reverser[chunkStart:chunkEnd])
        #     chunkStart = chunkEnd
        #     chunkEnd += chunk
        
        # # # add sound effects here!
        # newReverser = chunked[0]
        # for i in range (1,10):
        #     if i == 3:
        #         newReverser += chunked[i].invert_phase(channels=(1,1))
        #     elif i == 4  or i == 5:
        #         newReverser += chunked[i].pan(-0.45)
        #     elif i == 6  or i == 7:
        #         newReverser += chunked[i].pan(0.45)
        #     else:
        #         newReverser += chunked[i]
            

        # cut up into different segments and loop
        # used to just be reverser
        reverser.export("lofi/static/lofi/downloads/" + video_id + '.wav', format='wav')
        print('complete')
