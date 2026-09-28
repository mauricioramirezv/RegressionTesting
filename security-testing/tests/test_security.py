import pytest

from app.validaciones import sanitizar_entrada, validar_password_segura


def test_password_segura_valida():
    assert validar_password_segura("Segura123!") is True


@pytest.mark.parametrize(
    "password",
    [
        "Ab1!",
        "segura123!",
        "SEGURA123!",
        "SeguraABC!",
        "Segura1234",
    ],
    ids=["corta", "sin-mayuscula", "sin-minuscula", "sin-digito", "sin-especial"],
)
def test_password_insegura_es_rechazada(password):
    assert validar_password_segura(password) is False


def test_sanitizar_entrada_escapa_etiquetas_html():
    texto = "<script>alert('x')</script>"

    resultado = sanitizar_entrada(texto)

    assert resultado == "&lt;script&gt;alert(&#x27;x&#x27;)&lt;/script&gt;"
    assert "<script>" not in resultado


def test_sanitizar_entrada_escapa_atributos_con_comillas():
    texto = '<img src="x" onerror="alert(1)">'

    resultado = sanitizar_entrada(texto)

    assert "&quot;" in resultado
    assert "<img" not in resultado


def test_sanitizar_entrada_conserva_texto_normal():
    assert sanitizar_entrada("  Hola, mundo  ") == "Hola, mundo"
