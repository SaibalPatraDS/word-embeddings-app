import pytest
from phrase_matching import PhraseMatcher

matcher = PhraseMatcher("data/phrases.csv", "data/word_vectors.kv")

def test_find_match():
    phrase = "how company compares to its peers?"
    match, score = matcher.find_match(phrase)
    assert isinstance(match, str)
    assert isinstance(score, float)
    assert 0 <= score <= 1

def test_empty_input():
    match, score = matcher.find_match("")
    assert match is None
    assert score == 0.0
