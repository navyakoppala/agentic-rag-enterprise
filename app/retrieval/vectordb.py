import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="rag_collection"
)


def store_embeddings(
    chunks,
    embeddings
):

    collection.add(
        documents=chunks,

        embeddings=embeddings,

        ids=[
            str(i)
            for i in range(
                len(chunks)
            )
        ]
    )