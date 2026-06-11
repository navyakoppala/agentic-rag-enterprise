from sentence_transformers import (
    CrossEncoder
)

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank_documents(
    question,
    documents
):

    pairs = [
        [question, doc]
        for doc in documents
    ]

    scores = reranker.predict(
        pairs
    )

    ranked = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        doc[0]
        for doc in ranked[:3]
    ]