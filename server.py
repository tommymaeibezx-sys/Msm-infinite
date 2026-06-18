import socket
import json
import threading
from router import route
from session_manager import create_guest, update_activity, remove_inactive, is_full

HOST = "0.0.0.0"
PORT = 9933

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("MSM SERVER PRO + ONLINE")

def send(client, data):
    client.send((json.dumps(data) + "\n").encode())

def cleanup_loop():
    while True:
        remove_inactive()

threading.Thread(target=cleanup_loop, daemon=True).start()

while True:
    client, addr = server.accept()
    print("Conexión:", addr)

    # 👤 CREAR GUEST AUTOMÁTICO
    if is_full():
        send(client, {"error": "server_full"})
        client.close()
        continue

    session = create_guest()
    user_id = session["user_id"]

    send(client, {
        "_cmd": "guest_login",
        "user_id": user_id
    })

    while True:
        try:
            raw = client.recv(4096)
            if not raw:
                break

            request = json.loads(raw.decode())

            # 🔄 actualizar actividad
            update_activity(user_id)

            response = route(request)

            # incluir user_id siempre
            response["user_id"] = user_id

            send(client, response)

        except Exception as e:
            print("ERROR:", e)
            break

    print("Jugador desconectado:", user_id)
    client.close()
