from typing import List

from fastapi import APIRouter, HTTPException

from models.aula import Aula as AulaModel
from schemas.aula import Aula, AulaCreate
from utils.lector_csv import LectorCSV  # Importar el lector CSV

router = APIRouter()

# Instancia del lector CSV
lector_csv = LectorCSV()


@router.post("/", response_model=Aula)
def crear_aula(aula: AulaCreate):
    # Leer aulas existentes desde el CSV
    aulas = lector_csv.leer_aulas()

    # Crear el nuevo aula y agregarla
    aula_id = len(aulas) + 1  # Generar ID secuencial
    new_aula = AulaModel(id=aula_id, **aula.dict())
    aulas.append(new_aula)

    # Guardar las aulas actualizadas en el CSV
    lector_csv.guardar_aulas(aulas)

    return new_aula


@router.get("/", response_model=List[Aula])
def obtener_aulas():
    # Leer aulas desde el CSV
    aulas = lector_csv.leer_aulas()
    return aulas


@router.get("/{aula_id}", response_model=Aula)
def obtener_aula(aula_id: int):
    aulas = lector_csv.leer_aulas()
    aula = next((a for a in aulas if a.id == aula_id), None)
    if aula is None:
        raise HTTPException(status_code=404, detail="Aula no encontrada")
    return aula


@router.put("/{aula_id}", response_model=Aula)
def actualizar_aula(aula_id: int, aula: AulaCreate):
    aulas = lector_csv.leer_aulas()
    aula_existente = next((a for a in aulas if a.id == aula_id), None)
    if aula_existente is None:
        raise HTTPException(status_code=404, detail="Aula no encontrada")

    # Actualizar los datos del aula
    aula_existente.capacidad = aula.capacidad
    aula_existente.uso_especial = aula.uso_especial

    # Guardar las aulas actualizadas en el CSV
    lector_csv.guardar_aulas(aulas)

    return aula_existente


@router.delete("/{aula_id}", response_model=Aula)
def eliminar_aula(aula_id: int):
    aulas = lector_csv.leer_aulas()
    aula = next((a for a in aulas if a.id == aula_id), None)
    if aula is None:
        raise HTTPException(status_code=404, detail="Aula no encontrada")

    # Eliminar el aula
    aulas.remove(aula)

    # Guardar las aulas actualizadas en el CSV
    lector_csv.guardar_aulas(aulas)

    return aula
