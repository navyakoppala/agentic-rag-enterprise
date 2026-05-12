from app.ingestion.loader import load_pdf

from app.retrieval.embedder import (
    chunk_text
)

from app.retrieval.vectordb import store_chunks

from app.agents.rag_agent import agentic_rag


def setup_rag():

    text = load_pdf("data/hr_policy.pdf")

    chunks = chunk_text(text)

    store_chunks(chunks)

    print("Documents indexed successfully.")


def chat():

    while True:

        question = input("\nAsk Question: ")

        if question.lower() == "exit":
            break

        answer = agentic_rag(question)

        print("\nAnswer:")
        print(answer)


if __name__ == "__main__":

    setup_rag()

    chat()