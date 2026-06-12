from qdrant_client import QdrantClient
import streamlit as st


@st.cache_resource
def get_qdrant_client():

    return QdrantClient(
        path="./qdrant_db"
    )