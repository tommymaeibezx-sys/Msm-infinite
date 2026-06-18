import time
from utils import save_player

def auto_handle(cmd, req, player):

    # =========================
    # 🧱 DATABASE (db_*)
    # =========================
    if cmd.startswith("db_"):
        key = cmd.replace("db_", "")

        return {
            "_cmd": cmd,
            "data": player.get(key, {})
        }

    # =========================
    # 🎮 GAME SYSTEM (gs_*)
    # =========================
    if cmd.startswith("gs_"):

        # 🪙 monedas genéricas
        if "collect" in cmd:
            player["currencies"]["coins"] += 500
            save_player(player)

            return {
                "_cmd": "gs_update_properties",
                "currencies": player["currencies"]
            }

        # 🏗️ estructuras
        if "structure" in cmd:
            return {
                "_cmd": "gs_update_structure",
                "status": "ok"
            }

        # 🧬 monstruos
        if "monster" in cmd:
            return {
                "_cmd": "gs_update_monster",
                "status": "ok"
            }

        # 🥚 huevos
        if "egg" in cmd:
            return {
                "_cmd": cmd,
                "status": "egg_ok"
            }

        # 🏝️ islas
        if "island" in cmd:
            return {
                "_cmd": cmd,
                "status": "island_ok"
            }

        # 📩 mensajes
        if "message" in cmd:
            return {
                "_cmd": cmd,
                "messages": player.get("messages", [])
            }

        # 🔥 antorchas
        if "torch" in cmd:
            return {
                "_cmd": cmd,
                "torches": player.get("torches", [])
            }

        # 👥 amigos
        if "friend" in cmd:
            return {
                "_cmd": cmd,
                "friends": player.get("friends", [])
            }

        # ⏱️ speed up
        if "speed_up" in cmd:
            return {
                "_cmd": cmd,
                "status": "instant"
            }

        # DEFAULT gs
        return {
            "_cmd": cmd,
            "status": "ok"
        }

    # =========================
    # ⚔️ BATTLE SYSTEM
    # =========================
    if cmd.startswith("battle_"):
        return {
            "_cmd": cmd,
            "battle": player.get("battle", {})
        }

    # =========================
    # 🧠 FALLBACK GLOBAL
    # =========================
    return {
        "_cmd": cmd,
        "status": "unknown_ok"
      } 
