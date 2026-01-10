from datetime import datetime

from pydantic import BaseModel

class PostOut(BaseModel):
    tittle: str
    content: str
    published_at: datetime | None
    date: datetime