# Pruebas de regresión de una API con FastAPI

Este módulo verifica el contrato HTTP de una API pequeña de productos. Las
pruebas se ejecutan en memoria mediante `TestClient`; no es necesario iniciar
un servidor para correrlas.

## Aspectos verificados

- disponibilidad mediante `/health`;
- códigos `200`, `201`, `404` y `422`;
- estructura y contenido de respuestas JSON;
- consulta de recursos existentes e inexistentes;
- creación y validación de productos;
- independencia entre pruebas que modifican el estado.

## Preparación aislada en Windows

Desde esta carpeta:

```powershell
py -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
```

## Ejecutar

Toda la suite:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest -v
```

Una prueba individual:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest `
    "tests/test_api.py::test_obtener_producto_inexistente" -v
```

Pruebas relacionadas con creación:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest -k "crear_producto" -v
```

El resultado esperado es `9 passed`.

## Ejecutar la API manualmente

```powershell
& ".\.venv\Scripts\python.exe" -m uvicorn app.main:app --reload
```

Después puede abrir:

- documentación Swagger: <http://127.0.0.1:8000/docs>
- comprobación de salud: <http://127.0.0.1:8000/health>

## Nota sobre FIRST

La API utiliza un diccionario en memoria. Una prueba que crea un producto podría
afectar las siguientes. La fixture automática conserva y restaura el estado,
por lo que las pruebas permanecen independientes y repetibles.
