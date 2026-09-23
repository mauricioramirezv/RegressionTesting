# Ejercicios para la clase

Ejecute primero `python -m pytest -q`. La suite debe estar completamente verde
antes de comenzar.

## Ejercicio 1. Patrón Triple AAA

Tome la prueba `test_regresion_resta` y explique qué instrucciones pertenecen
a cada sección:

1. **Arrange:** preparación del sistema y de los datos.
2. **Act:** ejecución de una sola acción principal.
3. **Assert:** verificación automática del resultado.

Después escriba una prueba para `modulo(20, 6)` sin copiar otra prueba y
organícela explícitamente con AAA. El resultado esperado es `2`.

## Ejercicio 2. Principios FIRST

Analice cada situación e indique el principio incumplido:

1. Una prueba contiene `sleep(10)` antes de comprobar el resultado.
2. Una prueba utiliza el objeto creado por una prueba anterior.
3. La prueba depende de la fecha actual y falla el primer día del mes.
4. La prueba imprime el resultado, pero no contiene una aserción.
5. La funcionalidad fue desarrollada hace meses y todavía no tiene pruebas.

Refactorice al menos los cuatro primeros casos. Las pruebas resultantes deben:

- utilizar datos locales;
- ejecutarse rápidamente;
- producir el mismo resultado en cualquier equipo;
- aprobar o fallar sin revisión manual.

## Ejercicio 3. Detectar una regresión

1. Confirme que toda la suite pasa.
2. Abra `app/carrito.py`.
3. En `total_con_descuento`, cambie temporalmente `/ 100` por `/ 10`.
4. Ejecute nuevamente `python -m pytest -q`.
5. Identifique las pruebas que detectan la regresión y explique sus mensajes.
6. Restaure `/ 100` y confirme que la suite vuelve a pasar.

El defecto temporal no debe incluirse en el commit.

## Ejercicio 4. Nueva regla y prueba de regresión

Agregue una regla que impida precios iguales a cero. Siga este orden:

1. Escriba primero una prueba que exprese el comportamiento esperado.
2. Ejecútela y compruebe que falla por la razón correcta.
3. Implemente la validación mínima.
4. Ejecute toda la suite para descartar regresiones.
5. Revise que la prueba cumpla AAA y FIRST.

## Preguntas de cierre

- ¿Qué diferencia existe entre volver a ejecutar pruebas y tener una estrategia
  de regresión?
- ¿Cuál prueba ofrece mayor información cuando falla?
- ¿Qué principio FIRST resulta más difícil de cumplir en pruebas de API?
- ¿Cómo mejoran las aserciones expresivas el diagnóstico de una regresión?
