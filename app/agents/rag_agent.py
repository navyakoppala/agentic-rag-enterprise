from app.retrieval.retriever import retrieve_context
from app.generation.generator import generate_answer


def agentic_rag(question):

    retrieved_docs = retrieve_context(question)

    if not retrieved_docs:

        return "No relevant documents found."

    answer = generate_answer(question, retrieved_docs)

    return answer