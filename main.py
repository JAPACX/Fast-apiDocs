from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# new this
from api.models.model_user import UserConnection
# add routes
from api.routers.route_movies import movies_router
from api.schema.user_schema import UserSchema

app = FastAPI()
connect = UserConnection()
app.title = "My app with FastAPI"
app.version = "0.0.1"

app.include_router(movies_router, tags=['Movies'])


@app.get('/', tags=['Home'])
def message():
    connect
    return HTMLResponse('<h1>Fast API Project</h1>')


@app.post("/api/insert", tags=['New Tutorial'])
def insert(user_data: UserSchema):
    print(user_data)
    return user_data
