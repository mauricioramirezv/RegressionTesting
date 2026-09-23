import pytest
from hamcrest import assert_that, equal_to

from app.calculadora import dividir, modulo, multiplicar, potencia, restar, sumar


def test_regresion_suma():
    # Arrange
    a = 2
    b = 3

    # Act
    resultado = sumar(a, b)

    # Assert
    assert_that(resultado, equal_to(5))


def test_regresion_resta():
    # Arrange
    a = 10
    b = 4

    # Act
    resultado = restar(a, b)

    # Assert
    assert_that(resultado, equal_to(6))


def test_regresion_multiplicacion():
    # Arrange
    a = 4
    b = 5

    # Act
    resultado = multiplicar(a, b)

    # Assert
    assert_that(resultado, equal_to(20))


def test_regresion_division():
    # Arrange
    dividendo = 20
    divisor = 4

    # Act
    resultado = dividir(dividendo, divisor)

    # Assert
    assert_that(resultado, equal_to(5))


def test_regresion_modulo():
    # Arrange
    dividendo = 10
    divisor = 3

    # Act
    resultado = modulo(dividendo, divisor)

    # Assert
    assert_that(resultado, equal_to(1))


def test_regresion_potencia():
    # Arrange
    base = 2
    exponente = 3

    # Act
    resultado = potencia(base, exponente)

    # Assert
    assert_that(resultado, equal_to(8))


def test_regresion_division_por_cero():
    # Arrange
    dividendo = 8
    divisor = 0

    # Act y Assert
    with pytest.raises(ValueError, match="No se puede dividir entre cero"):
        dividir(dividendo, divisor)
