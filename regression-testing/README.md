# Regresión funcional: AAA, FIRST y PyHamcrest

Este módulo utiliza una calculadora y un carrito de compras para mostrar cómo
las pruebas automatizadas protegen comportamientos previamente aceptados.

## Objetivos

- explicar el propósito de una prueba de regresión;
- organizar una prueba con Arrange, Act y Assert;
- reconocer los principios FIRST;
- utilizar aserciones expresivas con PyHamcrest;
- verificar casos normales, límites y excepciones;
- reproducir y corregir una regresión controlada.

## Estructura

```text
regression-testing/
├── app/
│   ├── calculadora.py
│   └── carrito.py
├── tests/
│   ├── test_regression.py
│   └── test_carrito_aaa_first.py
├── ejercicios/
│   └── README.md
├── pytest.ini
└── requirements.txt
```

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

El resultado esperado es `15 passed`.

Solo las pruebas de la calculadora:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest tests/test_regression.py -v
```

Solo las pruebas del carrito:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest tests/test_carrito_aaa_first.py -v
```

Una prueba individual:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest `
    "tests/test_carrito_aaa_first.py::test_total_con_descuento_del_diez_por_ciento" -v
```

Listar los identificadores disponibles:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest --collect-only -q
```

## Patrón Triple AAA

- **Arrange:** prepara el sistema y los datos.
- **Act:** ejecuta una acción principal.
- **Assert:** verifica automáticamente el resultado.

Ejemplo:

```python
def test_regresion_suma():
    # Arrange
    a = 2
    b = 3

    # Act
    resultado = sumar(a, b)

    # Assert
    assert_that(resultado, equal_to(5))
```

## Principios FIRST

- **Fast:** ejecución rápida.
- **Independent:** independencia entre pruebas.
- **Repeatable:** mismo resultado bajo las mismas condiciones.
- **Self-validating:** aprobación o fallo automático.
- **Timely:** creación oportuna junto con el comportamiento.

## Actividad sugerida

1. Confirme que las 15 pruebas pasan.
2. Ejecute una prueba individual.
3. Identifique Arrange, Act y Assert.
4. Analice la prueba según FIRST.
5. Introduzca el defecto controlado descrito en
   [`ejercicios/README.md`](ejercicios/README.md).
6. Observe qué prueba detecta la regresión.
7. Restaure el código y confirme nuevamente las 15 pruebas.

Los defectos temporales utilizados durante la práctica no deben incluirse en el
commit final.
