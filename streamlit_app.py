import streamlit as st

from app.auth.auth import authenticate, create_user

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

st.set_page_config(
    page_title="Enterprise Document Workspace",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = None

if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = None

if "documents" not in st.session_state:
    st.session_state.documents = []


if not st.session_state.logged_in:

    st.title(" Enterprise Workspace Login")

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:

        username = st.text_input(
            "Username",
            key="login_user"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_pass"
        )

        if st.button("Login"):

            if authenticate(username, password):

                st.session_state.logged_in = True
                st.session_state.username = username

                st.success("Login Successful")
                st.rerun()

            else:

                st.error(
                    "Invalid Username or Password"
                )

    with tab2:

        new_user = st.text_input(
            "New Username",
            key="register_user"
        )

        new_pass = st.text_input(
            "New Password",
            type="password",
            key="register_pass"
        )

        if st.button("Create Account"):

            if create_user(
                new_user,
                new_pass
            ):

                st.success(
                    "Account Created Successfully"
                )

            else:

                st.error(
                    "User Already Exists"
                )

    st.stop()


    uploaded_file = st.file_uploader(
    "",
    type=["pdf"],
    label_visibility="collapsed"
)


initialize_memory()

with st.sidebar:

    st.success(
        f"{st.session_state.username}"
    )

    st.header(" Documents")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    for doc in st.session_state.documents:

        if st.button(
            doc,
            use_container_width=True
        ):
            st.session_state.current_pdf = doc
            st.rerun()

    st.divider()

    if st.button(
        " Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    if st.button(
        " Logout",
        use_container_width=True
    ):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()


with st.sidebar:

    st.success(
        f" {st.session_state.username}"
    )

    st.header(" Documents")

    for i, doc in enumerate(st.session_state.documents):

        if st.button(
        doc,
        key=f"doc_{i}",
        use_container_width=True
    ):

            st.session_state.current_pdf = doc

            st.rerun()

    st.divider()

    if st.button(
        "Clear Chat",
        key="clear_chat_btn",
        use_container_width=True
   ):

        st.session_state.messages = []

        st.rerun()

    st.divider()

    if st.button(
        "Logout",
        key="logout_btn",
        use_container_width=True
   ):

        st.session_state.logged_in = False
        st.session_state.username = None

        st.rerun()

if uploaded_file:

    if uploaded_file.name not in st.session_state.documents:

        st.session_state.documents.append(
            uploaded_file.name
        )

    if st.session_state.current_pdf != uploaded_file.name:

        with st.spinner("Indexing PDF..."):

            text = load_pdf(
                uploaded_file
            )

            chunks = chunk_documents(
                text
            )

            embeddings = create_embeddings(
                chunks
            )

            store_embeddings(
                chunks,
                embeddings,
                uploaded_file.name
            )

            st.session_state.current_pdf = (
                uploaded_file.name
            )

        st.success(
            f"{uploaded_file.name} indexed successfully"
        )
if st.session_state.current_pdf:

    st.info(
        f" Current Document: {st.session_state.current_pdf}"
    )

else:

    st.warning(
        "Upload a PDF to begin."
    )

for msg in get_chat_history():

    with st.chat_message(
        msg["role"]
    ):

        st.markdown(
            msg["content"]
        )

question = st.chat_input(
    "Ask anything about your documents..."
)


if question and st.session_state.current_pdf:

    add_message(
        "user",
        question
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        try:

            retrieved = retrieve_context(
                question,
                st.session_state.current_pdf
            )

            documents = retrieved.get(
                "documents",
                []
            )

            metadata = retrieved.get(
                "metadata",
                []
            )

            context = "\n\n".join(
                documents
            )

            history = "\n".join([
                f"{m['role']}: {m['content']}"
                for m in get_chat_history()
            ])

            answer = generate_answer(
                question,
                context,
                history
            )

            st.markdown(answer)

            if metadata:

                with st.expander(
                    " Sources"
                ):

                    for item in metadata:

                        st.write(
                            f"{item.get('source')} | Chunk {item.get('chunk_id')}"
                        )

        except Exception as e:

            answer = f"Error: {str(e)}"

            st.error(answer)

    add_message(
        "assistant",
        answer
    )

    st.rerun()