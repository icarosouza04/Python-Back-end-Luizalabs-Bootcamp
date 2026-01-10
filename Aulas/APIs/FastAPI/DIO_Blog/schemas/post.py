from datetime import datetime

from pydantic import BaseModel

class PostIn(BaseModel):
    tittle: str
    content: str
    published_at: datetime | None = None
    published: bool = False
