from pyfox2x.server import Server

server = Server()

@server.event("login")
def on_login(client, data):
    return {
        "status": "ok",
        "user_id": 1
    }

server.start(port=9933)
