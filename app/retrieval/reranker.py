from sentence_transformers import CrossEncoder


def get_reranker():

    reranker = CrossEncoder(
        "cross-encoder/ms-marco-MiniLM-L-6-v2"
    )

    return reranker


def rerank_documents(
    question,
    documents
):

    reranker = get_reranker()

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

    top_docs = [
        doc[0]
        for doc in ranked[:3]
    ]

    return top_docs