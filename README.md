# Ejemplos de pruebas de regresión con Python

Repositorio educativo con cuatro proyectos independientes para estudiar pruebas de regresión funcional, API, rendimiento y seguridad.

Todos los ejemplos utilizan Pytest y pueden ejecutarse:

- conjuntamente desde la raíz del repositorio;
- individualmente por proyecto;
- por archivo de pruebas;
- como una única prueba específica.

## Proyectos incluidos

| Proyecto | Propósito | Resultado esperado |
|---|---|---:|
| [`regression-testing`](regression-testing/README.md) | Regresión funcional, Triple AAA, FIRST y PyHamcrest | 15 pruebas |
| [`api-testing`](api-testing/README.md) | Endpoints, códigos HTTP, JSON y validación de datos | 9 pruebas |
| [`performance-testing`](performance-testing/README.md) | Línea base, presupuesto y comparación de rendimiento | 8 pruebas |
| [`security-testing`](security-testing/README.md) | Contraseñas y escape de contenido HTML | 9 pruebas |
| **Total** | **Todas las suites** | **41 pruebas** |

## Requisitos

- Python 3.10 o superior.
- `pip`.
- Git.
- Visual Studio Code con la extensión **Python** (opcional).

## 1. Descargar el repositorio

```powershell
git clone https://github.com/mauricioramirezv/RegressionTesting.git
cd RegressionTesting
```

Los comandos siguientes deben ejecutarse desde la carpeta raíz `RegressionTesting`, excepto cuando se indique otra ubicación.

## 2. Preparar el entorno en Windows

Este procedimiento se realiza una sola vez:

```powershell
py -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
```

No es necesario activar el entorno virtual. Todos los comandos utilizan directamente su intérprete de Python.

## 3. Ejecutar todos los proyectos

Desde la raíz `RegressionTesting`, ejecute:

```powershell
& ".\.venv\Scripts\python.exe" run_all_tests.py
```

El resultado esperado es:

```text
regression-testing:   15 passed
api-testing:           9 passed
performance-testing:   8 passed
security-testing:      9 passed

Todas las suites finalizaron correctamente.
```

En total deben aprobarse **41 pruebas**.

El script ejecuta cada proyecto en un proceso independiente. Esto evita conflictos porque los cuatro proyectos contienen un paquete llamado `app`.

> No ejecute `python -m pytest` directamente desde la raíz. Pytest intentaría importar simultáneamente los cuatro paquetes llamados `app` y podría cargar el módulo incorrecto.

# Ejecución individual de los proyectos

Los siguientes comandos parten de la raíz del repositorio.

## 4. Ejecutar Regression Testing

Ingrese temporalmente al proyecto:

```powershell
Push-Location regression-testing
```

Ejecute todas las pruebas de regresión:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest -v
```

Resultado esperado:

```text
15 passed
```

Ejecute solamente las pruebas de la calculadora:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest tests/test_regression.py -v
```

Ejecute solamente las pruebas del carrito:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest tests/test_carrito_aaa_first.py -v
```

Ejecute una prueba específica:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest `
    "tests/test_regression.py::test_regresion_suma" -v
```

Ejecute las pruebas relacionadas con descuentos:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest -k "descuento" -v
```

Regrese a la raíz:

```powershell
Pop-Location
```

Este proyecto permite trabajar:

- pruebas de regresión;
- patrón Triple AAA;
- principios FIRST;
- aserciones expresivas con PyHamcrest;
- casos normales, límites y excepciones;
- reproducción controlada de un defecto.

La actividad completa está en [`regression-testing/ejercicios/README.md`](regression-testing/ejercicios/README.md).

## 5. Ejecutar API Testing

Ingrese temporalmente al proyecto:

```powershell
Push-Location api-testing
```

Ejecute todas las pruebas de API:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest -v
```

Resultado esperado:

```text
9 passed
```

Ejecute el archivo completo:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest tests/test_api.py -v
```

Ejecute solamente la prueba del recurso inexistente:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest `
    "tests/test_api.py::test_obtener_producto_inexistente" -v
```

Ejecute las pruebas relacionadas con la creación de productos:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest -k "crear_producto" -v
```

Regrese a la raíz:

```powershell
Pop-Location
```

Este proyecto verifica:

- endpoint de disponibilidad;
- códigos HTTP `200`, `201`, `404` y `422`;
- contenido de respuestas JSON;
- consulta de recursos existentes e inexistentes;
- validación de nombres y precios;
- independencia entre pruebas que modifican datos.

### Ejecutar la API manualmente

Desde `api-testing`:

```powershell
Push-Location api-testing

& "..\.venv\Scripts\python.exe" -m uvicorn app.main:app --reload
```

Abra en el navegador:

- Swagger: <http://127.0.0.1:8000/docs>
- Health: <http://127.0.0.1:8000/health>
- Productos: <http://127.0.0.1:8000/productos>

Para detener la API presione `Ctrl + C` y luego ejecute:

```powershell
Pop-Location
```

## 6. Ejecutar Performance Testing

Ingrese temporalmente al proyecto:

```powershell
Push-Location performance-testing
```

Ejecute todas las pruebas:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest -v
```

Resultado esperado:

```text
8 passed
```

Ejecute únicamente las pruebas marcadas como rendimiento:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest -m performance -v
```

Ejecute la prueba que verifica el presupuesto de tiempo:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest `
    "tests/test_performance.py::test_suma_iterativa_cumple_el_presupuesto_educativo" -v
