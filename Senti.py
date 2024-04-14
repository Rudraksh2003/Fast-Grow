from flask import Flask, render_template, request
import os
import csv
import re
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import plotly.express as px
import plotly.graph_objects as go
from colorama import Fore, Style
from typing import Dict

app = Flask(__name__)

nltk.download('vader_lexicon')

def extract_video_id(youtube_link):
    video_id_regex = r"^(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/watch\?v=|youtu.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(video_id_regex, youtube_link)
    if match:
        video_id = match.group(1)
        return video_id
    else:
        return None

def analyze_sentiment(csv_file):
    sid = SentimentIntensityAnalyzer()
    comments = []
    with open(csv_file, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            comments.append(row['Comment'])

    num_neutral = 0
    num_positive = 0
    num_negative = 0
    for comment in comments:
        sentiment_scores = sid.polarity_scores(comment)
        if sentiment_scores['compound'] == 0.0:
            num_neutral += 1
        elif sentiment_scores['compound'] > 0.0:
            num_positive += 1
        else:
            num_negative += 1

    results = {'num_neutral': num_neutral, 'num_positive': num_positive, 'num_negative': num_negative}
    return results

def bar_chart(csv_file: str) -> None:
    results: Dict[str, int] = analyze_sentiment(csv_file)

    num_neutral = results['num_neutral']
    num_positive = results['num_positive']
    num_negative = results['num_negative']

    df = pd.DataFrame({
        'Sentiment': ['Positive', 'Negative', 'Neutral'],
        'Number of Comments': [num_positive, num_negative, num_neutral]
    })

    fig = px.bar(df, x='Sentiment', y='Number of Comments', color='Sentiment', 
                 color_discrete_sequence=['#87CEFA', '#FFA07A', '#D3D3D3'],
                 title='Sentiment Analysis Results')
    fig.update_layout(title_font=dict(size=20))

    return fig

def plot_sentiment(csv_file: str) -> None:
    results: Dict[str, int] = analyze_sentiment(csv_file)

    num_neutral = results['num_neutral']
    num_positive = results['num_positive']
    num_negative = results['num_negative']

    labels = ['Neutral', 'Positive', 'Negative']
    values = [num_neutral, num_positive, num_negative]
    colors = ['yellow', 'green', 'red']
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 marker=dict(colors=colors))])
    fig.update_layout(title={'text': 'Sentiment Analysis Results', 'font': {'size': 20, 'family': 'Arial', 'color': 'grey'},
                              'x': 0.5, 'y': 0.9},
                      font=dict(size=14))
    return fig

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    youtube_link = request.form['youtube_link']
    directory_path = os.getcwd()

    if youtube_link:
        video_id = extract_video_id(youtube_link)
        if video_id:
            csv_file = save_video_comments_to_csv(video_id)
            delete_non_matching_csv_files(directory_path, video_id)

            channel_info = get_channel_info(youtube, channel_id)

            stats = get_video_stats(video_id)

            results = analyze_sentiment(csv_file)

            return render_template('result.html', channel_info=channel_info, stats=stats, results=results, youtube_link=youtube_link)

        else:
            error_message = "Invalid YouTube link"
            return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
