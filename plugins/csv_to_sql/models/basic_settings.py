from typing import Optional

from pydantic import BaseModel


class BasicSettings(BaseModel):
    id: int
    name: str
    age: Optional[int]
    email: Optional[str]
