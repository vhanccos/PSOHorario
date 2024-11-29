from pydantic import BaseModel


class AulaBase(BaseModel):
    capacidad: int
    uso_especial: str


class AulaCreate(AulaBase):
    pass


class Aula(AulaBase):
    id: str

    class Config:
        orm_mode = True
