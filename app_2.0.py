from src.phrase_matching import PhraseMatcher

if __name__ == "__main__":
    matcher = PhraseMatcher("data/phrases.csv", "data/word_vectors.kv")

    while True:
        phrase = input("Enter a phrase to match (or type 'exit' to quit): ").strip()
        
        if phrase.lower() == "exit":
            print("Exiting...")
            break
        
        match, score = matcher.find_match(phrase)
        print(f"Closest Match: {match}, Score: {score}\n")