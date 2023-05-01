import random

from utils import random_array


def generar_caso(n):
    mercaderia = {}
    soborno = {}
    optimo = {}

    k = 20

    for i in range(k):
        producto = f"producto{i}"
        paquetes = random_array(n)
        mercaderia[producto] = paquetes

        soborno_elegido = random.sample(paquetes, k=n // 3)
        soborno[producto] = sum(soborno_elegido)
        optimo[producto] = soborno_elegido


main()
