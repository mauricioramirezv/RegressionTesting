def suma_lenta(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser mayor o igual que cero")
    total = 0
    for i in range(n):
        total += i
    return total


def suma_rapida(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser mayor o igual que cero")
    return n * (n - 1) // 2
