import numpy as np
import pickle
from urllib.request import urlopen

pfile = open('./storage/embedding-knn.pkl', 'rb')
model = pickle.load(pfile)

word_embeddings = {}
f = open('./storage/glove.6B.100d.txt')
for line in f:
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






