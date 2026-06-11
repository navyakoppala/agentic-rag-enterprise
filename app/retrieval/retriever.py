from app.retrieval.embedder import (
    get_embedding_model
)

from app.retrieval.reranker import (
    rerank_documents
)

import chromadb


def retrieve_context(question):

    if not question:

        return {
            "documents": [],
            "metadata": []
        }

    client = chromadb.PersistentClient(
        path="./vector_store"
    )

    collection = client.get_collection(
        "enterprise_docs"
    )

    model = get_embedding_model()

    query_embedding = model.encode(
        str(question)
    ).tolist()

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=10
    )
    distances = results["distances"][0]

    documents = results["documents"][0]

    top_docs = rerank_documents(
        question,
        documents
    )

    metadata = []

    if "metadatas" in results:

        for item in results["metadatas"][0]:

            metadata.append(
                item
            )
    top_metadata = results["metadatas"][0]

    return {
    "documents": top_docs,
    "metadata": top_metadata,
    "distance": distances[0]
}