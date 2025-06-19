from fastapi import FastAPI
import os, json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Meal Map API is live"}

@app.get("/restaurants")
def list_restaurants():
    return [f.split(".")[0] for f in os.listdir("data") if f.endswith(".json")]

@app.get("/restaurants/{restaurant_id}")
def get_restaurant(restaurant_id: str):
    path = f"data/{restaurant_id}.json"
    if not os.path.exists(path):
        return {"error": "Not found"}
    with open(path) as f:
        return json.load(f)
