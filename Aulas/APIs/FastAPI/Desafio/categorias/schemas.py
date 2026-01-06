from typing import Annotated

from pydantic import UUID4, Field
from Aulas.APIs.FastAPI.Desafio.contrib.schemas import BaseSchema

class CategoriaIn(BaseSchema):
    nome : Annotated[str, Field(description = "Nome da categoria", example = "Scale", max_length = 50)]


class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description = "Identificador da categoria")]