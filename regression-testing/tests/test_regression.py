from hamcrest import assert_that, equal_to
import pytest
from app.calculadora import sumar, restar, multiplicar, dividir, modulo, potencia

def test_regresion_suma():
    # Arrange
    a = 2
    b = 3
    # Act
    resultado = sumar(a, b)
    # Assert
    assert_that(resultado, equal_to(5))

def test_regresion_resta():
    resultado = restar(10, 4)
    assert_that(resultado, equal_to(6))

def test_regresion_multiplicacion():
    resultado = multiplicar(4, 5)
    assert_that(resultado, equal_to(20))

def test_regresion_division():
    resultado = dividir(20, 4)
    assert_that(resultado, equal_to(5))

def test_regresion_modulo():
    resultado = modulo(10, 3)
    assert_that(resultado, equal_to(1))

def test_regresion_potencia():
    resultado = potencia(2, 3)
    assert_that(resultado, equal_to(8))

def test_regresion_division_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir entre cero"):
        dividir(8, 0)
