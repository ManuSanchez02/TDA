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

            if distancia(aproximacion_sin, valor_total) < distancia(aproximacion_con, valor_total):
                m[i][j] = aproximacion_sin
            else:
                m[i][j] = aproximacion_con

    return m, m[n][valor_total]


def reconstruir_solucion(valores, input_original, valor_total, m):
    n = len(valores)
    solucion = []
    for i in range(1, n+1):
        valor_actual = valores[n-i]

        if (m[n-i][input_original-valor_actual] == valor_total-valor_actual):
            solucion.append(valor_actual)
            input_original -= valor_actual
            valor_total -= valor_actual
        elif valor_total == valor_actual:
            solucion.append(valor_actual)
            valor_total = 0

    return solucion


def sobornar_dinamico(valores, valor_total):
    m, aproximacion_mas_cercana = sobornar_dinamico_iterativo(
        valores, valor_total)
    imprimir_matriz(m)
    return reconstruir_solucion(valores, valor_total, aproximacion_mas_cercana, m)


items = [5, 8, 9, 6, 2]
solucion = sobornar_dinamico(items, 23)
print(solucion)
print(sum(solucion))
