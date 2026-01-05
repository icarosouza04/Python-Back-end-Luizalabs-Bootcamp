from typing import Annotated

from pydantic import Field
from Aulas.APIs.FastAPI.Desafio.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome : Annotated[str, Field(description = "Nome do centro de treinamento", example = "CT North", max_length = 20)]
    endereco : Annotated[str, Field(description = "Endereço do centro de treinamento", example = "R. North, QN", max_length = 60)]
    proprietario : Annotated[str, Field(description = "Proprietário do centro de treinamento", example = "Larry", max_length = 30)]
    