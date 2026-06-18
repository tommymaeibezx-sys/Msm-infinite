players_online = {}

def player_join(user_id):
    players_online[user_id] = {
        "user_id": user_id
    }

def player_leave(user_id):
    if user_id in players_online:
        del players_online[user_id]

def get_online_players():
    return list(players_online.values()) 
