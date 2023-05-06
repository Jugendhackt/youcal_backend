import fastapi
import analysis

app = fastapi.FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, world!"}

# Finds out the most relevant keywords
@app.get("/api/v1/keywords")
def keywords(topic: str, num_words: int = 10):
    file = open(f"data/{topic}.json", "r")
    return analysis.count_words(analysis.parse_comments(file.read()), num_words)

# Sentiment Analysis: Finds out the sentiment of the comments
@app.get("/api/v1/analysis")
def keywords(topic: str):
    file = open(f"data/{topic}.json", "r")
    return analysis.sentiment_analysis(analysis.parse_comments(file.read()))