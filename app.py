from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/list")
def list():
    return render_template("list.html")
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(port=8000, debug=True)