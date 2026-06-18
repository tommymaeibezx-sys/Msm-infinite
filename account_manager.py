import json
import os
import random

DB_PATH = "database/players/"

def generate_id():
    return random.randint(100000, 999999)

def player_file(user_id):
    return os.path.join(DB_PATH, f"{user_id}.json")

def create_account():
    user_id = generate_id()

    data = {
        "user_id": user_id,
        "name": f"Guest{user_id}",
        "coins": 100,
        "island": []
    }

    save_account(user_id, data)
    return data

def load_account(user_id):
    try:
        with open(player_file(user_id)) as f:
            return json.load(f)
    except:
        return None

def save_account(user_id, data):
    with open(player_file(user_id), "w") as f:
        json.dump(data, f, indent=4)
