import socket
import json
import threading

from router import route
from session_manager import create_session, update_activity, remove_inactive, is_full
from account_manager import create_account, load_account
from multiplayer import player_join, player_leave

HOST = "0.0.0.0"
PORT = 9933

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("MSM PRO MAX SERVER ONLINE")

def send(client, data):
    client.send((json.dumps(data) + "\n").encode())

def cleanup():
    while True:
        remove_inactive()

threading.Thread(target=cleanup, daemon=True).start()

while True:
    client, addr = server.accept()
    print("Nueva conexión:", addr)

    if is_full():
        send(client, {"error": "server_full"})
        client.close()
        continue

    user_id = None

    try:
        # 📥 PRIMER MENSAJE = LOGIN
        raw = client.recv(4096)
        data = json.loads(raw.decode())

        if data["_cmd"] == "login":
            user_id = data.get("user_id")

            account = load_account(user_id)

            if not account:
                account = create_account()
                user_id = account["user_id"]

        else:
            account = create_account()
            user_id = account["user_id"]

        create_session(user_id)
        player_join(user_id)

        send(client, {
            "_cmd": "login_ok",
            "user_id": user_id
        })

        # 🔁 LOOP
        while True:
            raw = client.recv(4096)
            if not raw:
                break

            req = json.loads(raw.decode())

            update_activity(user_id)

            res = route(req, user_id)

            send(client, res)

    except Exception as e:
        print("ERROR:", e)

    finally:
        print("Desconectado:", user_id)
        player_leave(user_id)
        client.close()
