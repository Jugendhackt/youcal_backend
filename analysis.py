import json

from collections import Counter
from transformers import pipeline

import matplotlib.pyplot as plt

def parse_comments(comments):
    data = json.loads(comments)
    data = [data[i]['snippet']["textDisplay"] for i in range(len(data)) if len(data[i]['snippet']["textDisplay"]) < 512]
    max_length = 0
    for i in data:
        if len(i) > max_length:
            max_length = len(i)
    print(max_length)
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

if __name__ == "__main__":
    file = open("data/lanz.json", "r")
    comments = parse_comments(file.read())
    data = sentiment_analysis(comments)
    visualize_data(data)
    data = count_words(comments)