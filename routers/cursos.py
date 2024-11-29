from typing import List

from fastapi import APIRouter, HTTPException

from models.curso import Curso as CursoModel
from schemas.curso import Curso, CursoCreate, CursoUpdate
from utils.lector_csv import LectorCSV  # Importamos el lector CSV

router = APIRouter()

# Instancia del lector CSV
lector_csv = LectorCSV()


@router.post("/", response_model=Curso)
def crear_curso(curso: CursoCreate):
    # Leer los cursos existentes desde el archivo CSV
    cursos = lector_csv.leer_cursos()

    # Generar un nuevo ID para el curso
    curso_id = len(cursos) + 1
    new_curso = CursoModel(id=curso_id, **curso.dict())

    # Agregar el nuevo curso
    cursos.append(new_curso)

    # Guardar los cursos actualizados en el CSV
    lector_csv.guardar_cursos(cursos)

    return new_curso


@router.get("/", response_model=List[Curso])
def obtener_cursos():
    # Leer los cursos desde el archivo CSV
    cursos = lector_csv.leer_cursos()
    return cursos


@router.get("/{curso_id}", response_model=Curso)
def obtener_curso(curso_id: int):
    # Leer los cursos desde el archivo CSV
    cursos = lector_csv.leer_cursos()
    curso = next((c for c in cursos if c.id == curso_id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso


@router.put("/{curso_id}", response_model=Curso)
def actualizar_curso(curso_id: int, curso: CursoUpdate):
    # Leer los cursos desde el archivo CSV
    cursos = lector_csv.leer_cursos()
    curso_existente = next((c for c in cursos if c.id == curso_id), None)
    if curso_existente is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")

    # Actualizar los campos del curso
    curso_existente.nombre = curso.nombre if curso.nombre else curso_existente.nombre
    curso_existente.horas_semanales = (
        curso.horas_semanales
        if curso.horas_semanales
        else curso_existente.horas_semanales
    )
    curso_existente.docentes_calificados = (
        curso.docentes_calificados
        if curso.docentes_calificados
        else curso_existente.docentes_calificados
    )
    curso_existente.ciclo = curso.ciclo if curso.ciclo else curso_existente.ciclo

    # Guardar los cursos actualizados en el archivo CSV
    lector_csv.guardar_cursos(cursos)

    return curso_existente


@router.delete("/{curso_id}", response_model=Curso)
def eliminar_curso(curso_id: int):
    # Leer los cursos desde el archivo CSV
    cursos = lector_csv.leer_cursos()
    curso = next((c for c in cursos if c.id == curso_id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")

    # Eliminar el curso
    cursos.remove(curso)

    # Guardar los cursos actualizados en el archivo CSV
    lector_csv.guardar_cursos(cursos)

    return curso
