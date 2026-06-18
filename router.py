from multiplayer import get_online_players

def route(req, user_id):
    cmd = req.get("_cmd")

    if cmd == "get_online":
        return {
            "_cmd": "get_online",
            "players": get_online_players()
        }

    if cmd == "visit_island":
        target = req.get("target_id")

        return {
            "_cmd": "visit_island",
            "target_id": target
        }

    return {
        "_cmd": cmd,
        "status": "ok"
    }
