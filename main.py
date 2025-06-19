from fastapi import FastAPI
import json
import os

app = FastAPI()
DATA_DIR = "./data"

@app.get("/restaurants")
def list_restaurants():
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".json")]
    return [f.replace(".json", "") for f in files]

@app.get("/restaurants/{restaurant_id}")
def get_restaurant_data(restaurant_id: str):
    path = os.path.join(DATA_DIR, f"{restaurant_id}.json")
    if not os.path.exists(path):
        return {"error": "Restaurant not found"}
    with open(path) as f:
        return json.load(f)
