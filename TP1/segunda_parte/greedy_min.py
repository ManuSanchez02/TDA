# O(k n log n)
def ordernar_mercaderia(mercaderia):
    return dict(sorted(mercaderia.items(), key=lambda x: x[1][0]))


def es_mejor_solucion(cantidad_paquete, cantidad_ultimo_paquete, cantidad_restante):
    return (
            cantidad_ultimo_paquete < cantidad_paquete <= cantidad_restante + cantidad_ultimo_paquete)


def sobornar_greedy_min(mercaderia, soborno):
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
