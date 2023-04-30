def distancia(valor1, valor2):
    return abs(valor1 - valor2)


def sobornar_dinamico(valores, n, valor_total):
    if n < 0:
        return 0
    aproximacion_sin = sobornar_dinamico(valores, n-1, valor_total)
    aproximacion_con = sobornar_dinamico(
        valores, n-1, valor_total-valores[n]) + valores[n]
    if distancia(aproximacion_sin, valor_total) < distancia(aproximacion_con, valor_total):
        return aproximacion_sin
    else:
        return aproximacion_con


def sobornar(valores, valor_total):
    n = len(valores)
    m = [[-1 for _ in range(valor_total+1)] for _ in range(n+1)]
    m[0][0] = 0
    for i in range(1, n+1):
        valor_actual = valores[i-1]
        for j in range(valor_total+1):
            # if m[i][j-valor_actual]+valor_actual > j:
            #     m[i][j] = m[i-1][j]
            # else:
            #     m[i][j] = max(m[i-1][j-valor_actual]+valor_actual, m[i-1][j])
            # if m[i-1][j] == -1 and m[i-1][j-valor_actual] +  == -1:
            #     m[i][j] = -1
            
            aproximacion_sin = m[i-1][j]
            aproximacion_con = m[i-1][0]+valor_actual if j < valor_actual else m[i-1][j-valor_actual]+valor_actual
            if aproximacion_sin < j and aproximacion_con < j:
                m[i][j] = -1
                continue
            
            if distancia(aproximacion_sin, valor_total) < distancia(aproximacion_con, valor_total):
                m[i][j] = aproximacion_sin
            else:
                m[i][j] = aproximacion_con

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in m]))
    return m, m[n][valor_total]

def reconstruir_solucion(valores, input_original, valor_total, m):
    n = len(valores)
    solucion = []
    for i in range(1,n+1):
        valor_actual = valores[n-i]

        if (m[n-i][input_original-valor_actual] == valor_total-valor_actual):
            solucion.append(valor_actual)
            input_original -= valor_actual
            valor_total -= valor_actual
        elif valor_total == valor_actual:
            solucion.append(valor_actual)
            valor_total = 0
        
    return solucion


items = [5, 8, 9, 6, 2]
V = 23
solucion = []
m, valor_total = sobornar(items, V)
solucion = reconstruir_solucion(items, V, valor_total, m)
print(solucion)
print(sum(solucion))