import json

from collections import Counter
from transformers import pipeline

import matplotlib.pyplot as plt
from wordcloud import WordCloud

def parse_comments(comments):
    data = json.loads(comments)
    data = [data[i]['snippet']["textDisplay"] for i in range(len(data)) if len(data[i]['snippet']["textDisplay"]) < 512]
    return data

def sentiment_analysis(comments):
    sentiment_pipeline = pipeline("sentiment-analysis")
    #print(comments)
    result = sentiment_pipeline(comments)

    negative_comments = str(result).count("NEGATIVE")
    positive_comments = str(result).count("POSITIVE")

    return {"negative": negative_comments, "positive": positive_comments, "total": len(comments)}

def count_words(data, num_words=10):
    stopwords = open("stopwords.txt", "r").read().split("\n")

    word_counts = Counter(word for word in str(data).lower().replace("[", "").replace("]", "").replace("'", "").replace(",", "").split() if word not in stopwords)
    common_words = word_counts.most_common(num_words) 
    return common_words

def visualize_data(data):
    fig, ax = plt.subplots()

    content = ["Negative", "Positive"]
    counts = [data["negative"], data["positive"]]
    bar_labels = ['red', 'blue']
    bar_colors = ['tab:red', 'tab:blue']

    ax.bar(content, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Anzahl der Personen')
    ax.set_title('Sentiment Analysis von YouTube Kommentaren')

    plt.show()

def wordcloud(comments):
    data = ""
    for comment in comments:
        data += comment
    wordcloud = WordCloud(width=1600, height=800, max_font_size=200, background_color="white").generate(data)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.show()

if __name__ == "__main__":
    file = open("data/roblox.json", "r")
    comments = parse_comments(file.read())
    #data = sentiment_analysis(comments)
    #visualize_data(data)
    #data = count_words(comments)
    wordcloud(comments)