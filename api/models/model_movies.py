from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float

from api.config.db import meta, engine

movies = Table("movies", meta, Column("id", Integer, primary_key=True), Column("title", String(255)),
               Column("description", String(255)), Column("rating", Float), Column("genre", String))

meta.create_all(engine)
