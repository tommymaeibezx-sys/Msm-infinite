import socket
import json
from router import route

HOST = "0.0.0.0"
PORT = 9933

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("MSM PRO SERVER ONLINE")

def send(client, data):
    client.send((json.dumps(data) + "\n").encode())

while True:
    client, addr = server.accept()
    print("Cliente:", addr)

    while True:
        try:
            raw = client.recv(4096)
            if not raw:
                break

            request = json.loads(raw.decode())
            response = route(request)

            send(client, response)

        except Exception as e:
            print("ERROR:", e)
            break

    client.close()
