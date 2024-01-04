from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/list")
def list():
    return render_template("list.html")
@app.route("/filter")
def filter():
    return render_template("filter.html")