import pandas as pd
import numpy as np
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

# Load optimized word vectors
wv = KeyedVectors.load("data/word_vectors.kv")

# Load phrases
phrases_df = pd.read_csv("data/phrases.csv", encoding="ISO-8859-1")

# Function to compute phrase embeddings
def get_phrase_embedding(phrase, wv):
    words = phrase.split()
    word_vectors = [wv[word] for word in words if word in wv]
    return np.mean(word_vectors, axis=0) if word_vectors else np.zeros(wv.vector_size)

# Compute and store phrase embeddings
phrases_df['vector'] = phrases_df['Phrases'].apply(lambda x: get_phrase_embedding(x, wv))
phrases_df.to_pickle("data/phrase_vectors.pkl")

## Phrase Matching

# Load phrase embeddings
phrases_df = pd.read_pickle("data/phrase_vectors.pkl")

# Convert vectors to NumPy array
vectors = np.stack(phrases_df['vector'].values)

# Compute similarity matrix
similarity_matrix = cosine_similarity(vectors)

# Store for faster retrieval
similarity_df = pd.DataFrame(similarity_matrix, index=phrases_df['Phrases'], columns=phrases_df['Phrases'])
similarity_df.to_pickle("data/phrase_similarity.pkl")


## Implement Real-Time Phrase Matching
def find_closest_match(input_phrase, phrases_df, wv):
    input_vector = get_phrase_embedding(input_phrase, wv)
    vectors = np.stack(phrases_df['vector'].values)
    similarities = cosine_similarity([input_vector], vectors)[0]
    best_match_idx = np.argmax(similarities)
    return phrases_df.iloc[best_match_idx]['phrase'], similarities[best_match_idx]
