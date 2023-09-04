from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND

# models
from api.config.db import conn
from api.models.model_movies import movies


def get_list_movies(genre=None):
    #
    query = movies.select()

    if genre:
        query = query.where(movies.c.genre == genre)

    result = conn.execute(query).fetchall()

    movie_list = []
    for element in result:
        movie_dict = {
            'id': element.id,
            'title': element.title,
            'description': element.description,
            'rating': element.rating,
            'genre': element.genre
        }
        movie_list.append(movie_dict)

    return movie_list


def get_movie_info_by_id(movie_id: int):
    query = movies.select().where(movies.c.id == movie_id)
    result = conn.execute(query).fetchone()
    if result is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Id not found")
    id, title, description, rating = result
    movie_info = {
        'id': id,
        'title': title,
        'description': description,
        'rating': rating
    }

    return movie_info


def create_new_movie(new_movie):
    insert_new_movie = movies.insert().values(title=new_movie.title, description=new_movie.description,
                                              rating=new_movie.rating, genre=new_movie.genre)
    conn.execute(insert_new_movie)
    conn.commit()
    return new_movie


def update_movie_by_id(movie_id, new_data):
    new_info_movie = {
        'title': new_data.title,
        'description': new_data.description,
        'rating': new_data.rating
    }
    update_query = (
        movies
        .update()
        .where(movies.c.id == movie_id)
        .values(new_info_movie)
        .returning(movies)
    )
    result = conn.execute(update_query).fetchone()
    if result is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Movie not found")
    conn.commit()
    return {"message": f"Movie {result[1]} updated"}


def delete_movie_by_id(movie_id: int):
    query = movies.select().where(movies.c.id == movie_id)
    result = conn.execute(query).fetchone()
    if result is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Movie not found")

    delete_query = movies.delete().where(movies.c.id == movie_id)
    conn.execute(delete_query)
    conn.commit()

    return {"message": f"Movie {result[1]} with ID {movie_id}  deleted"}
