# Pruebas de regresión con Python

Repositorio educativo para estudiar cómo una suite automatizada detecta cambios que alteran comportamientos previamente correctos. El módulo principal integra el patrón Triple AAA, los principios FIRST y aserciones expresivas con PyHamcrest.

## Objetivos de aprendizaje

Al finalizar la práctica, el estudiante podrá:

- Explicar qué es una regresión de software.
- Organizar pruebas con Arrange, Act y Assert.
- Evaluar pruebas mediante los principios FIRST.
- Construir aserciones legibles y expresivas.
- Ejecutar pruebas completas, por archivo e individuales.
- Reproducir un defecto, detectarlo y evitar que reaparezca.

## Módulos

| Carpeta | Propósito |
|---|---|
| `regression-testing` | Regresión funcional, AAA, FIRST y PyHamcrest |
| `api-testing` | Regresión de endpoints, códigos HTTP y respuestas JSON |
| `performance-testing` | Detección básica de degradaciones de rendimiento |
| `security-testing` | Regresión de reglas de validación |

## Requisitos

- Python 3.10 o superior.
- `pip`.
- Visual Studio Code con la extensión **Python** (recomendado).
- Git, si el proyecto se obtiene desde GitHub.

## Estructura del módulo principal

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

Los archivos de `app/` contienen el código que se prueba. Los archivos de `tests/` contienen las pruebas automatizadas. Las actividades para desarrollar durante la clase se encuentran en `ejercicios/README.md`.

## Inicio rápido del módulo principal

### Windows PowerShell

Desde la carpeta raíz del repositorio, ejecute:

```powershell
cd regression-testing
py -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
& ".\.venv\Scripts\python.exe" -m pytest -q
```

La creación del entorno virtual y la instalación de dependencias solo se realizan la primera vez.

En las siguientes sesiones, ingrese a `regression-testing` y ejecute directamente las pruebas:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest -q
```

### Linux o macOS

```bash
cd regression-testing
python3 -m venv .venv
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python -m pytest -q
```

## Ejecutar todas las pruebas

En Windows PowerShell:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest -v
```

El resultado esperado es:

```text
15 passed
```

Para obtener una salida resumida:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest -q
```

## Consultar las pruebas disponibles

Para listar todas las pruebas sin ejecutarlas:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest --collect-only -q
```

Pytest identifica cada prueba mediante la siguiente estructura:

```text
ruta_del_archivo.py::nombre_de_la_prueba
```

## Ejecutar las pruebas por archivo

Ejecutar solamente las pruebas de la calculadora:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest tests/test_regression.py -v
```

Ejecutar solamente las pruebas del carrito:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest tests/test_carrito_aaa_first.py -v
```

## Ejecutar una prueba individual

Ejecutar solamente la prueba de suma:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest "tests/test_regression.py::test_regresion_suma" -v
```

Ejecutar solamente la prueba de resta:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest "tests/test_regression.py::test_regresion_resta" -v
```

Ejecutar solamente la prueba de multiplicación:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest "tests/test_regression.py::test_regresion_multiplicacion" -v
```

Ejecutar solamente la prueba de división:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest "tests/test_regression.py::test_regresion_division" -v
```

Ejecutar solamente la prueba de división por cero:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest "tests/test_regression.py::test_regresion_division_por_cero" -v
```

Ejecutar solamente la prueba del descuento del 10 %:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest "tests/test_carrito_aaa_first.py::test_total_con_descuento_del_diez_por_ciento" -v
```

También se pueden ejecutar todas las pruebas cuyo nombre contenga una palabra:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest -k "descuento" -v
```

## Ejecutar una prueba desde Visual Studio Code

1. Abra la carpeta raíz `RegressionTesting` en Visual Studio Code.
2. Abra uno de los archivos ubicados en `regression-testing/tests`.
3. Localice una función cuyo nombre comience por `test_`.
4. Seleccione la opción **Run Test** que aparece encima de la función.
5. Revise el resultado en el panel **Testing**.

Si no aparece la opción **Run Test**:

1. Abra el panel **Testing**.
2. Seleccione **Configure Python Tests**.
3. Elija `pytest`.
4. Seleccione la carpeta `regression-testing/tests`.
5. Configure como intérprete el Python del entorno `.venv`.

## Patrón Triple AAA

Las pruebas se organizan utilizando el patrón Triple AAA:

- **Arrange:** preparar los datos y las condiciones necesarias.
- **Act:** ejecutar la operación que se quiere probar.
- **Assert:** verificar automáticamente el resultado obtenido.

Ejemplo:

```python
def test_regresion_suma():
    # Arrange
    numero_uno = 10
    numero_dos = 5

    # Act
    resultado = suma(numero_uno, numero_dos)

    # Assert
    assert_that(resultado, equal_to(15))
```

## Principios FIRST

Las pruebas deben cumplir los siguientes principios:

- **Fast:** deben ejecutarse rápidamente.
- **Independent:** no deben depender de otras pruebas.
- **Repeatable:** deben producir el mismo resultado en diferentes ejecuciones.
- **Self-validating:** deben determinar automáticamente si pasan o fallan.
- **Timely:** deben escribirse en el momento adecuado, preferiblemente junto con la funcionalidad.

## Interpretación de los resultados

- `PASSED`: el comportamiento cumple con el resultado esperado.
- `FAILED`: una aserción no se cumplió.
- `ERROR`: la prueba no pudo ejecutarse debido a un problema de configuración, importación o dependencias.

Cuando una prueba falla, no debe modificarse inmediatamente para conseguir que pase. Primero se debe determinar si el problema se encuentra en el código de `app/`, en los datos de prueba o en el resultado esperado.

## Ruta sugerida para la clase

1. Ejecutar toda la suite y confirmar que las 15 pruebas pasan.
2. Establecer esta ejecución como línea base.
3. Ejecutar una prueba individual de la calculadora.
4. Ejecutar una prueba individual del carrito.
5. Reconocer Arrange, Act y Assert en las pruebas.
6. Revisar el cumplimiento de los principios FIRST.
7. Introducir de manera controlada un defecto.
8. Ejecutar nuevamente la suite y observar la regresión.
9. Corregir el código.
10. Ejecutar toda la suite para comprobar que las 15 pruebas vuelven a pasar.
11. Agregar una prueba que evite la reaparición del defecto.

Los defectos introducidos durante la práctica son temporales y no deben incluirse en el commit final.

La guía completa de actividades se encuentra en [`regression-testing/ejercicios/README.md`](regression-testing/ejercicios/README.md).

## Resultado esperado

Todas las pruebas deben finalizar correctamente antes y después de cada cambio válido.


## Nota académica

Los ejemplos de rendimiento y seguridad son introductorios. Un límite de tiempo aislado no sustituye una herramienta de carga y la sanitización simple no reemplaza los mecanismos de seguridad propios del framework utilizado.