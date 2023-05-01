import csv
import json
import os
import random

from dinamica import sobornar_dinamico
from greedy import sobornar_greedy
from utils import random_array

random.seed(100)

DEFAULT_DATASET_PATH = 'dataset.csv'


def calcular_error(sobornar, mercaderia, solucion, soborno):
    error = 0

    resultado = sobornar(mercaderia, soborno)

    for producto, paquetes in resultado.items():
        error += (sum(paquetes) - solucion[producto]) / solucion[producto] * 100

    return error / len(resultado)


def comparar_algoritmos(mercaderias, soluciones, sobornos):
    for i in range(len(mercaderias)):
        mercaderia = mercaderias[i]
        solucion = soluciones[i]
        soborno = sobornos[i]

        print(f"Simulacion nro {i + 1}")

        print(f"Error de greedy: {calcular_error(sobornar_greedy, mercaderia, solucion, soborno)}%")
        print(f"Error de dinamica: {calcular_error(sobornar_dinamico, mercaderia, solucion, soborno)}%")


def guardar_set_datos(mercaderias, sobornos, soluciones):
    with open(DEFAULT_DATASET_PATH, 'w') as archivo:
        archivo.write("mercaderia;soborno;solucion\n")
        for i in range(len(mercaderias)):
            mercaderia = json.dumps(mercaderias[i])
            soborno = json.dumps(sobornos[i])
            solucion = json.dumps(soluciones[i])

            archivo.write(f"{mercaderia};{soborno};{solucion}\n")


def leer_set_datos(path):
    mercaderias = []
    soluciones = []
    sobornos = []
    with open(path, 'r') as archivo:
        reader = csv.DictReader(archivo, delimiter=';')
        for linea in reader:
            for atributo, valor in linea.items():
                linea[atributo] = json.loads(valor)

            mercaderias.append(linea['mercaderia'])
            soluciones.append(linea['soborno'])
            sobornos.append(linea['solucion'])
    return mercaderias, soluciones, sobornos


def generar_set_de_datos(n, k, iteraciones):
    mercaderias = []
    sobornos = []
    soluciones = []

    for i in range(iteraciones):
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

        mercaderias.append(mercaderia)
        sobornos.append(soborno)
        soluciones.append(solucion)

    return mercaderias, sobornos, soluciones


def main():
    if not os.path.exists(DEFAULT_DATASET_PATH):
        mercaderias, soluciones, sobornos = generar_set_de_datos(30, 20, 20)
        guardar_set_datos(mercaderias, soluciones, sobornos)

    mercaderias, soluciones, sobornos = leer_set_datos(DEFAULT_DATASET_PATH)

    comparar_algoritmos(mercaderias, soluciones, sobornos)


main()
