import sys
import time
from math import inf, isclose
import copy

BT_FLAG = 'E'
APROX_FLAG = 'A'
GREEDY_FLAG = 'A2'

def empaquetar_bt_con_paquetes(objetos: list, solucion_parcial: list = []) -> list:
    solucion = None
    if len(objetos) == 0: return solucion_parcial

    objeto = objetos.pop()
    for paquete in solucion_parcial:
        if sum(paquete) + objeto <= 1:
            paquete.append(objeto)
            solucion_actual = empaquetar_bt(objetos, solucion_parcial)
            if not solucion or len(solucion_actual) < len(solucion):
                solucion = copy.deepcopy(solucion_actual)
            paquete.pop()

    solucion_parcial.append([objeto])
    solucion_actual = empaquetar_bt(objetos, solucion_parcial)
    if not solucion or len(solucion_actual) < len(solucion):
        solucion = copy.deepcopy(solucion_actual)
    solucion_parcial.pop()
    objetos.append(objeto)

    return solucion

def empaquetar_bt(objetos: list, solucion_parcial: list = [], mejor_solucion: int = inf) -> int:
    if len(objetos) == 0: 
        return len(solucion_parcial)


    objeto = objetos.pop()
    for paquete in solucion_parcial:
        if  paquete[1] + objeto <= 1 or isclose(paquete[1] + objeto, 1):
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


def empaquetar_aprox(objetos: list, n: int = 1):
    solucion = [2, 3]

    return solucion


def empaquetar_greedy(objetos: list, n: int = 1):
    solucion = [5, 6, 7]

    return solucion


empaquetar_dict = {
    BT_FLAG: empaquetar_bt,
    APROX_FLAG: empaquetar_aprox,
    GREEDY_FLAG: empaquetar_greedy
}


def main():
    argumentos = sys.argv[1:]

    if len(argumentos) != 2:
        raise ValueError("Cantidad de parametros erronea")

    flags, ruta_datos = argumentos

    flags = flags.split('|')

    objetos = []
    with open(ruta_datos) as archivo:
        objetos.extend([float(linea.rstrip()) for linea in archivo.readlines()[2:]])

    start_time = time.time()
    paquetes_por_metodo = [str(empaquetar_dict[flag](objetos)) for flag in flags]
    end_time = time.time()

    print(f"{'|'.join(paquetes_por_metodo)}: #Envases")
    print(f"Tiempo de ejecucion: {(end_time - start_time) * 1000}")


if __name__ == '__main__':
    objetos = [0.4, 0.8, 0.5, 0.1, 0.7, 0.6, 0.1, 0.4, 0.2, 0.2]
    solucion = empaquetar_bt(objetos)

    main()
    print(solucion)
