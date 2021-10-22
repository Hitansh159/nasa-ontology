import numpy as np
import json
import pickle
from urllib.request import urlopen
import requests 

model = pickle.load(urlopen('https://download1488.mediafire.com/e1r7fbtzpvsg/d42ui2jpk72lhie/embedding-knn.pkl'))

word_embeddings = {}
f = urlopen('https://download1502.mediafire.com/9ybvz6z7hnig/zp8pc0tshe9t20b/glove.6B.100d.txt')
for line in f:
    line = line.decode('utf8')
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs
f.close()

def search(query:str, n:int = 200):

    v = sum( map(lambda x: word_embeddings.get(x, np.zeros((100,))),  query.split()) ) / (len(query.split())+0.001)

    results = model.kneighbors([v])
    # print(len(results[0][0]))

    distances = (np.max(results[0]) - results[0]) / \
        ((np.max(results[0])-(np.min(results[0]))))
    
    return (list(zip(results[1][0].tolist(), distances[0].tolist())))[:n]






