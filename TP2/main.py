import sys
import time
from empaquetar_aprox import empaquetar_aprox
from empaquetar_bt import empaquetar_bt
from empaquetar_aprox_2 import empaquetar_aprox_2

BT_FLAG = 'E'
APROX_FLAG = 'A'
GREEDY_FLAG = 'A2'

empaquetar_dict = {
    BT_FLAG: empaquetar_bt,
    APROX_FLAG: empaquetar_aprox,
    GREEDY_FLAG: empaquetar_aprox_2
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
    paquetes_por_metodo = [str(len(empaquetar_dict[flag](objetos))) for flag in flags]
    end_time = time.time()

    print(f"{'|'.join(paquetes_por_metodo)}: #Envases")
    print(f"Tiempo de ejecucion: {(end_time - start_time) * 1000}")


if __name__ == '__main__':
    main()
    