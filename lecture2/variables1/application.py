import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = random.choice(["Hello, world!", "Hi there!", "Good morning!","Hello there!"])
    return render_template("index.html", headline=headline)
