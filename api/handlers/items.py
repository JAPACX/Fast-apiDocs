# api/handlers/items.py

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}
