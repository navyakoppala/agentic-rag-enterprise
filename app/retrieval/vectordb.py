import chromadb

client = chromadb.PersistentClient(path="./vector_store")

collection = client.get_or_create_collection(
    name="enterprise_knowledge"
)


def store_chunks(chunks):

    for idx, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk],
            ids=[str(idx)]
        )