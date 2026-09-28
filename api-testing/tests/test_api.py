from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from app.main import PRODUCTOS, app

client = TestClient(app)


@pytest.fixture(autouse=True)
def restaurar_productos():
    """Mantiene las pruebas independientes aunque una de ellas modifique datos."""
    productos_iniciales = deepcopy(PRODUCTOS)
    yield
    PRODUCTOS.clear()
    PRODUCTOS.update(productos_iniciales)

def test_health_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_listar_productos():
    response = client.get("/productos")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "nombre": "Teclado", "precio": 120.0},
        {"id": 2, "nombre": "Mouse", "precio": 80.0},
    ]

def test_obtener_producto_existente():
    response = client.get("/productos/1")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Teclado"

def test_obtener_producto_inexistente():
    response = client.get("/productos/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Producto no encontrado"

def test_crear_producto():
    payload = {"nombre": "Monitor", "precio": 500.0}
    response = client.post("/productos", json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 3
    assert body["nombre"] == "Monitor"
    assert body["precio"] == 500.0


@pytest.mark.parametrize(
    "payload",
    [
        {"nombre": "", "precio": 100.0},
        {"nombre": "Monitor", "precio": 0},
        {"nombre": "Monitor", "precio": -1},
    ],
)
def test_crear_producto_rechaza_datos_invalidos(payload):
    response = client.post("/productos", json=payload)

    assert response.status_code == 422


def test_crear_producto_no_contamina_otras_pruebas():
    response = client.get("/productos")

    assert response.status_code == 200
    assert len(response.json()) == 2
