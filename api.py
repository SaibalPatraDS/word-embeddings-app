from fastapi import FastAPI
from src.phrase_matching import PhraseMatcher

app = FastAPI()
matcher = PhraseMatcher("data/phrases.csv", "data/word_vectors.kv")

@app.get("/match/")
async def match_phrase(phrase: str):
    match, score = matcher.find_match(phrase)
    return {"input": phrase, "closest_match": match, "score": score}