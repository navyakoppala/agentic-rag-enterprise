from sentence_transformers import SentenceTransformer

def get_embedding_model():

    model = SentenceTransformer(
        "BAAI/bge-base-en-v1.5"
    )

    return model


def create_embeddings(chunks):

    model = get_embedding_model()

    embeddings = model.encode(
        chunks
    ).tolist()

    return embeddings