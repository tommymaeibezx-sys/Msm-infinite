def handle_account(req, user_id):
    return {
        "_cmd": "account",
        "user_id": user_id
    }
