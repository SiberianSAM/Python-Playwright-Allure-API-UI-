import json
import os

TOKEN_FILE = "Study_project/token.json"

def save_token(token):
    with open(TOKEN_FILE, "w") as f:
        json.dump({"token": token}, f)
    print(f"Токен сохранен в {TOKEN_FILE}")


def load_token():
    if not os.path.exists(TOKEN_FILE):
        return None

    with open(TOKEN_FILE, "r") as f:
        data = json.load(f)
        return data.get("token")