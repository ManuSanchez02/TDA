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
    return (
            cantidad_paquete < cantidad_ultimo_paquete and cantidad_paquete >= cantidad_restante + cantidad_ultimo_paquete)


def sobornar_greedy(mercaderia, soborno):
    # O(k n log n)
    mercaderia = ordernar_mercaderia(mercaderia)
    mejor_soborno = {}

    # O (k)
    for producto_pedido, cantidad_paquete in soborno.items():
        cantidad_restante = cantidad_paquete
        mejor_soborno[producto_pedido] = []
        cantidad_ultimo_paquete = None
        # O(n)
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
