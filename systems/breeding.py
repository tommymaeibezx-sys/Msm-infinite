import time
from utils import save_player

BREED_TIME = 30  # segundos

def start(player, req):
    m1 = req.get("parent_1")
    m2 = req.get("parent_2")

    player["breeding"] = {
        "parent_1": m1,
        "parent_2": m2,
        "end_time": time.time() + BREED_TIME
    }

    save_player(player)

    return {"_cmd": "gs_breed_monsters", "status": "started"}


def finish(player):
    if time.time() < player["breeding"]["end_time"]:
        return {"error": "not_ready"}

    egg = {
        "id": len(player["eggs"]) + 1,
        "type": "noggin"
    }

    player["eggs"].append(egg)
    player["breeding"] = None

    save_player(player)

    return {"_cmd": "gs_finish_breeding", "egg": egg}


def hatch(player):
    if not player["eggs"]:
        return {"error": "no_egg"}

    egg = player["eggs"].pop(0)

    monster = {
        "id": len(player["monsters"]) + 1,
        "type": egg["type"],
        "level": 1,
        "happiness": 100
    }

    player["monsters"].append(monster)
    save_player(player)

    return {"_cmd": "gs_update_monster", "monster": monster}
