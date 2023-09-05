from fastapi import APIRouter

from api.handlers import handler_users
from api.schemas.schema_users import UserModel

users_router = APIRouter()


@users_router.get('/users')  # --> Optional Query's
def get_list_users_route():
    return handler_users.get_list_users()


@users_router.get('/users/{user_id}')  # --> Optional Query's
def get_list_users_route(user_id: int):
    return handler_users.get_user_by_id(user_id)


@users_router.post('/users/')  # --> Body
def get_list_users_route(new_user: UserModel):
    return handler_users.create_user(new_user)


@users_router.put('/users/{user_id}')  # --> Optional Query's
def update_user_by_id_route(user_id: int, new_data: UserModel):
    return handler_users.update_user_by_id(user_id, new_data)


@users_router.delete('/users/{user_id}')  # --> Optional Query's
def delete_user_by_id_route(user_id: int):
    return handler_users.delete_user_by_id(user_id)
