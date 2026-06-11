import streamlit as st

from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_documents

from app.retrieval.embedder import create_embeddings
from app.retrieval.vectordb import store_embeddings
from app.retrieval.retriever import retrieve_context

from app.generation.generator import generate_answer

from app.memory.chat_memory import (
    initialize_memory,
    add_message,
    get_chat_history
)

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="Enterprise PDF RAG",
    layout="wide"
)

# ---------------------------------
# MEMORY INIT
# ---------------------------------

initialize_memory()

if "pdf_indexed" not in st.session_state:
    st.session_state.pdf_indexed = False

# ---------------------------------
# TITLE
# ---------------------------------

st.title("📄 Enterprise PDF RAG")

# ---------------------------------
# SIDEBAR
# ---------------------------------

with st.sidebar:

    st.header("PDF Upload")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# ---------------------------------
# PDF PROCESSING
# ---------------------------------

if uploaded_file:

    if (
        "current_pdf" not in st.session_state
        or
        st.session_state.current_pdf
        != uploaded_file.name
    ):

        documents = load_pdf(
            uploaded_file
        )

        chunks = chunk_documents(
            documents
        )

        embeddings = create_embeddings(
            chunks
        )

        store_embeddings(
            chunks,
            embeddings
        )

        st.session_state.current_pdf = (
            uploaded_file.name
        )

        st.success(
            f"{uploaded_file.name} indexed"
        )

# ---------------------------------
# DISPLAY CHAT HISTORY
# ---------------------------------

for msg in get_chat_history():

    with st.chat_message(
        msg["role"]
    ):
        st.markdown(
            msg["content"]
        )

# ---------------------------------
# CHAT INPUT
# ---------------------------------

question = st.chat_input(
    "Ask anything about your documents..."
)

# ---------------------------------
# QUESTION ANSWERING
# ---------------------------------

if question:

    add_message(
        "user",
        question
    )

    with st.chat_message("user"):

        st.markdown(
            question
        )

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                retrieved = retrieve_context(
                    question
                )

                documents = retrieved.get(
                    "documents",
                    []
                )

                metadata = retrieved.get(
                    "metadata",
                    []
                )

                distance = retrieved.get(
                    "distance",
                    0.5
                )

                context = "\n\n".join(
                    documents
                )

                history = "\n".join(
                    [
                        f"{msg['role']}: {msg['content']}"
                        for msg in get_chat_history()
                    ]
                )

                answer = generate_answer(
                    question,
                    context,
                    history
                )

                st.markdown(
                    answer
                )

                confidence = round(
                    (1 - distance) * 100,
                    2
                )

                st.metric(
                    "Confidence",
                    f"{confidence}%"
                )

                if metadata:

                    with st.expander(
                        "Sources"
                    ):

                        for item in metadata:

                            st.write(
                                f"Source: {item.get('source')} | Chunk: {item.get('chunk_id')}"
                            )

            except Exception as e:

                answer = f"Error: {str(e)}"

                st.error(
                    answer
                )

    add_message(
        "assistant",
        answer
    )

    st.rerun()