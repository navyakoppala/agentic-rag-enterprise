import json
import os

FILE_PATH = "app/database/analytics.json"


def get_analytics():

    if not os.path.exists(FILE_PATH):

        return {
            "total_users": 0,
            "total_questions": 0,
            "total_uploads": 0
        }

    with open(FILE_PATH, "r") as f:
        return json.load(f)


def save_analytics(data):

    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)


def increment_users():

    data = get_analytics()
    data["total_users"] += 1
    save_analytics(data)


def increment_questions():

    data = get_analytics()
    data["total_questions"] += 1
    save_analytics(data)


def increment_uploads():

    data = get_analytics()
    data["total_uploads"] += 1
    save_analytics(data)