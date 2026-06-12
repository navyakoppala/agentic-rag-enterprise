from app.retrieval.qdrant_client import get_qdrant_client
from app.retrieval.embedder import get_embedding_model
from app.retrieval.reranker import rerank_documents

from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue
)

client = get_qdrant_client()

COLLECTION_NAME = "enterprise_docs"


def retrieve_context(question, document_name):

    model = get_embedding_model()

    query_embedding = model.encode(
        question,
        normalize_embeddings=True
    ).tolist()

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        query_filter=Filter(
            must=[
                FieldCondition(
                    key="document_name",
                    match=MatchValue(
                        value=document_name
                    )
                )
            ]
        ),
        limit=10
    )

    documents = []
    metadata = []
    scores = []

    for hit in results.points:

        documents.append(
            hit.payload.get("text", "")
        )

        metadata.append(
            {
                "source": hit.payload.get(
                    "source",
                    document_name
                ),
                "chunk_id": hit.payload.get(
                    "chunk_id",
                    0
                ),
                "document_name": hit.payload.get(
                    "document_name",
                    document_name
                )
            }
        )

        scores.append(hit.score)

    if not documents:

        return {
            "documents": [],
            "metadata": [],
            "distance": 1
        }

    top_docs = rerank_documents(
        question,
        documents
    )

    return {
        "documents": top_docs,
        "metadata": metadata,
        "distance": 1 - max(scores)
    }