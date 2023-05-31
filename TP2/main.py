import sys
import time

BT_FLAG = 'E'
APROX_FLAG = 'A'
GREEDY_FLAG = 'A2'


def empaquetar_bt(objetos: list, n: int = 1):
    solucion = [1]

    return solucion


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

    paquetes = []
    with open(ruta_datos) as archivo:
        paquetes.extend([float(linea.rstrip()) for linea in archivo.readlines()[2:]])

    start_time = time.time()
    cant_paq_x_met = [str(len(empaquetar_dict[flag](paquetes))) for flag in flags]
    end_time = time.time()

    print(f"{'|'.join(cant_paq_x_met)}: #Envases")
    print(f"Tiempo de ejecucion: {(end_time - start_time) * 1000}")


if __name__ == '__main__':
    objetos = [0.4, 0.2, 0.5, 0.3, 0.7, 0.6, 0.1, 0.4, 0.2, 0.2]
    solucion = empaquetar_bt(objetos)

    main()
    print(solucion)
