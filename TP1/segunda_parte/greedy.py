mercaderia = {
    'Cigarrillo': [8, 5],
    'Vodka': [5]
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
    "Vodka": 1
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

# O(k n log n)
def ordernar_mercaderia(mercaderia):
    return dict(sorted(mercaderia.items(), key=lambda x: x[1][0], reverse=True))


# Suponiendo: 
# Cantidad maxima de paquetes: n
# Cantidad de productos: k

def sobornar_greedy(mercaderia, soborno):
    mejor_soborno = {}
    
    # O(k n log n)
    mercaderia_ordenada = ordernar_mercaderia(mercaderia)

    # O(k)
    for producto_pedido, cantidad_pedida in soborno.items():
        cantidad_pedida_actual = cantidad_pedida

        # O(n)
        for cantidad in mercaderia_ordenada[producto_pedido]:
            mejor_soborno[producto_pedido] = mejor_soborno.get(producto_pedido, [])

            if cantidad_pedida_actual > 0:
                mejor_soborno[producto_pedido].append(cantidad)
                cantidad_pedida_actual -= cantidad

    return mejor_soborno
        

assert sobornar_greedy(mercaderia, soborno_1) == sol_1
assert sobornar_greedy(mercaderia, soborno_2) == sol_2
assert sobornar_greedy(mercaderia, soborno_3) != sol_3