import time

MAX_PLAYERS = 40
TIMEOUT = 240

sessions = {}

def create_session(user_id):
    if len(sessions) >= MAX_PLAYERS:
        return None

    sessions[user_id] = {"last_active": time.time()}
    return sessions[user_id]

def update_activity(user_id):
    if user_id in sessions:
        sessions[user_id]["last_active"] = time.time()

def remove_inactive():
    now = time.time()
    to_delete = []

    for uid, s in sessions.items():
        if now - s["last_active"] > TIMEOUT:
            to_delete.append(uid)

    for uid in to_delete:
        del sessions[uid]

def is_full():
    return len(sessions) >= MAX_PLAYERS
