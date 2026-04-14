from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API Testing Demo", version="1.0.0")

PRODUCTOS = {
    1: {"id": 1, "nombre": "Teclado", "precio": 120.0},
    2: {"id": 2, "nombre": "Mouse", "precio": 80.0},
}

class ProductoIn(BaseModel):
    nombre: str
    precio: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/productos")
def listar_productos():
    return list(PRODUCTOS.values())

@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    if producto_id not in PRODUCTOS:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return PRODUCTOS[producto_id]

@app.post("/productos", status_code=201)
def crear_producto(producto: ProductoIn):
    nuevo_id = max(PRODUCTOS.keys()) + 1 if PRODUCTOS else 1
    nuevo = {"id": nuevo_id, "nombre": producto.nombre, "precio": producto.precio}
    PRODUCTOS[nuevo_id] = nuevo
    return nuevo
