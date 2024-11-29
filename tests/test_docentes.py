import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_docente():
    response = client.post(
        "/docentes/",
        json={
            "nombre": "Juan Perez",
            "tipo": "Profesor",
            "disponibilidad": ["Lunes", "Martes"],
            "horas_max": 20,
            "horas_min": 10,
        },
    )
    assert response.status_code == 200
    assert response.json()["nombre"] == "Juan Perez"


def test_get_docentes():
    response = client.get("/docentes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_docente():
    response = client.post(
        "/docentes/",
        json={
            "nombre": "Carlos Garcia",
            "tipo": "Tutor",
            "disponibilidad": ["Miércoles", "Viernes"],
            "horas_max": 15,
            "horas_min": 5,
        },
    )
    docente_id = response.json()["id"]
    response = client.get(f"/docentes/{docente_id}")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Carlos Garcia"


def test_update_docente():
    response = client.post(
        "/docentes/",
        json={
            "nombre": "Ana López",
            "tipo": "Auxiliar",
            "disponibilidad": ["Martes", "Jueves"],
            "horas_max": 10,
            "horas_min": 5,
        },
    )
    docente_id = response.json()["id"]
    response = client.put(
        f"/docentes/{docente_id}",
        json={
            "nombre": "Ana López",
            "tipo": "Auxiliar",
            "disponibilidad": ["Martes", "Jueves", "Viernes"],
            "horas_max": 12,
            "horas_min": 6,
        },
    )
    assert response.status_code == 200
    assert "Viernes" in response.json()["disponibilidad"]


def test_delete_docente():
    response = client.post(
        "/docentes/",
        json={
            "nombre": "Roberto Díaz",
            "tipo": "Asistente",
            "disponibilidad": ["Lunes", "Miércoles"],
            "horas_max": 18,
            "horas_min": 8,
        },
    )
    docente_id = response.json()["id"]
    response = client.delete(f"/docentes/{docente_id}")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Roberto Díaz"
