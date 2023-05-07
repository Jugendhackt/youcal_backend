import os
import json
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)

def getcomments(video_link):
    video_id = video_link.split("watch?v=")
    video_id=video_id[1]
    Coments=[]

# Define the API request to retrieve the video's comments
    comments_request = YOUTUBE.commentThreads().list(
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
        comments_request = YOUTUBE.commentThreads().list_next(
            comments_request,
            comments_response
        )
    path = f'data/{video_id}.json'
    json.dump(Coments,open(path,'w'),indent=4)
    return path

if __name__ == "__main__":
    getcomments("https://www.youtube.com/watch?v=O37W3BhPrVo")