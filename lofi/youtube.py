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
    if response['pageInfo']['totalResults'] == 0:
        print(response)
        print('no results')
        # TODO: what should we do in response?
        # TODO: grab the youtube suggestions, fix spelling errors and try again
        return None
    else:
        if resultNum > len(response["items"]):
            resultNum = len(response["items"])
        return response["items"][resultNum - 1]["id"]["videoId"]
