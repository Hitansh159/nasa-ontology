from flask import Flask
from flask import render_template
from engines import embedding_engine, bm25_engine, tfidf_engine
import json

datasets = json.load(open('./static/master_data.json'))
bm25_engine = bm25_engine.bm25_engine()

app = Flask(__name__, static_folder="static")

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/dataset/<query>')
def dataset(query):
    engine = 'embedding_engine'
    result = embedding_engine.search(query)
    
    return f'query: {query}\nResults: {result}'