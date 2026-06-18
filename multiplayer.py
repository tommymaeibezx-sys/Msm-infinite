players_online = {}

def player_join(user_id):
    players_online[user_id] = {"user_id": user_id}

def player_leave(user_id):
    players_online.pop(user_id, None)

def get_online_players():
    return list(players_online.values())
