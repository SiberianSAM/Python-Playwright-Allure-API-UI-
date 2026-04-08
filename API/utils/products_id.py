import json
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
ID_FILE = PROJECT_ROOT / "token.json"

def save_id(first_prod_id):
    with open(ID_FILE, "w") as f:
        json.dump({"product_id":first_prod_id}, f)
    print(f"ID сохранен в {ID_FILE}")


def load_id():
    if not os.path.exists(ID_FILE):
        return None

    with open(ID_FILE, "r") as f:
        data = json.load(f)
        return data.get("product_id")