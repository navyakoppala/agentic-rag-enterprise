import streamlit as st

from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_documents

from app.retrieval.embedder import (
    create_embeddings
)

from app.retrieval.vectordb import (
    store_embeddings
)

from app.retrieval.retriever import (
    retrieve_context
)

from app.generation.generator import (
    generate_answer
)

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Agentic RAG Enterprise",
    page_icon="IntelligentAssistant",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-left:8rem;
    padding-right:8rem;
}

[data-testid="stChatMessage"]{
    padding:1rem;
    border-radius:12px;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# TITLE
# =====================================

st.title("Agentic RAG Enterprise")

st.markdown(
    "Enterprise AI Assistant powered by RAG + Gemini"
)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.header("Upload Knowledge Base")

    uploaded_files = st.file_uploader(
        "Upload PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("Process Documents"):

        if uploaded_files:

            with st.spinner(
                "Processing PDFs..."
            ):

                all_chunks = []

                for uploaded_file in uploaded_files:

                    text = load_pdf(
                        uploaded_file
                    )

                    chunks = chunk_documents(
                        text
                    )

                    all_chunks.extend(
                        chunks
                    )

                embeddings = create_embeddings(
                    all_chunks
                )

                store_embeddings(
                    all_chunks,
                    embeddings
                )

            st.success(
                "Documents processed successfully!"
            )

# =====================================
# CHAT MEMORY
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================
# DISPLAY CHAT HISTORY
# =====================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

# =====================================
# USER INPUT
# =====================================

question = st.chat_input(
    "Ask anything about your documents..."
)

# =====================================
# QUESTION ANSWERING
# =====================================

if question:

    # USER MESSAGE
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):

        st.markdown(question)

    # ASSISTANT
    with st.chat_message("assistant"):

        with st.spinner(
            "Thinking..."
        ):

            context = retrieve_context(
                question
            )

            answer = generate_answer(
                question,
                context
            )

            st.markdown(answer)

    # SAVE RESPONSE
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })