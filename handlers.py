import json
import time

def load_player():
    with open("database/player.json") as f:
        return json.load(f)

def save_player(data):
    with open("database/player.json", "w") as f:
        json.dump(data, f, indent=4)

def handle_request(cmd, data):
    player = load_player()

    # INIT
    if cmd == "gs_initialized":
        return {
            "_cmd": "gs_initialized",
            "server_time": int(time.time())
        }

    # DATABASE SYNC
    if cmd == "db_island":
        return {"_cmd": "db_island", "data": player["islands"]}

    if cmd == "db_monster":
        return {"_cmd": "db_monster", "data": player["monsters"]}

    if cmd == "db_structure":
        return {"_cmd": "db_structure", "data": player["structures"]}

    # MONSTERS
    if cmd == "gs_hatch_egg":
        new_monster = {
            "id": len(player["monsters"]) + 1,
            "type": "noggin",
            "level": 1
        }
        player["monsters"].append(new_monster)
        save_player(player)

        return {"_cmd": "gs_update_monster", "monster": new_monster}

    # BUILDINGS
    if cmd == "gs_buy_structure":
        structure = {
            "id": len(player["structures"]) + 1,
            "type": "nursery"
        }
        player["structures"].append(structure)
        save_player(player)

        return {"_cmd": "gs_update_structure", "structure": structure}

    # REWARDS
    if cmd == "gs_collect_rewards":
        player["currencies"]["coins"] += 1000
        save_player(player)

        return {
            "_cmd": "gs_update_properties",
            "currencies": player["currencies"]
        }

    # DEFAULT
    return {"_cmd": cmd, "status": "ok"}
