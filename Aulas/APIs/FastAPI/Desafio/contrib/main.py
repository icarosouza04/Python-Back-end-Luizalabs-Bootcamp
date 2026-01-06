from fastapi import FastAPI
from Aulas.APIs.FastAPI.Desafio.contrib.routers import api_router

app = FastAPI(title = "Desafio")
app.include_router(api_router)