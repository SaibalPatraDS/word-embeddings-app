import argparse
from src.phrase_matching import PhraseMatcher

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phrase Matcher CLI")
    parser.add_argument("phrase", type=str, help="Enter a phrase to match")
    args = parser.parse_args()

    matcher = PhraseMatcher("data/phrases.csv", "data/word_vectors.kv")
    match, score = matcher.find_match(args.phrase)
    print(f"Closest Match: {match}, Score: {score}")