import os
import gensim
from gensim.models import KeyedVectors
import pandas as pd

def load_word_vectors(model_path=r"C:\Users\saiba\OneDrive\Documents\Projects Machine Learning\Project 66 - Galytix Assignment\word-embeddings-app\GoogleNews-vectors-negative300.bin", limit=1000000):
    """
    Loads pre-trained Word2Vec embeddings.
    """
    wv = KeyedVectors.load_word2vec_format(model_path, binary=True, limit=limit)
    return wv

def save_word_vectors(wv, output_file="data/vectors.csv"):
    """
    Saves word vectors in a structured CSV format.
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure directory exists

    print(f"Saving word vectors to {output_file}...")
    with open(output_file, "w", encoding="utf-8") as f:  # Use UTF-8 encoding
        for word in wv.index_to_key:
            vector = " ".join(map(str, wv[word]))
            f.write(f"{word},{vector}\n")
    print("Word embeddings saved successfully.")

if __name__ == "__main__":
    word_vectors = load_word_vectors()
    save_word_vectors(word_vectors)
    print("Word embeddings saved to vectors.csv")