class Carrito:
    """Carrito pequeño para practicar regresión, AAA y FIRST."""

    def __init__(self) -> None:
        self._productos: list[tuple[str, float, int]] = []

    def agregar_producto(self, nombre: str, precio: float, cantidad: int = 1) -> None:
        if not nombre.strip():
            raise ValueError("El nombre es obligatorio")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        self._productos.append((nombre.strip(), precio, cantidad))

    def subtotal(self) -> float:
        return round(sum(precio * cantidad for _, precio, cantidad in self._productos), 2)

    def total_con_descuento(self, porcentaje: float) -> float:
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")
        return round(self.subtotal() * (1 - porcentaje / 100), 2)

    def nombres_productos(self) -> list[str]:
        return [nombre for nombre, _, _ in self._productos]
