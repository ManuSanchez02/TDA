from utils import solucion_valida
from math import inf

def empaquetar_bt(objetos: list, solucion_parcial: list = [], mejor_solucion: int = inf) -> int:
    if len(objetos) == 0: 
        return len(solucion_parcial)


    objeto = objetos.pop()
    for paquete in solucion_parcial:
        if  solucion_valida(paquete[1] + objeto):
            paquete[0].append(objeto)
            paquete[1] += objeto
            solucion_actual = empaquetar_bt(objetos, solucion_parcial, mejor_solucion)
            mejor_solucion = min(solucion_actual, mejor_solucion)
            paquete[1] -= objeto
            paquete[0].pop()

    if len(solucion_parcial) + 1 >= mejor_solucion: 
        objetos.append(objeto)
        return mejor_solucion

    solucion_parcial.append([[objeto], objeto])
    solucion_actual = empaquetar_bt(objetos, solucion_parcial, mejor_solucion)
    mejor_solucion = min(solucion_actual, mejor_solucion)
    solucion_parcial.pop()
    objetos.append(objeto)

    return mejor_solucion