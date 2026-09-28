from html import escape
import re


def validar_password_segura(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


def sanitizar_entrada(texto: str) -> str:
    """Escapa texto para mostrarlo en contenido HTML, no para otros contextos."""
    return escape(texto.strip(), quote=True)
