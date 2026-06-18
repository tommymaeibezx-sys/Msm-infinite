@server.event("login")
def on_login(client, data):
    return {
        "status": "OK",
        "data": {
            "user_id": 1,
            "name": "player",
            "level": 10
        }
    }
