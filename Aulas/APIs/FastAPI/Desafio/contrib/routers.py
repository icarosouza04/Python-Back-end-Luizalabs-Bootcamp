from fastapi import APIRouter
from Aulas.APIs.FastAPI.Desafio.atleta.controller import router as atleta
from Aulas.APIs.FastAPI.Desafio.categorias.controller import router as categorias

api_router = APIRouter()
api_router.include_router(atleta, prefix = "/atletas", tags = ["atletas"])
api_router.include_router(categorias, prefix = "/categorias", tags = ["categorias"])