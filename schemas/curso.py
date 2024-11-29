from typing import List, Optional

from pydantic import BaseModel


class CursoCreate(BaseModel):
    nombre: str
    horas_semanales: int
    docentes_calificados: List[int]  # Lista de IDs de docentes calificados
    ciclo: str


class Curso(BaseModel):
    id: str
    nombre: str
    horas_semanales: int
    docentes_calificados: List[int]
    ciclo: str

    class Config:
        orm_mode = True


class CursoUpdate(BaseModel):
    nombre: Optional[str]
    horas_semanales: Optional[int]
    docentes_calificados: Optional[List[int]]
    ciclo: Optional[str]
