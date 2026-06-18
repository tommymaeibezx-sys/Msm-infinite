import socket
import json
from handlers import handle_request

HOST = "0.0.0.0"
PORT = 9933

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Servidor MSM corriendo en puerto", PORT)

def send(client, data):
    packet = json.dumps(data).encode()
    client.send(packet)

while True:
    client, addr = server.accept()
    print("Cliente conectado:", addr)

    while True:
        try:
            data = client.recv(4096)
            if not data:
                break

            request = json.loads(data.decode())
            cmd = request.get("_cmd")

            response = handle_request(cmd, request)

            send(client, response)

        except Exception as e:
            print("Error:", e)
            break

    client.close() 
