import time
from utils import load_player, save_player
from systems import breeding, baking, structures, battle

def route(req):
    cmd = req.get("_cmd")
    player = load_player()

    # INIT
    if cmd == "gs_initialized":
        return {
            "_cmd": "gs_initialized",
            "server_time": int(time.time())
        }

    # =====================
    # DATABASE (db_*)
    # =====================
    if cmd == "db_monster":
        return {"_cmd": cmd, "data": player["monsters"]}

    if cmd == "db_structure":
        return {"_cmd": cmd, "data": player["structures"]}

    if cmd == "db_island":
        return {"_cmd": cmd, "data": player["islands"]}

    if cmd == "db_battle":
        return {"_cmd": cmd, "data": player["battle"]}

    # =====================
    # BREEDING
    # =====================
    if cmd == "gs_breed_monsters":
        return breeding.start(player, req)

    if cmd == "gs_finish_breeding":
        return breeding.finish(player)

    if cmd == "gs_hatch_egg":
        return breeding.hatch(player)

    # =====================
    # BAKING
    # =====================
    if cmd == "gs_start_baking":
        return baking.start(player)

    if cmd == "gs_finish_baking":
        return baking.finish(player)

    # =====================
    # STRUCTURES
    # =====================
    if cmd == "gs_buy_structure":
        return structures.buy(player, req)

    if cmd == "gs_move_structure":
        return structures.move(player, req)

    # =====================
    # REWARDS
    # =====================
    if cmd == "gs_collect_rewards":
        player["currencies"]["coins"] += 1000
        save_player(player)

        return {
            "_cmd": "gs_update_properties",
            "currencies": player["currencies"]
        }

    # =====================
    # MONSTER UPDATE
    # =====================
    if cmd == "gs_update_monster":
        save_player(player)
        return {"_cmd": cmd, "status": "ok"}

    # DEFAULT
    return {"_cmd": cmd, "status": "ok"}
