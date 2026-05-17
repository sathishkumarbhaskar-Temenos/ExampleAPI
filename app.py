from fastapi import FastAPI
from enum import Enum
app = FastAPI()
@app.get("/hello/{name}")
async def hello(name):
    return f"Welcome {name}"
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = "Welcome Apple....!!!"):
    return {"item_id": item_id, "q": q}