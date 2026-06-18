from multiplayer import get_online_players
import json

ISLANDS_FILE = "database/islands.json"

def load_all():
    with open(ISLANDS_FILE) as f:
        return json.load(f)

def save_all(data):
    with open(ISLANDS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def route(req, user_id):
    cmd = req.get("_cmd")

    # 🌐 ONLINE
    if cmd == "get_online":
        return {
            "_cmd": "get_online",
            "players": get_online_players()
        }

    # 🏝️ MI ISLA
    if cmd == "get_island":
        data = load_all()
        island = data["islands"].get(str(user_id))

        return {
            "_cmd": "get_island",
            "island": island
        }

    # 🏝️ VISITAR
    if cmd == "visit_island":
        target = str(req.get("target_id"))

        data = load_all()
        island = data["islands"].get(target)

        return {
            "_cmd": "visit_island",
            "island": island
        }

    # 🧱 COLOCAR MONSTRUO
    if cmd == "place_monster":
        data = load_all()
        island = data["islands"][str(user_id)]

        island["monsters"].append(req.get("monster"))

        save_all(data)

        return {
            "_cmd": "place_monster",
            "status": "ok"
        }

    return {
        "_cmd": cmd,
        "status": "ok"
    }
