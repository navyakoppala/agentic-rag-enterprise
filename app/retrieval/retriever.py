from app.retrieval.vectordb import collection


def retrieve_context(query, top_k=2):

    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    documents = results["documents"][0]

    cleaned_docs = []

    for doc in documents:
        cleaned_docs.append(doc[:300])

    return cleaned_docs