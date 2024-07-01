from flask import Flask, render_template, request
import os
from Senti import extract_video_id, analyze_sentiment, bar_chart, plot_sentiment
from YoutubeCommentScrapper import save_video_comments_to_csv, get_channel_info, youtube, get_channel_id, get_video_stats

app = Flask(__name__)

def delete_non_matching_csv_files(directory_path, video_id):
    for file_name in os.listdir(directory_path):
        if not file_name.endswith('.csv'):
            continue
        if file_name == f'{video_id}.csv':
            continue
        os.remove(os.path.join(directory_path, file_name))

@app.route('/')
def comment():
    return render_template('comment.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    youtube_link = request.form['youtube_link']
    directory_path = os.getcwd()

    if youtube_link:
        video_id = extract_video_id(youtube_link)
        channel_id = get_channel_id(video_id)
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

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/partner')
def partner():
    return render_template('partner.html')

@app.route('/data')
def pdf():
    return render_template('Data.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
