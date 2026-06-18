import json

def load_player():
    with open("database/player.json") as f:
        return json.load(f)

def save_player(data):
    with open("database/player.json", "w") as f:
        json.dump(data, f, indent=4)
