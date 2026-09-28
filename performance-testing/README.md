# Pruebas educativas de rendimiento

Este módulo compara dos implementaciones para sumar los números desde `0` hasta
`n - 1`: una iterativa y otra basada en una fórmula de tiempo constante.

## Aspectos verificados

- corrección funcional para distintos tamaños de entrada;
- rechazo de entradas negativas;
- cumplimiento de un presupuesto de tiempo amplio;
- comparación repetida mediante la mediana de cinco mediciones.

## Preparación aislada en Windows

```powershell
py -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
```

## Ejecutar

Toda la suite:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest -v
```

Solo las pruebas marcadas como rendimiento:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest -m performance -v
```

Una prueba individual:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest `
    "tests/test_performance.py::test_formula_es_mas_rapida_que_la_iteracion" -v
```

El resultado esperado es `8 passed`.

## Interpretación

Una prueba funcional comprueba que el resultado es correcto. Una prueba de
rendimiento agrega una expectativa no funcional, por ejemplo, terminar dentro
de un presupuesto o superar una línea base.

El límite utilizado es intencionalmente amplio para reducir falsos fallos en
equipos diferentes. Este ejemplo no reemplaza herramientas como Locust, JMeter,
k6 o pytest-benchmark para estudios rigurosos de carga y rendimiento.
