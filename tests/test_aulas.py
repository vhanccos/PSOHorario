import pytest
from fastapi.testclient import TestClient
from main import app
from models.aula import Aula
from schemas.aula import AulaCreate

client = TestClient(app)


@pytest.fixture
def aula_data():
    return {"capacidad": 30, "uso_especial": "Laboratorio de informática"}


# Test para crear un aula
def test_crear_aula(aula_data):
    response = client.post("/aulas/", json=aula_data)
    assert response.status_code == 200
    assert response.json()["capacidad"] == aula_data["capacidad"]
    assert response.json()["uso_especial"] == aula_data["uso_especial"]


# Test para obtener todos los aulas
def test_obtener_aulas():
    response = client.get("/aulas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test para obtener un aula específico
def test_obtener_aula(aula_data):
    # Crear un aula primero
    response = client.post("/aulas/", json=aula_data)
    aula_id = response.json()["id"]

    response = client.get(f"/aulas/{aula_id}")
    assert response.status_code == 200
    assert response.json()["id"] == aula_id
    assert response.json()["capacidad"] == aula_data["capacidad"]


# Test para actualizar un aula
def test_actualizar_aula(aula_data):
    # Crear un aula primero
    response = client.post("/aulas/", json=aula_data)
    aula_id = response.json()["id"]

    # Cambiar los datos del aula
    aula_data_actualizada = aula_data.copy()
    aula_data_actualizada["capacidad"] = 40

    response = client.put(f"/aulas/{aula_id}", json=aula_data_actualizada)
    assert response.status_code == 200
    assert response.json()["capacidad"] == 40


# Test para eliminar un aula
def test_eliminar_aula(aula_data):
    # Crear un aula primero
    response = client.post("/aulas/", json=aula_data)
    aula_id = response.json()["id"]

    # Eliminar el aula
    response = client.delete(f"/aulas/{aula_id}")
    assert response.status_code == 200
    assert response.json()["id"] == aula_id

    # Verificar que el aula ya no existe
    response = client.get(f"/aulas/{aula_id}")
    assert response.status_code == 404
