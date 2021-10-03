import numpy as np
import json
import pickle

model = pickle.load(open('', 'rb'))

word_embeddings = {}
f = open('glove.6B.200d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs
f.close()

def search(query:str, n:int = 200):
    v = sum([word_embeddings.get(w, np.zeros((100,))) for w in query.split()])/(len(query.split())+0.001)
    results = model.kneighbors([v])

    distances = (np.max(results[0]) - results[0]) / \
        ((np.max(results[0])-(np.min(results[0]))))
    return (list(zip(results[1][0].tolist(), distances[0].tolist())))
