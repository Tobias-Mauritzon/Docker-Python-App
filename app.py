from flask import Flask
from flask import render_template
import os
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("public/start.xhtml")

@app.route("/h1/")
def who():
    return "Who are toy?"


@app.route("/h1/<username>")
def greet(username):
    return f"hi there, {username}!"

@app.route("/index")
def index():
    return render_template("public/index.xhtml")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))