import numpy as np
import scipy.linalg
from gensim.models import KeyedVectors


def cosine_similarity(vec1, vec2):
  dp = np.dot(vec1, vec2)
  #norm is essentially magnitude.
  norm1 = np.linalg.norm(vec1)
  norm2 = np.linalg.norm(vec2)
  return dp / (norm1 * norm2)


model = KeyedVectors.load_word2vec_format('models/glove.6B.50d.word2vec.txt', binary=False)


def scorer(word1, word2):
  try:
    vec1 = model[word1]
    vec2 = model[word2]
    similarity = cosine_similarity(vec1, vec2)
    print("cosine similarity = ", similarity)
  except KeyError:
    print("error, word probably doesnt exist")
