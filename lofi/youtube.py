from django.conf import settings
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import random

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
