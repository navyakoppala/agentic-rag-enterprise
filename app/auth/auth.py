import json
import os

USERS_FILE = "app/auth/users.json"


def load_users():

    if not os.path.exists(USERS_FILE):

        default_users = {
            "admin": {
                "password": "admin123",
                "role": "admin"
            }
        }

        with open(
            USERS_FILE,
            "w"
        ) as f:

            json.dump(
                default_users,
                f,
                indent=4
            )

    with open(
        USERS_FILE,
        "r"
    ) as f:

        return json.load(f)


def save_users(users):

    with open(
        USERS_FILE,
        "w"
    ) as f:

        json.dump(
            users,
            f,
            indent=4
        )


def create_user(
    username,
    password
):

    users = load_users()

    if username in users:
        return False

    users[username] = {
        "password": password,
        "role": "user"
    }

    save_users(users)

    return True


def authenticate(
    username,
    password
):

    users = load_users()

    return (
        username in users
        and users[username]["password"] == password
    )


def get_role(username):

    users = load_users()

    if username in users:
        return users[username]["role"]

    return "user"