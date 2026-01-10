from fastapi import FastAPI
from Aulas.APIs.FastAPI.DIO_Blog.controllers import auth, post
from contextlib import asynccontextmanager
from Aulas.APIs.FastAPI.DIO_Blog.database import database, metadata, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    from Aulas.APIs.FastAPI.DIO_Blog.models.post import posts # noqa

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)
app.include_router(auth.router)
