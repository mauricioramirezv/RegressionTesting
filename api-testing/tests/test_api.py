from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_listar_productos():
    response = client.get("/productos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

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
    assert body["nombre"] == "Monitor"
    assert body["precio"] == 500.0
