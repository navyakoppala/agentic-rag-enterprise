from sentence_transformers import SentenceTransformer

embedding_model = None

def get_embedding_model():
    global embedding_model

    if embedding_model is None:
        print("Loading Embedding Model...")
        embedding_model = SentenceTransformer(
            "BAAI/bge-base-en-v1.5"
        )
        print("Embedding Model Loaded")

    return embedding_model

def create_embeddings(chunks):

    model = get_embedding_model()

    embeddings = model.encode(
        chunks,
        normalize_embeddings=True
    )

    return embeddings.tolist()

def create_query_embedding(query):

    model = get_embedding_model()

    embedding = model.encode(
        query,
        normalize_embeddings=True
    )

    return embedding.tolist()