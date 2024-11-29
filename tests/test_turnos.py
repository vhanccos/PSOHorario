from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_crear_turno():
    response = client.post(
        "/turnos/",
        json={
            "nombre": "Turno Matutino",
            "horario_disponible": {"inicio": "7:00", "fin": "13:00"},
        },
    )
    assert response.status_code == 200
    assert response.json()["nombre"] == "Turno Matutino"
    assert response.json()["horario_disponible"] == {"inicio": "7:00", "fin": "13:00"}


def test_obtener_turnos():
    response = client.get("/turnos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_obtener_turno():
    response = client.get("/turnos/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_actualizar_turno():
    response = client.put(
        "/turnos/1",
        json={
            "nombre": "Turno Vespertino",
            "horario_disponible": {"inicio": "14:00", "fin": "20:00"},
        },
    )
    assert response.status_code == 200
    assert response.json()["nombre"] == "Turno Vespertino"
    assert response.json()["horario_disponible"] == {"inicio": "14:00", "fin": "20:00"}


def test_eliminar_turno():
    response = client.delete("/turnos/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

    # Verificar que el turno fue eliminado
    response = client.get("/turnos/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "Turno no encontrado"
