from utils import solucion_valida


def empaquetar_aprox(objetos: list):
    paquetes = []
    paquete_actual = [[], 0]
    for objeto in objetos:
        if solucion_valida(paquete_actual[1] + objeto):
            paquete_actual[0].append(objeto)
            paquete_actual[1] += objeto
        else:
            paquetes.append(paquete_actual)
            paquete_actual = [[objeto], objeto]

    paquetes.append(paquete_actual)

    return paquetes
