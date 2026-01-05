from typing import Annotated

from pydantic import Field
from Aulas.APIs.FastAPI.Desafio.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome : Annotated[str, Field(description = "Nome da categoria", example = "Scale", max_length = 50)]