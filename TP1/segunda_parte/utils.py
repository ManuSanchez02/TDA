import random


def random_array(n):
    return [random.choice(range(1000)) for _ in range(n)]


def generar_contrabando(n, k):
    mercaderia = {}
    solucion = {}
    soborno = {}

    for j in range(k):
        producto = f"producto{j}"
        paquetes = random_array(n)
        mercaderia[producto] = paquetes

        soborno_elegido = random.sample(paquetes, k=n // 3)
        soborno[producto] = sum(soborno_elegido)
        solucion[producto] = soborno[producto]

    return mercaderia, solucion, soborno
