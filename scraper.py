import os
import json
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set up the YouTube Data API v3 credentials
def setup (API):
    global youtube
    DEVELOPER_KEY = API
    youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)


def getcomments(video_link):
    video_id = video_link.split("watch?v=")
    video_id=video_id[1]
    Coments=[]
    global youtube
# Define the video ID of the YouTube video you want to scrape comments from
#video Id must be a string
#amount msut be string


# Define the API request to retrieve the video's comments
    comments_request = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id,
        textFormat='plainText'
    )

    # Execute the API request and loop through each comment
    while comments_request:
        comments_response = comments_request.execute()
        for comment in comments_response['items']:
            Coments.append(comment['snippet']["topLevelComment"])
            print(comment)
            if "replies" in comment:
                Coments.extend (comment['replies']["comments"])

        
        # Check if there are more comments and, if so, continue retrieving them
        comments_request = youtube.commentThreads().list_next(
            comments_request,
            comments_response
        )
    json.dump(Coments,open(f'data/{video_id}.json','w'),indent=4)
setup("")
getcomments("https://www.youtube.com/watch?v=OU44UG4wx14")