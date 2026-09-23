# Regresión funcional: AAA, FIRST y PyHamcrest

Este módulo utiliza una calculadora y un carrito de compras para mostrar cómo
las pruebas automatizadas protegen comportamientos que ya fueron aceptados.

## Conceptos incluidos

- Patrón Triple AAA: Arrange, Act y Assert.
- Principios FIRST: Fast, Independent, Repeatable, Self-validating y Timely.
- Aserciones expresivas con PyHamcrest.
- Casos normales, casos límite y excepciones.
- Reproducción controlada de una regresión.

## Ejecutar

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

Pytest solo recoge las pruebas de `tests/`. Los archivos de `ejercicios/` son
actividades para completar durante la clase y no afectan la suite principal.

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
└── pytest.ini
```

## Resultado esperado

Todas las pruebas deben finalizar correctamente antes y después de cada cambio
válido. Cuando se introduce el defecto indicado en la guía, al menos una prueba
debe fallar y señalar el comportamiento alterado.
