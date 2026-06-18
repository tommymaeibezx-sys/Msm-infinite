import time
import random

MAX_PLAYERS = 40
TIMEOUT = 240  # 4 minutos

sessions = {}

def generate_id():
    return random.randint(100000, 999999)


def create_guest():
    if len(sessions) >= MAX_PLAYERS:
        return None

    user_id = generate_id()

    sessions[user_id] = {
        "user_id": user_id,
        "last_active": time.time()
    }

    return sessions[user_id]


def update_activity(user_id):
    if user_id in sessions:
        sessions[user_id]["last_active"] = time.time()


def remove_inactive():
    now = time.time()
    to_delete = []

    for uid, session in sessions.items():
        if now - session["last_active"] > TIMEOUT:
            to_delete.append(uid)

    for uid in to_delete:
        del sessions[uid]


def is_full():
    return len(sessions) >= MAX_PLAYERS
