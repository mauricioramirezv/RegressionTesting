# Ejemplos de pruebas de regresión con Python

Repositorio educativo con cuatro módulos independientes para estudiar regresión
funcional, pruebas de API, verificaciones básicas de rendimiento y validaciones
de seguridad. Todos los ejemplos utilizan Pytest y están preparados para
ejecutarse de forma aislada o mediante un único comando desde la raíz.

## Objetivos de aprendizaje

Al finalizar las prácticas, el estudiante podrá:

- explicar qué es una regresión de software;
- organizar pruebas con Arrange, Act y Assert;
- evaluar pruebas mediante los principios FIRST;
- comprobar contratos HTTP, códigos de estado y validaciones de entrada;
- establecer una línea base educativa de rendimiento;
- verificar reglas básicas de contraseñas y escape de texto para HTML;
- ejecutar una suite completa, un módulo o una prueba individual.

## Módulos

| Carpeta | Propósito | Suite esperada |
|---|---|---:|
| [`regression-testing`](regression-testing/README.md) | Regresión funcional, AAA, FIRST y PyHamcrest | 15 pruebas |
| [`api-testing`](api-testing/README.md) | Contratos de endpoints, respuestas JSON y validación | 9 pruebas |
| [`performance-testing`](performance-testing/README.md) | Línea base, presupuesto y comparación de rendimiento | 8 pruebas |
| [`security-testing`](security-testing/README.md) | Reglas de contraseña y escape de contenido HTML | 9 pruebas |

## Requisitos

- Python 3.10 o superior.
- `pip`.
- Git.
- Visual Studio Code con la extensión **Python** (opcional).

## Inicio rápido: ejecutar todos los módulos

En Windows PowerShell, desde la raíz del repositorio:

```powershell
py -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
& ".\.venv\Scripts\python.exe" run_all_tests.py
```

En Linux o macOS:

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python run_all_tests.py
```

El script ejecuta cada módulo en un proceso independiente. Esto es necesario
porque todos contienen un paquete llamado `app`.

> No ejecute `python -m pytest` directamente desde la raíz. Pytest intentaría
> cargar simultáneamente los cuatro paquetes `app` y podría producir errores de
> importación o importar el módulo incorrecto.

## Ejecutar un solo módulo

Ejemplo para pruebas de API en Windows:

```powershell
Set-Location api-testing
& "..\.venv\Scripts\python.exe" -m pytest -v
```

Cambie `api-testing` por `regression-testing`, `performance-testing` o
`security-testing` según la práctica que quiera ejecutar.

## Ejecutar una prueba individual

```powershell
Set-Location regression-testing
& "..\.venv\Scripts\python.exe" -m pytest `
    "tests/test_regression.py::test_regresion_suma" -v
```

Para consultar todos los identificadores disponibles dentro de un módulo:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest --collect-only -q
```

## Ruta sugerida para la clase

1. Ejecutar todas las suites y establecer una línea base verde.
2. Trabajar regresión funcional, Triple AAA y principios FIRST.
3. Revisar contratos y aislamiento del estado en pruebas de API.
4. Comparar corrección funcional con restricciones de rendimiento.
5. Analizar validaciones de seguridad y sus límites.
6. Introducir un defecto controlado en un módulo.
7. Ejecutar primero la prueba relacionada y luego todas las suites.
8. Restaurar el comportamiento correcto antes del commit final.

## Alcance académico

Estos ejemplos son introductorios. Una restricción de tiempo ejecutada en una
sola máquina no reemplaza pruebas de carga, estrés o capacidad con herramientas
especializadas. Del mismo modo, el escape de texto para HTML no sustituye los
controles de autenticación, autorización, gestión de secretos, consultas
parametrizadas, encabezados de seguridad y demás mecanismos del framework.

Los defectos introducidos durante los ejercicios son temporales y no deben
publicarse en el repositorio.
