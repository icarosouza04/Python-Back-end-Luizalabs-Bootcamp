from fastapi import APIRouter
from Aulas.APIs.FastAPI.Desafio.atleta.controller import router as atleta

api_router = APIRouter()
api_router.include_router(atleta, prefix = "/atletas", tags = ["atletas"])