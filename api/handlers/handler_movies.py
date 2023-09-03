from fastapi import HTTPException


def get_list_movies(genre: str):
    if genre:
        return {"message": f"Movies about {genre}"}
    return {"message": "all information about Movies"}


def get_movie_info_by_id(movie_id: int):
    if 0 < movie_id < 1000:
        return {'message': f'Id is {movie_id}'}
    else:
        raise HTTPException(status_code=404, detail="Out of range 1 - 1000")


def create_new_movie(new_movie):
    return {"message": f"Movie {new_movie.title} {new_movie.id} created success"}
