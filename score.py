import numpy as np
import config
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('models/glove.6B.50d.word2vec.txt', binary=False)

def cosine_similarity(vec1, vec2):
  dp = np.dot(vec1, vec2)
  #norm is essentially magnitude.
  norm1 = np.linalg.norm(vec1)
  norm2 = np.linalg.norm(vec2)
  return dp / (norm1 * norm2)


def scorer(word1, target_word, word_list):
    try:
        vec1 = model[word1]
        vec_target = model[target_word]
        
        similarity = cosine_similarity(vec1, vec_target)
        print(f"Cosine similarity with target: {similarity:.5f}")
        
        #ranking alg, might be able to precompute this but i dont want to do that
        similarities = []
        for word in word_list:
            try:
                vec = model[word]
                score = cosine_similarity(vec1, vec)
                similarities.append((word, score))
            except KeyError:
                continue
        
        #reverse order
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        #rank of guessed word
        rank = next((i + 1 for i, (word, _) in enumerate(similarities) if word == target_word), None)
        print(f"{word1} is ranked #{rank} out of {len(similarities)}.")
        
        if 1 - config.WINNING_TOLERANCE <= similarity <= 1 + config.WINNING_TOLERANCE:
            return True
        else:
            return False
          
    except KeyError:
        print(f"Error: '{word1}' is not in the vocabulary.")
        return False