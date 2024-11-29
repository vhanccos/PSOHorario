from typing import List

from fastapi import APIRouter, HTTPException

from models.docente import Docente
from schemas.docente import DocenteCreate, DocenteInDB, DocenteUpdate
from utils.lector_csv import LectorCSV  # Importamos el lector CSV

router = APIRouter()

# Instancia del lector CSV
lector_csv = LectorCSV()


@router.post("/", response_model=DocenteInDB)
async def create_docente(docente: DocenteCreate):
    # Leer los docentes desde el archivo CSV
    docentes = lector_csv.leer_docentes()

    # Generar un nuevo ID para el docente
    docente_id = len(docentes) + 1
    new_docente = Docente(id=docente_id, **docente.dict())

    # Agregar el nuevo docente a la lista
    docentes.append(new_docente)

    # Guardar los docentes actualizados en el archivo CSV
    lector_csv.guardar_docentes(docentes)

    return new_docente


@router.get("/", response_model=List[DocenteInDB])
async def get_docentes():
    # Leer los docentes desde el archivo CSV
    docentes = lector_csv.leer_docentes()
    return docentes


@router.get("/{docente_id}", response_model=DocenteInDB)
async def get_docente(docente_id: int):
    # Leer los docentes desde el archivo CSV
    docentes = lector_csv.leer_docentes()
    docente = next((d for d in docentes if d.id == docente_id), None)
    if docente is None:
        raise HTTPException(status_code=404, detail="Docente no encontrado")
    return docente


@router.put("/{docente_id}", response_model=DocenteInDB)
async def update_docente(docente_id: int, docente: DocenteUpdate):
    # Leer los docentes desde el archivo CSV
    docentes = lector_csv.leer_docentes()
    docente_existente = next((d for d in docentes if d.id == docente_id), None)
    if docente_existente is None:
        raise HTTPException(status_code=404, detail="Docente no encontrado")

    # Actualizar los campos del docente
    docente_existente.nombre = (
        docente.nombre if docente.nombre else docente_existente.nombre
    )
    docente_existente.email = (
        docente.email if docente.email else docente_existente.email
    )

    # Guardar los docentes actualizados en el archivo CSV
    lector_csv.guardar_docentes(docentes)

    return docente_existente


@router.delete("/{docente_id}", response_model=DocenteInDB)
async def delete_docente(docente_id: int):
    # Leer los docentes desde el archivo CSV
    docentes = lector_csv.leer_docentes()
    docente = next((d for d in docentes if d.id == docente_id), None)
    if docente is None:
        raise HTTPException(status_code=404, detail="Docente no encontrado")

    # Eliminar el docente
    docentes.remove(docente)

    # Guardar los docentes actualizados en el archivo CSV
    lector_csv.guardar_docentes(docentes)

    return docente
