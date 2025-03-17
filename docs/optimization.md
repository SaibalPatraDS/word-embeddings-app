## Optimization

* Vector Preloading: Load word_vectors.kv into memory on startup.
* Batch Processing: Instead of processing one phrase at a time, allow batch requests.
* FAISS Indexing: Use Facebook’s FAISS to speed up similarity search.
* Caching Results: Use Redis to store frequently queried phrase embeddings.