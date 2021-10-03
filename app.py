from typing import Counter
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
    
    nodes = []
    result = {"nodes":[], "links":[]}


    nodes0 = embedding_engine.search(query, 10)
    for node, dist in nodes0:
        nodes.append(node)
        result['nodes'].append(datasets[str(node)])
        result['links'].append({
            "source": nodes0[0][0],
            "target": node,
            "value": dist
        })
  
    for idx, i in enumerate(nodes0):

        nodes1 = embedding_engine.search(datasets[str(i[0])]['title'], 15+5*idx)
        counter = 0
        for node, dist in nodes1:
            if node not in nodes:
                nodes.append(node)
                result['nodes'].append(datasets[str(node)])

                result['links'].append({
                    "source": i[0],
                    "target": node,
                    "value": dist
                })
                counter += 1
            if counter == 10:
                break


    return render_template('visualizer.html', data=result)