from app.retrieval.qdrant_client import get_qdrant_client

client = get_qdrant_client()

from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct
)

COLLECTION_NAME = "enterprise_docs"


def store_embeddings(
    chunks,
    embeddings,
    pdf_name
):

    try:

        client.get_collection(
            COLLECTION_NAME
        )

    except:

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=len(embeddings[0]),
                distance=Distance.COSINE
            )
        )

    points = []

    for i in range(len(chunks)):

        points.append(

            PointStruct(
                id=abs(
                    hash(
                        pdf_name + str(i)
                    )
                ),
                vector=embeddings[i],
                payload={

                    "text": chunks[i],

                    "source": pdf_name,

                    "document_name": pdf_name,

                    "chunk_id": i

                }
            )

        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    return True