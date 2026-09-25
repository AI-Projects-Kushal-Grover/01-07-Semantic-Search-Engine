from typing import List

from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

class Embedder():
    def __init__(self) -> None:
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL)

    def embed(self, chunks: List[str]):
        embeddings: list[tuple[str, list[float]]] = []
        for chunk in chunks:
            embeddings.append((chunk, self.embedding_model.encode(chunk, normalize_embeddings=True).tolist()))
        return embeddings
