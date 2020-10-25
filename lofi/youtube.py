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
    # os.system('youtube-dl -x --audio-format wav ' + url)
    video_id = url[32:]
    def download_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting')
            # Create the new .wav filename
            audio_file = d["filename"]
            print(audio_file)
            # start = 0
            # end = 1.5 * 60 * 1000
            # wav_filename = os.path.splitext(os.path.basename(audio_file))[0] + ".wav"
            # AudioSegment.from_file(audio_file).export(out_f=wav_filename, 
            #                           format='wav')
            # # song = AudioSegment.from_file(audio_file, "m4a")[start:end]
            # # extract = song[start:end]
            # # extract.export(audio_file, format="m4a")

    ydl_opts = {
        'format': 'm4a/bestaudio',
        'outtmpl': "lofi/static/lofi/downloads/%(id)s.%(ext)s",  
        'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'wav',
        }],
        'ffmpeg_location': 'ffmpeg-f/',
        'progress_hooks': [download_hook],
        'download': False,
    }

    ydl = youtube_dl.YoutubeDL(ydl_opts)

    with ydl:
        vid_info = ydl.extract_info(url, download=False)
        # keeping copy of filname
        video_id = vid_info.get('id')
        filename = "lofi/static/lofi/downloads/" + video_id + ".wav"
        ydl.download([url])

        print('Converting to Lo-Fi')
        beat = AudioSegment.from_wav(filename)
        filtered = beat.low_pass_filter(1000)
        filtered.export(video_id + '.wav', format='wav')
        print('Done!')

