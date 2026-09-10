from sentence_transformers import SentenceTransformer


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


print("Loading embedding model...")

model = SentenceTransformer(
    MODEL_NAME
)


def embed(texts, batch_size=32):

    if not texts:
        return []

    return model.encode(
        texts,
        batch_size=batch_size,
        normalize_embeddings=True,
        show_progress_bar=True
    ).tolist()