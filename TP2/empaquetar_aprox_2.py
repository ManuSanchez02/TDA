from utils import solucion_valida

def empaquetar_aprox_2(objetos: list):
    objetos_ordenados = sorted(objetos, reverse=True)
    solucion = []
    for objeto in objetos_ordenados:
        for paquete in solucion:
            if solucion_valida(paquete[1] + objeto):
                paquete[0].append(objeto)
                paquete[1] += objeto
                break
        else:
            solucion.append([[objeto], objeto])
    return solucion
