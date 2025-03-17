from data_preprocessing import clean_data
from phrase_matching import PhraseMatcher

def run_pipeline():
    print("Starting Phrase Matching Pipeline...")

    # Step 1: Clean Data
    clean_data("data/phrases.csv")

    # Step 2: Load Model
    matcher = PhraseMatcher("data/phrases.csv", "data/word_vectors.kv")

    # Step 3: Interactive User Input Loop
    while True:
        phrase = input("Enter a phrase to match (or type 'exit' to quit): ").strip()
        
        if phrase.lower() == "exit":
            print("Exiting the pipeline...")
            break

        match, score = matcher.find_match(phrase)
        print(f"Closest Match: {match} (Score: {score})\n")

if __name__ == "__main__":
    run_pipeline()
