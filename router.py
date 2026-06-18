import time
from utils import load_player, save_player
from systems import breeding, baking, structures
from auto_handler import auto_handle

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
    # SISTEMAS REALES
    # =====================

    if cmd == "gs_breed_monsters":
        return breeding.start(player, req)

    if cmd == "gs_finish_breeding":
        return breeding.finish(player)

    if cmd == "gs_hatch_egg":
        return breeding.hatch(player)

    if cmd == "gs_start_baking":
        return baking.start(player)

    if cmd == "gs_finish_baking":
        return baking.finish(player)

    if cmd == "gs_buy_structure":
        return structures.buy(player, req)

    # =====================
    # AUTO HANDLER (MAGIA)
    # =====================

    return auto_handle(cmd, req, player)
