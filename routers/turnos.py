from typing import List

from fastapi import APIRouter, HTTPException

from models.turno import Turno as TurnoModel
from schemas.turno import Turno, TurnoCreate, TurnoUpdate
from utils.lector_csv import LectorCSV  # Importamos el lector CSV

router = APIRouter()

# Instancia del lector CSV
lector_csv = LectorCSV()


@router.post("/", response_model=Turno)
async def crear_turno(turno: TurnoCreate):
    # Leer los turnos desde el archivo CSV
    turnos = lector_csv.leer_turnos()

    # Generar un nuevo ID para el turno
    turno_id = len(turnos) + 1
    new_turno = TurnoModel(id=turno_id, **turno.dict())

    # Agregar el nuevo turno a la lista
    turnos.append(new_turno)

    # Guardar los turnos actualizados en el archivo CSV
    lector_csv.guardar_turnos(turnos)

    return new_turno


@router.get("/", response_model=List[Turno])
async def obtener_turnos():
    # Leer los turnos desde el archivo CSV
    turnos = lector_csv.leer_turnos()
    return turnos


@router.get("/{turno_id}", response_model=Turno)
async def obtener_turno(turno_id: int):
    # Leer los turnos desde el archivo CSV
    turnos = lector_csv.leer_turnos()
    turno = next((t for t in turnos if t.id == turno_id), None)
    if turno is None:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return turno


@router.put("/{turno_id}", response_model=Turno)
async def actualizar_turno(turno_id: int, turno: TurnoUpdate):
    # Leer los turnos desde el archivo CSV
    turnos = lector_csv.leer_turnos()
    turno_existente = next((t for t in turnos if t.id == turno_id), None)
    if turno_existente is None:
        raise HTTPException(status_code=404, detail="Turno no encontrado")

    # Actualizar los campos del turno
    turno_existente.nombre = turno.nombre if turno.nombre else turno_existente.nombre
    turno_existente.horario_disponible = (
        turno.horario_disponible
        if turno.horario_disponible
        else turno_existente.horario_disponible
    )

    # Guardar los turnos actualizados en el archivo CSV
    lector_csv.guardar_turnos(turnos)

    return turno_existente


@router.delete("/{turno_id}", response_model=Turno)
async def eliminar_turno(turno_id: int):
    # Leer los turnos desde el archivo CSV
    turnos = lector_csv.leer_turnos()
    turno = next((t for t in turnos if t.id == turno_id), None)
    if turno is None:
        raise HTTPException(status_code=404, detail="Turno no encontrado")

    # Eliminar el turno
    turnos.remove(turno)

    # Guardar los turnos actualizados en el archivo CSV
    lector_csv.guardar_turnos(turnos)

    return turno
