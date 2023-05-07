import fastapi
import analysis
import scraper

app = fastapi.FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, world!"}

# Finds out the most relevant keywords
@app.get("/api/v1/keywords")
def keywords(video_link: str, request: fastapi.Request):
    file = open(scraper.getcomments(video_link), "r")
    return {"img_url":  request.url._url.replace(f"api/v1/keywords?video_link={video_link}", "") + "img/?name=" + analysis.wordcloud(analysis.parse_comments(file.read()))}

# Sentiment Analysis: Finds out the sentiment of the comments
@app.get("/api/v1/analysis")
def keywords(video_link: str, request: fastapi.Request):
    file = open(scraper.getcomments(video_link), "r")
    return {"img_url": request.url._url.replace(f"api/v1/analysis?video_link={video_link}", "") + "img/?name=" + analysis.visualize_data(analysis.sentiment_analysis(analysis.parse_comments(file.read())))}

@app.get("/img/")
def img(name: str):
    return fastapi.responses.FileResponse(f"assets/img/{name}")