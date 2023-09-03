from typing import Optional

from pydantic import BaseModel


class MovieModel(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    rating: Optional[float] = None
