from flask import Flask
from flask import render_template
from engines import embedding_engine
import json
import urllib 

datasets = json.load(open('./storage/master_data.json'))
# bm25_engine = bm25_engine.bm25_engine()

app = Flask(__name__, static_folder="static")

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/dataset/<query>')
def dataset(query):
    engine = 'embedding_engine'
    nodes = embedding_engine.search(query)
    result = {"nodes":[], "links":[]}
    for node, dist in nodes:
        result['nodes'].append(datasets[str(node)])
        result['links'].append({
            "source": nodes[0][0],
            "target": node,
            "value": dist
        })

    return f'query: {query} <br> Results: {result}'