from math import isclose
from random import uniform


def solucion_valida(suma_solucion: int) -> bool:
    return suma_solucion <= 1 or isclose(suma_solucion, 1)


def generar_objetos(n: int, n_decimales: int = 3):
    return [round(uniform(0, 1), n_decimales) for _ in range(n)]
