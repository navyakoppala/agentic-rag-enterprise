import chromadb

client = chromadb.PersistentClient(
    path="./vector_store"
)


def store_embeddings(
    chunks,
    embeddings
):

    try:
        client.delete_collection(
            "enterprise_docs"
        )
    except:
        pass

    collection = client.create_collection(
        name="enterprise_docs"
    )

    ids = [
        str(i)
        for i in range(len(chunks))
    ]

    metadatas = []

    for i in range(len(chunks)):

        metadatas.append(
            {
                "source": "Uploaded PDF",
                "chunk_id": i
            }
        )

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )

    return collection