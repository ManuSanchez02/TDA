from utils import solucion_valida


def empaquetar_aprox(objetos: list):
    paquetes = []
    paquete_actual = []
    for objeto in objetos:
        if solucion_valida(sum(paquete_actual) + objeto):
            paquete_actual.append(objeto)
        else:
            paquetes.append(paquete_actual)
            paquete_actual = [objeto]

    return paquetes

