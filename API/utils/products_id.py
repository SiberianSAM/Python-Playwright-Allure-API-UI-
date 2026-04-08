import json
import os

ID_FILE = "Study_project/current_products_id.json"

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