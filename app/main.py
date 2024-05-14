from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World11123123123111"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/random_wep")
def get_medieval_weapons():
    weapons = [
        {"name": "Longsword", "type": "Sword", "origin": "Europe"},
        {"name": "Katana", "type": "Sword", "origin": "Japan"},
        {"name": "Halberd", "type": "Polearm", "origin": "Europe"},
        {"name": "Crossbow", "type": "Ranged Weapon", "origin": "Europe"}
    ]
    return {"medieval_weapons": weapons}
