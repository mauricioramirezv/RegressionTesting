# Pruebas básicas de seguridad

Este módulo muestra cómo convertir reglas de seguridad sencillas en pruebas de
regresión. Incluye una política educativa de contraseñas y escape de contenido
que será mostrado como texto dentro de HTML.

## Aspectos verificados

- longitud mínima de contraseña;
- presencia de mayúscula, minúscula, dígito y carácter especial;
- escape de etiquetas, comillas y atributos HTML;
- conservación y limpieza de texto normal.

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

Solo las pruebas de contraseñas:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest -k "password" -v
```

Una prueba individual:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest `
    "tests/test_security.py::test_sanitizar_entrada_escapa_etiquetas_html" -v
```

El resultado esperado es `9 passed`.

## Límite de la sanitización

`sanitizar_entrada` escapa texto para insertarlo en contenido HTML. Este control
depende del contexto: no protege consultas SQL, comandos del sistema, URLs,
JavaScript, CSS ni atributos construidos manualmente. En aplicaciones reales se
deben utilizar el autoescape del framework, consultas parametrizadas, políticas
de autorización y controles específicos para cada contexto.
