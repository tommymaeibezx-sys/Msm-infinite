import time
from systems import breeding, structures, baking

from utils import load_player, save_player

def route(req):
    cmd = req.get("_cmd")
    player = load_player()

    # INIT
    if cmd == "gs_initialized":
        return {
            "_cmd": "gs_initialized",
            "server_time": int(time.time())
        }

    # DB SYNC
    if cmd.startswith("db_"):
        return handle_db(cmd, player)

    # SYSTEMS
    if cmd.startswith("gs_breed"):
        return breeding.start(player, req)

    if cmd == "gs_finish_breeding":
        return breeding.finish(player)

    if cmd == "gs_hatch_egg":
        return breeding.hatch(player)

    if cmd == "gs_buy_structure":
        return structures.buy(player, req)

    if cmd == "gs_collect_rewards":
        player["currencies"]["coins"] += 500
        save_player(player)

        return {
            "_cmd": "gs_update_properties",
            "currencies": player["currencies"]
        }

    return {"_cmd": cmd, "ok": True}


def handle_db(cmd, player):
    return {
        "_cmd": cmd,
        "data": player.get(cmd.replace("db_", ""), {})
    }
