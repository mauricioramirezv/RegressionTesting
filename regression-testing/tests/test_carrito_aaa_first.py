import pytest
from hamcrest import assert_that, contains_exactly, equal_to, has_length, is_

from app.carrito import Carrito


def test_total_sin_descuento_sigue_siendo_el_subtotal():
    # Arrange: datos locales y controlados para mantener la independencia.
    carrito = Carrito()
    carrito.agregar_producto("Teclado", 120_000, 1)
    carrito.agregar_producto("Mouse", 80_000, 2)

    # Act: una sola operación principal.
    total = carrito.total_con_descuento(0)

    # Assert: la prueba se valida automáticamente.
    assert_that(total, equal_to(280_000))


def test_total_con_descuento_del_diez_por_ciento():
    # Arrange
    carrito = Carrito()
    carrito.agregar_producto("Monitor", 500_000, 2)

    # Act
    total = carrito.total_con_descuento(10)

    # Assert
    assert_that(total, equal_to(900_000))


def test_productos_conservan_el_orden_de_ingreso():
    # Arrange
    carrito = Carrito()
    carrito.agregar_producto("Teclado", 120_000)
    carrito.agregar_producto("Mouse", 80_000)

    # Act
    nombres = carrito.nombres_productos()

    # Assert: aserciones expresivas sobre una colección.
    assert_that(nombres, has_length(2))
    assert_that(nombres, contains_exactly("Teclado", "Mouse"))


@pytest.mark.parametrize("porcentaje", [-1, 101])
def test_descuento_fuera_del_rango_es_rechazado(porcentaje):
    # Arrange
    carrito = Carrito()
    carrito.agregar_producto("Teclado", 120_000)

    # Act y Assert
    with pytest.raises(ValueError, match="entre 0 y 100"):
        carrito.total_con_descuento(porcentaje)


@pytest.mark.parametrize(
    ("porcentaje", "esperado"),
    [(0, 100_000), (25, 75_000), (100, 0)],
)
def test_descuentos_limite_son_repetibles(porcentaje, esperado):
    # Arrange
    carrito = Carrito()
    carrito.agregar_producto("Producto", 100_000)

    # Act
    total = carrito.total_con_descuento(porcentaje)

    # Assert
    assert_that(total, is_(esperado))
