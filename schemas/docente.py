from pydantic import BaseModel
from typing import List, Optional


class DocenteBase(BaseModel):
    nombre: str
    tipo: str
    disponibilidad: List[str]  # Lista de días o turnos disponibles
    horas_max: int
    horas_min: int


class DocenteCreate(DocenteBase):
    pass


class DocenteUpdate(DocenteBase):
    pass


class DocenteInDB(DocenteBase):
    id: str

    class Config:
        orm_mode = True
