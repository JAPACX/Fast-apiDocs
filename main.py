from fastapi import FastAPI


# add routes
from api.routers.route_movies import movies_router
from api.routers.route_users import users_router

app = FastAPI()
app.title = "My app with FastAPI"
app.version = "0.0.1"

app.include_router(movies_router, tags=['Movies'])
app.include_router(users_router, tags=['Users'])


@app.get('/', tags=['Home'])
def welcome():
    return {"message": "Welcome to my API"}


