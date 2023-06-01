import sys
import time
from empaquetar_aprox import empaquetar_aprox

from empaquetar_bt import empaquetar_bt
from empaquetar_greedy import empaquetar_greedy

BT_FLAG = 'E'
APROX_FLAG = 'A'
GREEDY_FLAG = 'A2'


# def empaquetar_bt_con_paquetes(objetos: list, solucion_parcial: list = []) -> list:
#     solucion = None
#     if len(objetos) == 0: return solucion_parcial

#     objeto = objetos.pop()
#     for paquete in solucion_parcial:
#         if sum(paquete) + objeto <= 1:
#             paquete.append(objeto)
#             solucion_actual = empaquetar_bt(objetos, solucion_parcial)
#             if not solucion or len(solucion_actual) < len(solucion):
#                 solucion = copy.deepcopy(solucion_actual)
#             paquete.pop()

#     solucion_parcial.append([objeto])
#     solucion_actual = empaquetar_bt(objetos, solucion_parcial)
#     if not solucion or len(solucion_actual) < len(solucion):
#         solucion = copy.deepcopy(solucion_actual)
#     solucion_parcial.pop()
#     objetos.append(objeto)

#     return solucion

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
