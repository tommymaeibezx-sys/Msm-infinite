from utils import save_player

def buy(player, req):
    structure = {
        "id": len(player["structures"]) + 1,
        "type": req.get("type", "nursery"),
        "level": 1
    }

    player["structures"].append(structure)
    save_player(player)

    return {"_cmd": "gs_update_structure", "structure": structure}
