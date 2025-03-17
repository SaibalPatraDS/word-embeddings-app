# word-embeddings-app

## Step-by-Step Guide to Using This Repo


1️⃣ Clone the Repository

```
git clone https://github.com/SaibalPatraDS/word-embeddings-app.git
cd word-embeddings-app
```

2️⃣ Set Up the Environment

Choose either Conda or pip:

🔹 Using Conda

```conda env create -f environment.yml
conda activate phrase-matcher```

🔹 Using pip (if not using Conda)

``` pip install -r requirements.txt```


3️⃣ Download the Pre-trained Word2Vec Model

Make sure `GoogleNews-vectors-negative300.bin` is inside the data/ folder.
If not, download it from [text](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit) and place it there.

4️⃣ Preprocess the Data (Optional)

If you want to clean phrases.csv (remove duplicates, stopwords):

``` python src/data_preprocessing.py ```

5️⃣ Run the Phrase Matching CLI

Test the phrase matching system using the command-line interface:

```python app.py```

or 

```python app_2.0.py```

🔹 Enter a phrase and get the closest match from the dataset.

```
 word-embeddings-app
 ├──  data
 │    ├── phrases.csv                # Input file containing phrases (.csv)
 │    ├── phrase_vectors.pkl          # Pickled phrase embeddings (.pkl)
 │    ├── phrase_similarity.pkl       # Precomputed similarity matrix (.pkl)
 │    ├── GoogleNews-vectors-negative300.bin  # Word2Vec binary model (.bin)
 │    ├── word_vectors.kv             # Optimized word vectors storage (.kv)
 │
 ├──  src
 │    ├── phrase_matching.py          # Core phrase matching functions (.py)
 │    ├── embedding_utils.py          # Helper functions for embeddings (.py)
 │    ├── data_preprocessing.py       # Cleaning, removing duplicates, stopwords (.py) ➡️ (Bonus IV)
 │    ├── pipeline.py                 # Code to run the process as a pipeline (.py) ➡️ (Bonus III)
 │    ├── tests
 │    │    ├── test_phrase_matching.py # Unit tests for phrase matching (.py) ➡️ (Bonus III)
 │    │    ├── test_embeddings.py      # Unit tests for embeddings (.py) ➡️ (Bonus III)
 │
 ├──  app.py                           # CLI-based phrase matcher (.py)
 ├──  api.py                           # FastAPI-based web service (.py) ➡️ (Bonus V)
 ├──  requirements.txt                  # Required Python libraries (.txt)
 ├──  environment.yml                    # Conda environment file ➡️ (Bonus I)
 ├──  README.md                          # Documentation (.md) ➡️ (Bonus II)

```


## Step-by-Step Description of Each Component

1️⃣ Data Directory (`data/`)

This folder contains all necessary files for phrase matching and word embeddings.

`phrases.csv` → Contains predefined phrases for matching.

`phrase_vectors.pkl` → Stores phrase embeddings after processing.

`phrase_similarity.pkl` → Stores precomputed phrase similarity scores.

`GoogleNews-vectors-negative300.bin` → Pre-trained Word2Vec model from Google News.

`word_vectors.kv` → Optimized storage of word vectors for faster access.

2️⃣ Source Code (`src/`)

This directory contains the core functionality of the project.

🔹 `phrase_matching.py` → (Core Matching Logic)

Loads precomputed phrase embeddings.

Finds the closest matching phrase using Word2Vec similarity.

Implements fuzzy matching (Levenshtein distance) when exact matches aren't found.

🔹 `embedding_utils.py` → (Embedding Functions)

Converts text phrases into numerical word embeddings using Word2Vec.

Computes cosine similarity between phrase vectors.

🔹 `data_preprocessing.py` → (Preprocessing - Bonus IV)

Removes duplicates from phrases.csv.

Removes stopwords using NLTK.

Handles missing words by finding the closest match using Levenshtein distance.

Saves the cleaned data back into phrases.csv.

🔹 `pipeline.py` → (Automating the Process - Bonus III)

Runs the phrase matching pipeline automatically.

Loads and cleans data from phrases.csv.

Processes phrases and stores results in phrase_vectors.pkl.

Can be scheduled to run at fixed intervals (e.g., via cron jobs).

🔹 `tests/` → (Unit Tests - Bonus III)

`test_phrase_matching.py` → Tests phrase matching logic.

`test_embeddings.py` → Tests word embedding functions.

Ensures correctness of functions before deployment.

## Testing `app_2.0.py`

Command : `python app_2.0.py` 

Output Sample : 
![Output Sample](https://github.com/user-attachments/assets/a018c452-a6f7-439f-8319-a3d93b80ba94)
