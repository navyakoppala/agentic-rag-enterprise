import json
import os


CHAT_FILE = "chat_history.json"


def save_chat(
    document_name,
    messages
):

    data = {}

    if os.path.exists(
        CHAT_FILE
    ):

        with open(
            CHAT_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            try:

                data = json.load(f)

            except:

                data = {}

    data[document_name] = messages

    with open(
        CHAT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


def load_chat(
    document_name
):

    if not os.path.exists(
        CHAT_FILE
    ):

        return []

    with open(
        CHAT_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        try:

            data = json.load(f)

        except:

            return []

    return data.get(
        document_name,
        []
    )