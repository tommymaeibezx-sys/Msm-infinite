import time
from utils import save_player

def start(player):
    player["baking"] = {
        "end_time": time.time() + 30
    }

    save_player(player)
    return {"_cmd": "gs_start_baking"}


def finish(player):
    if time.time() < player["baking"]["end_time"]:
        return {"error": "wait"}

    player["currencies"]["food"] += 200
    player["baking"] = None

    save_player(player)
    return {"_cmd": "gs_finish_baking"}
