from flask import Flask, render_template, request
from googleapiclient.discovery import build
from collections import Counter
import csv
import os
import warnings
import pandas as pd
import toml  # Import the toml library to parse the TOML file

app = Flask(__name__)

import streamlit as st

# Hide warnings
warnings.filterwarnings('ignore')

# Load secrets from the secrets.toml file
with open('secrets.toml', 'r') as f:
    secrets = toml.load(f)

# Retrieve the API key from the secrets
DEVELOPER_KEY = secrets['api_key']

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# Create a client object to interact with the YouTube API
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

def get_channel_id(video_id):
    response = youtube.videos().list(part='snippet', id=video_id).execute()
    channel_id = response['items'][0]['snippet']['channelId']
    return channel_id


def save_video_comments_to_csv(video_id):
    # Retrieve comments for the specified video using the comments().list() method
    comments = []
    results = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText'
    ).execute()

    # Extract the text content of each comment and add it to the comments list
    while results:
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            username = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comments.append([username, comment])
        if 'nextPageToken' in results:
            nextPage = results['nextPageToken']
            results = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                textFormat='plainText',
                pageToken=nextPage
            ).execute()
        else:
            break

    # Save the comments to a CSV file with the video ID as the filename
    filename = video_id + '.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Username', 'Comment'])
        for comment in comments:
            writer.writerow([comment[0], comment[1]])

    return filename


def get_video_stats(video_id):
    try:
        response = youtube.videos().list(
            part='statistics',
            id=video_id
        ).execute()

        return response['items'][0]['statistics']

    except HttpError as error:
        print(f'An error occurred: {error}')
        return None


def get_channel_info(youtube, channel_id):
    try:
        response = youtube.channels().list(
            part='snippet,statistics,brandingSettings',
            id=channel_id
        ).execute()

        channel_title = response['items'][0]['snippet']['title']
        video_count = response['items'][0]['statistics']['videoCount']
        channel_logo_url = response['items'][0]['snippet']['thumbnails']['high']['url']
        channel_created_date = response['items'][0]['snippet']['publishedAt']
        subscriber_count = response['items'][0]['statistics']['subscriberCount']
        channel_description = response['items'][0]['snippet']['description']

        channel_info = {
            'channel_title': channel_title,
            'video_count': video_count,
            'channel_logo_url': channel_logo_url,
            'channel_created_date': channel_created_date,
            'subscriber_count': subscriber_count,
            'channel_description': channel_description
        }

        return channel_info

    except HttpError as error:
        print(f'An error occurred: {error}')
        return None


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

            return render_template('result.html', channel_info=channel_info, stats=stats, results=results,
                                   youtube_link=youtube_link)

        else:
            error_message = "Invalid YouTube link"
            return render_template('error.html', error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)
