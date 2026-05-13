import streamlit as st

from app.agents.rag_agent import agentic_rag

st.title("Enterprise Agentic RAG Assistant")

question = st.text_input("Ask your question")

if st.button("Generate Answer"):

    if question:

        answer = agentic_rag(question)

        st.write(answer)