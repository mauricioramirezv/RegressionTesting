from app.validaciones import validar_password_segura, sanitizar_entrada

def test_password_segura_valida():
    resultado = validar_password_segura("Segura123!")
    assert resultado is True

def test_password_insegura_muy_corta():
    assert validar_password_segura("Ab1!") is False

def test_password_insegura_sin_mayuscula():
    assert validar_password_segura("segura123!") is False

def test_sanitizar_entrada_html():
    texto = "<script>alert('x')</script>"
    resultado = sanitizar_entrada(texto)
    assert "<" not in resultado
    assert ">" not in resultado
