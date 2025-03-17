import pandas as pd
import nltk
from nltk.corpus import stopwords
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Download stopwords (if not already downloaded)
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

def clean_data(csv_path):
    """
    Cleans phrase data by:
    - Removing duplicates
    - Removing stopwords from phrases
    - Saving cleaned data back to CSV
    """
    try:
        df = pd.read_csv(csv_path)

        if "Phrases" not in df.columns:
            print("Error: 'Phrases' column not found!")
            return

        # Remove duplicates
        df = df.drop_duplicates()

        # Remove stopwords
        df["Phrases"] = df["Phrases"].astype(str).apply(
            lambda x: " ".join([word for word in x.split() if word.lower() not in stop_words])
        )

        # Save cleaned data
        output_file = csv_path.replace(".csv", "_cleaned.csv")
        df.to_csv(output_file, index=False)
        print(f"✅ Data cleaned and saved to: {output_file}")

    except Exception as e:
        print(f"Error during cleaning: {e}")

def find_closest_match(word, word_list):
    """
    Finds the closest match for a given word from a list using Fuzzy Matching (Levenshtein distance).
    Returns the match if similarity is above 80%, otherwise None.
    """
    if not word_list:
        return None

    match, score = process.extractOne(word, word_list, scorer=fuzz.ratio)
    return match if score > 80 else None