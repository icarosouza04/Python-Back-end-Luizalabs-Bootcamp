from fastapi import Depends, status, APIRouter
from Aulas.APIs.FastAPI.DIO_Blog.security import login_required
from Aulas.APIs.FastAPI.DIO_Blog.services.post import PostService
from Aulas.APIs.FastAPI.DIO_Blog.schemas.post import PostIn, PostUpdateIn
from Aulas.APIs.FastAPI.DIO_Blog.views.post import PostOut
from Aulas.APIs.FastAPI.DIO_Blog.models.post import posts
from Aulas.APIs.FastAPI.DIO_Blog.database import database

router = APIRouter(prefix = "/posts", dependencies = [Depends(login_required)])

service = PostService()

@router.get("/", response_model = list[PostOut])
async def read_posts(published: bool, limit: int, skip: int = 0):
    return await service.read_all(published = published, limit = limit, skip = skip)


@router.post("/", status_code = status.HTTP_201_CREATED, response_model = PostOut)
async def creat_post(post: PostIn):
    return {**post.model_dump(), "id": await service.create(post)}


@router.get("/{id}", response_model = PostOut)
async def read_post(id: int):
    return await service.read(id)


@router.patch("/{id}", response_model = PostOut)
async def update_post(id: int, post: PostUpdateIn):
    return await service.update(id = id, post = post)
    

@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT, response_model = None)
async def delete_post(id: int):
    await service.delete(id)