from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: str
    title: str
    author: str
    description: str
    image_url: Optional[str] = None
