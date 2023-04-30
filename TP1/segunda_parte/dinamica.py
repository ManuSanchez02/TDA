def distancia(valor1, valor2):
    return abs(valor1 - valor2)


def imprimir_matriz(matriz):
    print('\n'.join([''.join(['{:4}'.format(item)
          for item in row]) for row in matriz]))


def sobornar_dinamico_recursivo(valores, n, valor_total):
    if n < 0:
        return 0
    aproximacion_sin = sobornar_dinamico_recursivo(valores, n-1, valor_total)
    aproximacion_con = sobornar_dinamico_recursivo(
        valores, n-1, valor_total-valores[n]) + valores[n]
    if distancia(aproximacion_sin, valor_total) < distancia(aproximacion_con, valor_total):
        return aproximacion_sin
    else:
        return aproximacion_con


def sobornar_dinamico_iterativo(valores, valor_total):
    n = len(valores)
    m = [[-1 for _ in range(valor_total+1)] for _ in range(n+1)]
    m[0][0] = 0
    for i in range(1, n+1):
        valor_actual = valores[i-1]
        for j in range(valor_total+1):
            aproximacion_sin = m[i-1][j]
            aproximacion_con = m[i-1][max(j-valor_actual, 0)]+valor_actual
            if aproximacion_sin < j and aproximacion_con < j:
                continue
            elif aproximacion_sin > j and aproximacion_con < j:
                m[i][j] = aproximacion_sin
            elif aproximacion_sin < j and aproximacion_con > j:
                m[i][j] = aproximacion_con
            elif distancia(aproximacion_sin, valor_total) < distancia(aproximacion_con, valor_total):
                m[i][j] = aproximacion_sin
            else:
                m[i][j] = aproximacion_con

    return m, m[n][valor_total]


def reconstruir_solucion(valores, input_original, valor_total, m):
    if valor_total < 0:
        raise Exception("No hay solucion posible")

    n = len(valores)
    solucion = []
    for i in range(1, n+1):
        valor_actual = valores[n-i]
        if valor_total == valor_actual:
            solucion.append(valor_actual)
            valor_total = 0
        elif (m[n-i][input_original-valor_actual] == valor_total-valor_actual):
            solucion.append(valor_actual)
            input_original -= valor_actual
            valor_total -= valor_actual

    return solucion


def sobornar_dinamico(mercaderia, soborno):
    solucion = {}
    for producto, cantidad in soborno.items():
        matriz_soluciones, aproximacion_mas_cercana = sobornar_dinamico_iterativo(mercaderia[producto], cantidad)
        imprimir_matriz(matriz_soluciones)
        solucion[producto] = reconstruir_solucion(mercaderia[producto], cantidad, aproximacion_mas_cercana, matriz_soluciones)
    return solucion


mercaderia = {
    'Cigarrillo': [8, 5],
    'Vodka': [5]
}

soborno_2 = {
    "Cigarrillo": 13,
    "Vodka": 1
}

print(sobornar_dinamico(mercaderia, soborno_2))
