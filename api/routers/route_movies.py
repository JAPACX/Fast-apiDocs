from typing import Union

from fastapi import APIRouter

# handlers
from api.handlers import handler_movies
# models
from api.models.model_movie import MovieModel

movies_router = APIRouter()


@movies_router.get('/movies')  # --> Optional Query's
def get_list_movies_route(genre: Union[str, None] = None):
    return handler_movies.get_list_movies(genre)


@movies_router.get('/movies/{movie_id}')  # --> Obligatory Path Parameter
def get_movie_info_by_id_route(movie_id: int):
    return handler_movies.get_movie_info_by_id(movie_id)


@movies_router.post("/movies/")  # --> Body request, the optional parameters is in Model
def create_new_movie_route(new_movie: MovieModel):
    return handler_movies.create_new_movie(new_movie)