```

Ejecute la comparación entre las dos implementaciones:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest `
    "tests/test_performance.py::test_formula_es_mas_rapida_que_la_iteracion" -v
```

Regrese a la raíz:

```powershell
Pop-Location
```

Este proyecto permite comparar:

- corrección funcional;
- implementación iterativa;
- implementación mediante fórmula;
- presupuesto máximo de ejecución;
- mediana de varias mediciones;
- diferencia entre pruebas funcionales y no funcionales.

El límite de tiempo es intencionalmente amplio para evitar fallos falsos en computadores con diferentes capacidades.

## 7. Ejecutar Security Testing

Ingrese temporalmente al proyecto:

```powershell
Push-Location security-testing
```

Ejecute todas las pruebas:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest -v
```

Resultado esperado:

```text
9 passed
```

Ejecute las pruebas relacionadas con contraseñas:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest -k "password" -v
```

Ejecute las pruebas relacionadas con sanitización:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest -k "sanitizar" -v
```

Ejecute una prueba específica:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest `
    "tests/test_security.py::test_sanitizar_entrada_escapa_etiquetas_html" -v
```

Regrese a la raíz:

```powershell
Pop-Location
```

Este proyecto verifica:

- longitud mínima de contraseña;
- presencia de letras mayúsculas;
- presencia de letras minúsculas;
- presencia de números;
- presencia de caracteres especiales;
- escape de etiquetas HTML;
- escape de comillas y atributos;
- conservación del texto normal.

# Consultar las pruebas disponibles

Para conocer los identificadores de las pruebas de un proyecto, ingrese a su carpeta y ejecute:

```powershell
& "..\.venv\Scripts\python.exe" -m pytest --collect-only -q
```

Ejemplo:

```powershell
Push-Location api-testing
& "..\.venv\Scripts\python.exe" -m pytest --collect-only -q
Pop-Location
```

Pytest identifica cada prueba mediante esta estructura:

```text
tests/archivo.py::nombre_de_la_prueba
```

# Ejecución en Linux o macOS

## Preparación

Desde la raíz:

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
```

## Ejecutar todos los proyectos

```bash
./.venv/bin/python run_all_tests.py
```

## Ejecutar un proyecto individual

Regresión:

```bash
(cd regression-testing && ../.venv/bin/python -m pytest -v)
```

API:

```bash
(cd api-testing && ../.venv/bin/python -m pytest -v)
```

Rendimiento:

```bash
(cd performance-testing && ../.venv/bin/python -m pytest -v)
```

Seguridad:

```bash
(cd security-testing && ../.venv/bin/python -m pytest -v)
```

# Ejecución desde Visual Studio Code

1. Abra la carpeta raíz `RegressionTesting`.
2. Abra una terminal integrada.
3. Cree el entorno e instale las dependencias.
4. Ejecute todos los proyectos con `run_all_tests.py`.
5. Para utilizar el panel **Testing**, configure individualmente la carpeta del proyecto que va a trabajar.

Ejemplo para regresión:

1. Abra el panel **Testing**.
2. Seleccione **Configure Python Tests**.
3. Elija `pytest`.
4. Seleccione `regression-testing`.
5. Configure como intérprete:

```text
RegressionTesting\.venv\Scripts\python.exe
```

No configure simultáneamente las cuatro carpetas en una misma sesión de descubrimiento, porque todas utilizan un paquete llamado `app`.

# Interpretación de resultados

- `PASSED`: el comportamiento cumple el resultado esperado.
- `FAILED`: una aserción no se cumplió.
- `ERROR`: la prueba no pudo ejecutarse por configuración, importaciones o dependencias.
- `SKIPPED`: la prueba fue omitida intencionalmente.
- `XFAIL`: el fallo estaba previsto y documentado.

Cuando una prueba falla, no debe modificarse inmediatamente para conseguir que pase. Primero se debe determinar si el problema está en:

- el código de la aplicación;
- los datos de prueba;
- la configuración;
- la dependencia utilizada;
- el resultado esperado.

# Ruta sugerida para la clase

1. Ejecutar las 41 pruebas y establecer una línea base verde.
2. Trabajar regresión funcional, Triple AAA y principios FIRST.
3. Ejecutar una prueba individual.
4. Revisar contratos y aislamiento del estado en las pruebas de API.
5. Comparar corrección funcional con restricciones de rendimiento.
6. Analizar reglas de contraseña y escape HTML.
7. Introducir un defecto controlado en uno de los proyectos.
8. Ejecutar primero la prueba relacionada.
9. Ejecutar después todas las suites.
10. Restaurar el comportamiento correcto.
11. Confirmar nuevamente las 41 pruebas antes del commit.

# Alcance académico

Los ejemplos son introductorios.

Una restricción de tiempo ejecutada en una sola máquina no reemplaza pruebas profesionales de carga, estrés, capacidad o resistencia con herramientas como Locust, JMeter, k6 o pytest-benchmark.

El escape de texto para HTML no sustituye:

- autenticación;
- autorización;
- consultas parametrizadas;
- gestión de secretos;
- validación del lado del servidor;
- encabezados de seguridad;
- controles específicos del framework;
- pruebas basadas en OWASP.

Los defectos introducidos durante las actividades son temporales y no deben publicarse en el repositorio.