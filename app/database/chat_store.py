import json
import os


CHAT_FILE = "chat_history.json"


def save_chat(messages):

    with open(CHAT_FILE, "w") as f:
        json.dump(messages, f)


def load_chat():

    if not os.path.exists(CHAT_FILE):
        return []

    with open(CHAT_FILE, "r") as f:
        return json.load(f)