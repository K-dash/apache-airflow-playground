from pydantic import BaseModel
from typing import Optional

class BasicSettings(BaseModel):
    id: int
    name: str
    age: Optional[int]
    email: Optional[str]
