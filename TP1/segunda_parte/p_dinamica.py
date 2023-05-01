# Supuestos
# n = cantidad maxima de paquetes por producto
# k = cantidad de productos
# s = soborno pedido por producto

def _reconstruir_sol(productos, matriz, i, j):
    if i <= 0 or j <= 0:
        return []

    val_actual = matriz[i][j]
    if val_actual == matriz[i - 1][j]:
        return _reconstruir_sol(productos, matriz, i - 1, j)
    else:
        return [productos[i - 1]] + _reconstruir_sol(productos, matriz, i - 1, j - productos[i - 1])


# O(n): Por cada paso de la recursion se decrece la cantidad de paquetes utilizados por la solucion hasta llegar a 0
def reconstruir_sol(productos, matriz):
    return _reconstruir_sol(productos, matriz, len(matriz) - 1, len(matriz[0]) - 1)


def sobornar_producto(mercaderia, soborno_pedido):
    # O(n)
    matriz = [[] for _ in range(len(mercaderia))]

    # O(n)
    matriz.insert(0, [0] * (soborno_pedido + 1))

    # O(n)
    for i in range(1, len(matriz)):
        # O(s)
        for j in range(len(matriz[0])):
            # O(1)
            valor_sin_elemento = matriz[i - 1][j]
            valor_con_elemento = mercaderia[i - 1] + matriz[i - 1][max(j - mercaderia[i - 1], 0)]

            dif_sin = valor_sin_elemento - j
            dif_con = valor_con_elemento - j

            if dif_sin < 0 and dif_con < 0:
                matriz[i].append(0)

            valores = [valor_sin_elemento, valor_con_elemento]
            valores_validos = [v for v in valores if v - j >= 0]
            if valores_validos:
                min_val = min(valores_validos, key=lambda x: abs(x - j))
                matriz[i].append(min_val)
    return matriz


def imprimir_matriz(matriz):
    print('\n'.join([''.join(['{:4}'.format(item)
                              for item in row]) for row in matriz]))


# O(k * n * s)
def sobornar(mercaderia, soborno):
    res = {}

    # O(k)
    for producto, cantidad in soborno.items():
        # O(n * s)
        matriz = sobornar_producto(mercaderia[producto], cantidad)

        # O(n)
        res[producto] = reconstruir_sol(mercaderia[producto], matriz)

    return res
