import fastapi

app = fastapi.FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, world!"}

# Matplotlib: Generate graph and return image link
@app.get("/api/v1/graph_image")
def calculate(topic: str):
    return {"message": "Image."}

# Finds out the most relevant keywords
@app.get("/api/v1/keywords")
def keywords(topic: str):
    return {"message": "Keywords!"}

# ChatGPT-Summary: Summarizes the Comments and Posts
@app.get("/api/v1/summary")
def summary(topic: str):
    return {"message": "Summary!"}