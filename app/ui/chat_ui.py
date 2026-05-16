import streamlit as st

def initialize_chat():
    
    if "messages" not in st.session_state:
        st.session_state.messages = []


def display_chat_history():

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def add_user_message(message):

    st.session_state.messages.append({
        "role": "user",
        "content": message
    })


def add_assistant_message(message):

    st.session_state.messages.append({
        "role": "assistant",
        "content": message
    })


def get_user_input():

    return st.chat_input(
        "Ask questions from your PDF..."
    )