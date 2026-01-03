from datetime import datetime, UTC

from fastapi import FastAPI

app = FastAPI()

fake_db = [
    {"tittle": f"Criando uma aplicação com Django", "date": datetime.now(UTC)},
    {"tittle": f"Internacionalizando uma app FastAPI", "date": datetime.now(UTC)}
]

@app.get("/posts")

@app.get("/posts/{framework}")
def read_framework_posts(framework):
    return {
        "posts": [
            {"tittle": f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)},
            {"tittle": f"Internacionalizando uma app {framework}", "date": datetime.now(UTC)}
        ]
    }
