# Pruebas de regresión con Python

Repositorio educativo para estudiar cómo una suite automatizada detecta cambios
que alteran comportamientos previamente correctos. El módulo principal integra
el patrón Triple AAA, los principios FIRST y aserciones expresivas con
PyHamcrest.

## Objetivos de aprendizaje

- Explicar qué es una regresión de software.
- Organizar pruebas con Arrange, Act y Assert.
- Evaluar pruebas mediante los principios FIRST.
- Construir aserciones legibles y expresivas.
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

## Inicio rápido del módulo principal

En Windows PowerShell:

```powershell
cd regression-testing
py -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
& ".\.venv\Scripts\python.exe" -m pytest -q
```

En Linux o macOS:

```bash
cd regression-testing
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python -m pytest -q
```

## Ruta sugerida para la clase

1. Ejecutar la suite y establecer una línea base.
2. Reconocer Arrange, Act y Assert en las pruebas.
3. Revisar los principios FIRST.
4. Introducir de manera controlada un defecto.
5. Ejecutar la suite y observar la regresión.
6. Corregir el código y agregar una prueba que evite su reaparición.

La guía completa se encuentra en
[`regression-testing/ejercicios/README.md`](regression-testing/ejercicios/README.md).

## Nota académica

Los ejemplos de rendimiento y seguridad son introductorios. Un límite de
tiempo aislado no sustituye una herramienta de carga y la sanitización simple
no reemplaza los mecanismos de seguridad propios del framework utilizado.
