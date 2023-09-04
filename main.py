from fastapi import FastAPI


# add routes
from api.routers.route_movies import movies_router

app = FastAPI()
app.title = "My app with FastAPI"
app.version = "0.0.1"

app.include_router(movies_router, tags=['Movies'])


@app.get('/', tags=['Home'])
def welcome():
    return {"message": "Welcome to my API"}


