SIN_SOLUCION = -1


def imprimir_matriz(matriz):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matriz]))


def soluciones_subproblemas(mercaderia, soborno_deseado):
    n = len(mercaderia)
    soluciones = [[SIN_SOLUCION for _ in range(soborno_deseado + 1)] for _ in range(n + 1)]
    soluciones[0][0] = 0
    for i in range(1, n + 1):
        paquete = mercaderia[i - 1]
        for soborno_subproblema in range(soborno_deseado + 1):
            aproximacion_sin = soluciones[i - 1][soborno_subproblema]
            solucion_subproblema_con = soluciones[i - 1][max(soborno_subproblema - paquete, 0)]
            aproximacion_con = solucion_subproblema_con + paquete
            cantidades_posibles = [aproximacion_sin, aproximacion_con] if solucion_subproblema_con != SIN_SOLUCION else [aproximacion_sin]

            if all([aprox < soborno_subproblema for aprox in cantidades_posibles]):
                continue
            cantidades_validas = [cantidad for cantidad in cantidades_posibles if cantidad >= soborno_subproblema]
            if cantidades_validas:
                soluciones[i][soborno_subproblema] = min(cantidades_validas, key=lambda x: abs(x - soborno_subproblema))

    return soluciones


def reconstruir_solucion(mercaderia, soborno_deseado, matriz_soluciones):
    n = len(mercaderia)
    aproximacion_mas_cercana = matriz_soluciones[n][soborno_deseado]
    if aproximacion_mas_cercana < 0: raise Exception("No hay solucion posible")
    solucion = []

    for i in range(1, n + 1):
        cantidad_actual = mercaderia[n - i]
        if matriz_soluciones[n - i][
            max(soborno_deseado - cantidad_actual, 0)] == aproximacion_mas_cercana - cantidad_actual:
            solucion.append(cantidad_actual)
            soborno_deseado -= cantidad_actual
            aproximacion_mas_cercana -= cantidad_actual

    return solucion


# Suponiendo:
# n = cantidad maxima de paquetes por producto
# k = cantidad de productos
def sobornar_dinamico(mercaderia, soborno):
    solucion = {}
    # O(k)
    for producto, cantidad in soborno.items():
        matriz_soluciones = soluciones_subproblemas(mercaderia[producto], cantidad)
        solucion[producto] = reconstruir_solucion(mercaderia[producto], cantidad, matriz_soluciones)
    return solucion
