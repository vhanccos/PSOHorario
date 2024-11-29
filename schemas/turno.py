from typing import Dict, Optional

from pydantic import BaseModel


class TurnoCreate(BaseModel):
    nombre: str
    horario_disponible: Dict[str, str]  # {"inicio": "7:00", "fin": "13:00"}


class Turno(BaseModel):
    id: str
    nombre: str
    horario_disponible: Dict[str, str]  # {"inicio": "7:00", "fin": "13:00"}

    class Config:
        orm_mode = True


class TurnoUpdate(BaseModel):
    nombre: Optional[str]
    horario_disponible: Optional[Dict[str, str]]
