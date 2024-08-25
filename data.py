import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_TOKEN = "" 

@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template("Data.html")

@app.route("/Summarize", methods=["POST"])
def Summarize():
    if request.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        data = request.form["data"]

        maxL = int(request.form["maxL"])
        minL = maxL // 4

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query(
            {
                "inputs": data,
                "parameters": {"min_length": minL, "max_length": maxL},
            }
        )[0]

        return render_template("Data.html", result=output["summary_text"])
    else:
        return render_template("Data.html")

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/partner')
def about():
    return render_template('partner.html')

@app.route('/comment')
def pdf():
    return render_template('comment.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Ensure this is 5001

