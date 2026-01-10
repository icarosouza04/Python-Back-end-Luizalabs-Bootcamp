from fastapi import APIRouter

from Aulas.APIs.FastAPI.DIO_Blog.schemas.auth import LoginIn
from Aulas.APIs.FastAPI.DIO_Blog.security import sign_jwt
from Aulas.APIs.FastAPI.DIO_Blog.views.auth import LoginOut

router = APIRouter(prefix = "/auth", tags = ["auth"])

@router.post("/login", response_model = LoginOut)
async def login(data: LoginIn):
    return sign_jwt(user_id = data.user_id)