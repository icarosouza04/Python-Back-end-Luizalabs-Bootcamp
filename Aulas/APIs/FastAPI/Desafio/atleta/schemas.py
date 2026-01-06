from Aulas.APIs.FastAPI.Desafio.contrib.schemas import BaseSchema, OutMixin
from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated

class Atleta(BaseSchema):
    nome : Annotated[str, Field(description = "Nome do atleta", example = "Icaro", max_length = 50)]
    cpf: Annotated[str, Field(description = "CPF do atleta", example = "00000000000", max_length = 11)]
    idade: Annotated[int, Field(description = "Idade do atleta", example = "21")]
    peso: Annotated[PositiveFloat, Field(description = "Peso do atleta", example = "70.1")]
    altura: Annotated[PositiveFloat, Field(description = "Altura do atleta", example = "1.73")]
    sexo: Annotated[str, Field(description = "Sexo do atleta", example = "M", max_length = 1)]

class AtletaIn(Atleta):
    pass

class AtletaOut(AtletaIn, OutMixin):
    pass