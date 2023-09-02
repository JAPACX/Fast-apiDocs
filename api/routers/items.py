# api/routers/items.py
from fastapi import APIRouter

items_router = APIRouter()


@items_router.get('/items')
def get_items():
    return {'message': 'items router correctly'}
