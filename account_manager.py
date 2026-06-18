import json
import os
import random

DB_PATH = "database/players/"
ISLANDS_FILE = "database/islands.json"

def generate_id():
    return random.randint(100000, 999999)

def player_file(user_id):
    return os.path.join(DB_PATH, f"{user_id}.json")

def load_islands():
    with open(ISLANDS_FILE) as f:
        return json.load(f)

def save_islands(data):
    with open(ISLANDS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def create_island(user_id):
    data = load_islands()

    data["islands"][str(user_id)] = {
        "user_id": user_id,
        "island_name": "Mi Isla",
        "level": 1,
        "coins": 100,
        "food": 50,
        "diamonds": 5,

        "monsters": [
            {
                "monster_id": 1,
                "type": "noggin",
                "x": 100,
                "y": 200,
                "level": 1,
                "happiness": 100
            }
        ],

        "structures": [
            {
                "structure_id": 1,
                "type": "castle",
                "x": 0,
                "y": 0,
                "level": 1
            }
        ],

        "decorations": [],

        "torches": [
            {
                "torch_id": 1,
                "active": False,
                "friend_id": None
            }
        ]
    }

    save_islands(data)

def create_account():
    user_id = generate_id()

    data = {
        "user_id": user_id,
        "name": f"Guest{user_id}",
        "coins": 100
    }

    with open(player_file(user_id), "w") as f:
        json.dump(data, f, indent=4)

    create_island(user_id)

    return data

def load_account(user_id):
    try:
        with open(player_file(user_id)) as f:
            return json.load(f)
    except:
        return None
