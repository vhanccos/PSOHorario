import pytest
from fastapi.testclient import TestClient

from main import app
from models.curso import Curso
from schemas.curso import CursoCreate

client = TestClient(app)


@pytest.fixture
def curso_data():
    return {
        "nombre": "Curso de Python",
        "horas_semanales": 5,
        "docentes_calificados": [1, 2],
        "ciclo": "2024-1",
    }


# Test para crear un curso
def test_crear_curso(curso_data):
    response = client.post("/cursos/", json=curso_data)
    assert response.status_code == 200
    assert response.json()["nombre"] == curso_data["nombre"]
    assert response.json()["horas_semanales"] == curso_data["horas_semanales"]
    assert response.json()["docentes_calificados"] == curso_data["docentes_calificados"]
    assert response.json()["ciclo"] == curso_data["ciclo"]


# Test para obtener todos los cursos
def test_obtener_cursos():
    response = client.get("/cursos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test para obtener un curso específico
def test_obtener_curso(curso_data):
    # Crear un curso primero
    response = client.post("/cursos/", json=curso_data)
    curso_id = response.json()["id"]

    response = client.get(f"/cursos/{curso_id}")
    assert response.status_code == 200
    assert response.json()["id"] == curso_id
    assert response.json()["nombre"] == curso_data["nombre"]


# Test para actualizar un curso
def test_actualizar_curso(curso_data):
    # Crear un curso primero
    response = client.post("/cursos/", json=curso_data)
    curso_id = response.json()["id"]

    # Cambiar los datos del curso
    curso_data_actualizada = curso_data.copy()
    curso_data_actualizada["nombre"] = "Curso de JavaScript"

    response = client.put(f"/cursos/{curso_id}", json=curso_data_actualizada)
    assert response.status_code == 200
    assert response.json()["nombre"] == "Curso de JavaScript"


# Test para eliminar un curso
def test_eliminar_curso(curso_data):
    # Crear un curso primero
    response = client.post("/cursos/", json=curso_data)
    curso_id = response.json()["id"]

    # Eliminar el curso
    response = client.delete(f"/cursos/{curso_id}")
    assert response.status_code == 200
    assert response.json()["id"] == curso_id

    # Verificar que el curso ya no existe
    response = client.get(f"/cursos/{curso_id}")
    assert response.status_code == 404
