from app.retrieval.embedder import (
    get_embedding_model
)

from app.retrieval.vectordb import (
    collection
)

from app.retrieval.reranker import (
    rerank_documents
)


def retrieve_context(question):

    model = get_embedding_model()

    query_embedding = model.encode(
        question
    ).tolist()

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=10
    )

    documents = results["documents"][0]

    top_docs = rerank_documents(
        question,
        documents
    )

    context = "\n".join(
        top_docs
    )

    return context