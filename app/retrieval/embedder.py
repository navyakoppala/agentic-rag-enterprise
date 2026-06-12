from sentence_transformers import SentenceTransformer

print("Loading Embedding Model...")

embedding_model = SentenceTransformer(
    "BAAI/bge-base-en-v1.5"
)

print("Embedding Model Loaded")


def get_embedding_model():
    """
    Returns loaded embedding model
    """
    return embedding_model


def create_embeddings(chunks):
    """
    Creates embeddings for document chunks
    """

    if not chunks:
        return []

    embeddings = embedding_model.encode(
        chunks,
        normalize_embeddings=True
    )

    return embeddings.tolist()


def create_query_embedding(query):
    """
    Creates embedding for user query
    """

    embedding = embedding_model.encode(
        query,
        normalize_embeddings=True
    )

    return embedding.tolist()