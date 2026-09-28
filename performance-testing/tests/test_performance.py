from statistics import median
from time import perf_counter
from timeit import repeat

import pytest

from app.procesamiento import suma_lenta, suma_rapida


@pytest.mark.parametrize("n", [0, 1, 10, 100_000])
def test_implementaciones_producen_el_resultado_correcto(n):
    esperado = sum(range(n))

    assert suma_lenta(n) == esperado
    assert suma_rapida(n) == esperado


@pytest.mark.parametrize("funcion", [suma_lenta, suma_rapida])
def test_entrada_negativa_es_rechazada(funcion):
    with pytest.raises(ValueError, match="mayor o igual que cero"):
        funcion(-1)


@pytest.mark.performance
def test_suma_iterativa_cumple_el_presupuesto_educativo():
    inicio = perf_counter()
    resultado = suma_lenta(250_000)
    duracion = perf_counter() - inicio

    assert resultado == sum(range(250_000))
    assert duracion < 0.5, f"La operación tardó {duracion:.6f} segundos"


@pytest.mark.performance
def test_formula_es_mas_rapida_que_la_iteracion():
    n = 250_000
    tiempos_iterativos = repeat(lambda: suma_lenta(n), number=1, repeat=5)
    tiempos_formula = repeat(lambda: suma_rapida(n), number=1, repeat=5)

    assert median(tiempos_formula) < median(tiempos_iterativos)
