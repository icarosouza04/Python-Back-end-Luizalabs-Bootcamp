from pydantic import AwareDatetime, BaseModel

class PostOut(BaseModel):
    id: int
    tittle: str
    content: str
    published_at: AwareDatetime | None
