import pickle
import numpy as np
import re


def clean_sentence(s):
    temp = []
    regex = r"[^a-zA-Z ]"
    subst = " "
    result = re.sub(regex, subst, s)
    sen = []
    for j in result.split():
        sen.append(j)
    return (" ".join(sen))


def search(query: str, n: int = 200):
    vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))
    x = clean_sentence(query)
    x = vectorizer.transform([x])
    knn = pickle.load(open("tfidf_knn.pkl", "rb"))
    neighbours = knn.kneighbors(x[0], 200)
    distances = (np.max(neighbours[0]) - neighbours[0]) / \
        ((np.max(neighbours[0])-(np.min(neighbours[0]))))
    return (list(zip(neighbours[1][0].tolist(), distances[0].tolist())))


print(search("Heli sddfv"))
