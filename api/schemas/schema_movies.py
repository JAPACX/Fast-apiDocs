from typing import Optional

from pydantic import BaseModel


class MovieModel(BaseModel):
    title: str
    description: Optional[str] = None
    rating: Optional[float] = None
    genre: Optional[str] = None
