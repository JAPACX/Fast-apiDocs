from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str
    phone: str
