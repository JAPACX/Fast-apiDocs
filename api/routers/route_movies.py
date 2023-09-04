from fastapi import APIRouter

from api.handlers import handler_movies
from api.schemas import schema_movies

movies_router = APIRouter()


@movies_router.get('/movies')  # --> Optional Query's
def get_list_movies_route(genre: str = None):
    return handler_movies.get_list_movies(genre)


@movies_router.get('/movies/{movie_id}')  # --> Obligatory Path Parameter
def get_movie_info_by_id_route(movie_id: int):
    return handler_movies.get_movie_info_by_id(movie_id)


@movies_router.post("/movies/")  # --> Body request, the optional parameters is in Model
def create_new_movie_route(new_movie: schema_movies.MovieModel):
    return handler_movies.create_new_movie(new_movie)


@movies_router.put("/movies/{movie_id}")  # --> Body request, the optional parameters is in Model
def update_movie_by_id_router(movie_id: int, new_data: schema_movies.MovieModel):
    return handler_movies.update_movie_by_id(movie_id, new_data)


@movies_router.delete("/movies/{movie_id}")  # --> Obligatory Path Parameter
def create_new_movie_route(movie_id):
    return handler_movies.delete_movie_by_id(movie_id)
