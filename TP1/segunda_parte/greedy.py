# O(k n log n)
def ordernar_mercaderia(mercaderia):
    return dict(sorted(mercaderia.items(), key=lambda x: x[1][0], reverse=True))


# Suponiendo:
# Cantidad maxima de paquetes: n
# Cantidad de productos: k

# 1. Tomar un producto de la mercaderia y fijarse si me alcanza para pagar todo el soborno
#     1.1. Si me alcanza, me lo guardo como optimo local
#     1.2. Si no me alcanza, lo agrego a la solucion
# 2. Repetir 1 hasta que haber pagado todo el soborno
# El algoritmo es unicamente capaz de optimizar el ultimo paquete de cada producto.
# Si un paquete no alcanza para pagar el soborno, se agrega a la solucion y se pasa al siguiente paquete. 
# Es decir, cuando no alcanza, siempre toma el mas grande. Esta es la parte donde falla y no es optimo.

def es_mejor_solucion(cantidad_paquete, cantidad_ultimo_paquete, cantidad_restante):
    return (cantidad_paquete < cantidad_ultimo_paquete and cantidad_paquete >= cantidad_restante+cantidad_ultimo_paquete)


def sobornar_greedy(mercaderia, soborno):
    mercaderia = ordernar_mercaderia(mercaderia)
    mejor_soborno = {}

    for producto_pedido, cantidad_paquete in soborno.items():
        cantidad_restante = cantidad_paquete
        mejor_soborno[producto_pedido] = []
        cantidad_ultimo_paquete = None
        for cantidad_paquete in mercaderia[producto_pedido]:

            if cantidad_paquete < cantidad_restante:
                mejor_soborno[producto_pedido].append(cantidad_paquete)
                cantidad_restante -= cantidad_paquete
                continue

            if not cantidad_ultimo_paquete:
                cantidad_restante -= cantidad_paquete
                cantidad_ultimo_paquete = cantidad_paquete
            elif es_mejor_solucion(cantidad_paquete, cantidad_ultimo_paquete, cantidad_restante):
                cantidad_restante += cantidad_ultimo_paquete - cantidad_paquete
                cantidad_ultimo_paquete = cantidad_paquete

        mejor_soborno[producto_pedido].append(cantidad_ultimo_paquete)

    return mejor_soborno


mercaderia = {
    'Cigarrillo': [8, 5],
    'Vodka': [5]
}
mercaderia2 = {
    'Cigarrillo': [8, 5, 3]
}

soborno_1 = {
    "Cigarrillo": 6
}
soborno_2 = {
    "Cigarrillo": 10
}
soborno_3 = {
    "Cigarrillo": 1,
    "Vodka": 1
}
soborno_4 = {
    "Cigarrillo": 11,
}

soborno_5 = {
    "Cigarrillo": 3,
}

sol_1 = {
    'Cigarrillo': [8]
}
sol_2 = {
    'Cigarrillo': [8, 5]
}
sol_3 = {
    'Cigarrillo': [5],
    'Vodka': [5]
}
sol_4 = {
    'Cigarrillo': [8, 3]
}
sol_5 = {
    'Cigarrillo': [3]
}

assert sobornar_greedy(mercaderia, soborno_1) == sol_1
assert sobornar_greedy(mercaderia, soborno_2) == sol_2
assert sobornar_greedy(mercaderia, soborno_3) == sol_3
assert sobornar_greedy(mercaderia2, soborno_4) == sol_4
assert sobornar_greedy(mercaderia2, soborno_5) == sol_5
print("Todo OK")
