import gensim
from gensim.models import KeyedVectors

# Load first 1,000,000 word embeddings
wv = KeyedVectors.load_word2vec_format("data/GoogleNews-vectors-negative300.bin", binary=True, limit=1000000)

# Save in a more efficient format
wv.save("data/word_vectors.kv")