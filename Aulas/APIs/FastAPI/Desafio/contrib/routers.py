from fastapi import APIRouter
from Aulas.APIs.FastAPI.Desafio.atleta.controller import router as atleta
from Aulas.APIs.FastAPI.Desafio.categorias.controller import router as categorias
from Aulas.APIs.FastAPI.Desafio.centro_treinamento.controller import router as centro_treinamento

api_router = APIRouter()
api_router.include_router(atleta, prefix = "/atletas", tags = ["atletas"])
api_router.include_router(categorias, prefix = "/categorias", tags = ["categorias"])
api_router.include_router(centro_treinamento, prefix = "/centros_treinamento", tags = ["centros_treinamento"])