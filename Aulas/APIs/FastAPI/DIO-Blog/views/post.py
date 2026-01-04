from datetime import datetime

from pydantic import BaseModel

class PostOut(BaseModel):
    tittle: str
    date: datetime