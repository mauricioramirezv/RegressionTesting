"""Ejecuta cada módulo en un proceso aislado para evitar colisiones de `app`."""

from pathlib import Path
import subprocess
import sys


MODULOS = (
    "regression-testing",
    "api-testing",
    "performance-testing",
    "security-testing",
)


def main() -> int:
    raiz = Path(__file__).resolve().parent
    fallidos: list[str] = []

    for modulo in MODULOS:
        print(f"\n{'=' * 70}\nEjecutando {modulo}\n{'=' * 70}", flush=True)
        resultado = subprocess.run(
            [sys.executable, "-m", "pytest", "-q"],
            cwd=raiz / modulo,
            check=False,
        )
        if resultado.returncode != 0:
            fallidos.append(modulo)

    if fallidos:
        print("\nMódulos con errores: " + ", ".join(fallidos))
        return 1

    print("\nTodas las suites finalizaron correctamente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
