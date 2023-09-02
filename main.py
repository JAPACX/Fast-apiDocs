from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# routes
from api.routers.items import items_router

app = FastAPI()
app.title = "My app with FastAPI"
app.version = "0.0.1"

app.include_router(items_router)


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Fast API Project</h1>')
