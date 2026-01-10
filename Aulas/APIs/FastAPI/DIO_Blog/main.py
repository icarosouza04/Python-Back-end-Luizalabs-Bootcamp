from fastapi import FastAPI
from controllers import post  
from contextlib import asynccontextmanager
from Aulas.APIs.FastAPI.DIO_Blog.database import database, metadata, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    from Aulas.APIs.FastAPI.DIO_Blog.models.post import posts # noqa

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(lifespan = None)
app.include_router(post.router)

