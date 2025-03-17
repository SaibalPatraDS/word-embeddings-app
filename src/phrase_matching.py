import pandas as pd
import numpy as np
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

class PhraseMatcher:
    def __init__(self, phrase_file, vector_file):
        # Load word vectors
        self.wv = KeyedVectors.load(vector_file)

        # Load phrases and compute embeddings
        self.phrases_df = pd.read_csv(phrase_file, encoding="ISO-8859-1")
        self.phrases_df['vector'] = self.phrases_df['Phrases'].apply(lambda x: self.get_phrase_embedding(x))

        # Convert to NumPy array
        self.vectors = np.stack(self.phrases_df['vector'].values)

        # Compute similarity matrix and store it
        similarity_matrix = cosine_similarity(self.vectors)
        self.similarity_df = pd.DataFrame(similarity_matrix, index=self.phrases_df['Phrases'], columns=self.phrases_df['Phrases'])

    def get_phrase_embedding(self, phrase):
        """Compute embedding for a given phrase."""
        words = phrase.split()
        word_vectors = [self.wv[word] for word in words if word in self.wv]
        return np.mean(word_vectors, axis=0) if word_vectors else np.zeros(self.wv.vector_size)

    def find_match(self, input_phrase):
        """Find the closest matching phrase."""
        input_vector = self.get_phrase_embedding(input_phrase)
        similarities = cosine_similarity([input_vector], self.vectors)[0]
        best_match_idx = np.argmax(similarities)
        return self.phrases_df.iloc[best_match_idx]['Phrases'], similarities[best_match_idx]