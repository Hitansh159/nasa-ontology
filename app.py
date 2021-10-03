from flask import Flask
from flask import render_template, url_for

app = Flask(__name__, static_folder="static")

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/dataset/<query>')
def dataset():
    pass
