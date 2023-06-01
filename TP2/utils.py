from math import isclose


def solucion_valida(suma_solucion: int) -> bool:
    return suma_solucion <= 1 or isclose(suma_solucion, 1)