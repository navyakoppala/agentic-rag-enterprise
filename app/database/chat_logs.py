import json
import os
from datetime import datetime

FILE_PATH = "app/database/chat_logs.json"


def save_chat(username, question, answer):

    if not os.path.exists(FILE_PATH):

        with open(FILE_PATH, "w") as f:

            json.dump(
                {"chats": []},
                f,
                indent=4
            )

    with open(FILE_PATH, "r") as f:

        data = json.load(f)

    data["chats"].append({

        "username": username,
        "question": question,
        "answer": answer,
        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    })

    with open(FILE_PATH, "w") as f:

        json.dump(
            data,
            f,
            indent=4
        )


def get_chats():

    if not os.path.exists(FILE_PATH):

        return []

    with open(FILE_PATH, "r") as f:

        data = json.load(f)

    return data["chats"]