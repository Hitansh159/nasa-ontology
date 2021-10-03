from rank_bm25 import *
import numpy as np
import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import PorterStemmer

class bm25_engine:

  def __init__(self,data:list,is_preprocessed):
    '''
    data : list of documents
    is_preprocessed : true if data is pre_processed else false
    '''
    if is_preprocessed: 
      self._index = list(range(len(data)))
      self._data = data
      self.bm25 =  BM25Okapi(self._data)
    
    else: 
      self._index = list(range(len(data)))
      self._data = self.preprocess(data)
      self.bm25 =  BM25Okapi(self._data)

      
  def __init(self):
    pass

  
  def preprocess(self,data: list):
    '''
    data : list of documents
    '''
    try:
      return list(map(self.preprocess_util,data))
    except Exception as e :
      print('Error in preprocessing')
      print(e)

  def spl_chars_removal(self,my_str):
      str_ =""
      str_ = re.sub("[^0-9A-Za-z ]","",my_str)
      return str_

  def stopwprds_removal_gensim_custom(self,my_str):
      
      ps = PorterStemmer() 

      all_stopwords_gensim = STOPWORDS.union({'none'})

      text_tokens = word_tokenize(my_str)
      tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
      str_t = " ".join(tokens_without_sw)
      return str_t

  def preprocess_util(self,text):

    my_str = text.lower()
    my_str = self.spl_chars_removal(my_str)
    my_str = self.stopwprds_removal_gensim_custom(my_str)
    #print(list_of_docs)
    my_str = ' '.join(list(map(ps.stem,my_str.split(' '))))
    return word_tokenize(my_str)

  
  def query(self,query_str, n = 200):

      q = self.preprocess_util(query_str)
      doc_scores = self.bm25.get_scores(q)

      docs = None
      if (max(doc_scores) <= 0.001):
        docs = np.array([0 for i in doc_scores])
      elif max(doc_scores) - min(doc_scores) <= 0.0001:
        docs = np.array([1 for i in doc_scores])
      else:
        docs = (doc_scores - min(doc_scores))/ (max(doc_scores) - min(doc_scores))
      docs = [ (i,v) for (i,v) in enumerate(docs)]
      docs = sorted(docs, key = lambda x: x[1], reverse = True)

      return docs[:n]
      
      



