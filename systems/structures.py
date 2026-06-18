from utils import save_player

def buy(player, req):
    structure = {
        "id": len(player["structures"]) + 1,
        "type": req.get("type", "nursery"),
        "x": 0,
        "y": 0
    }

    player["structures"].append(structure)
    save_player(player)

    return {"_cmd": "gs_update_structure", "structure": structure}


def move(player, req):
    sid = req.get("id")

    for s in player["structures"]:
        if s["id"] == sid:
            s["x"] = req.get("x")
            s["y"] = req.get("y")

    save_player(player)
    return {"_cmd": "gs_move_structure"}
