from fastapi import status, APIRouter
from schemas.post import PostIn
from views.post import PostOut
from Aulas.APIs.FastAPI.DIO_Blog.models.post import posts
from Aulas.APIs.FastAPI.DIO_Blog.database import database

router = APIRouter(prefix = "/posts")

@router.get("/", response_model = list[PostOut])
async def read_posts(published: bool, limit: int, skip: int = 0):
    query = posts.select()
    return await database.fetch_all(query)


@router.post("/", status_code = status.HTTP_201_CREATED, response_model = PostOut)
def creat_post(post: PostIn):
    comand = posts.inset().values(
    title = post.title,
    content = post.content, 
    published_at = post.published_at
    )
    return post


