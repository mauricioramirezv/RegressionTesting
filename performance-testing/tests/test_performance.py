import time
from app.procesamiento import suma_lenta

def test_rendimiento_suma_lenta():
    inicio = time.perf_counter()
    resultado = suma_lenta(100000)
    fin = time.perf_counter()
    duracion = fin - inicio

    assert resultado == sum(range(100000))
    assert duracion < 1.0
