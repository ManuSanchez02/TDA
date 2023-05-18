import csv
import json
import os
import random

from dinamica import sobornar_dinamico
from greedy import sobornar_greedy
from utils import generar_contrabando

random.seed(100)

DEFAULT_DATASET_PATH = 'dataset.csv'


def calcular_error(sobornar, mercaderia, solucion, soborno):
    error = 0

    resultado = sobornar(mercaderia, soborno)

    for producto, paquetes in resultado.items():
        error += (sum(paquetes) - solucion[producto]) / solucion[producto] * 100

    return error / len(resultado)


def comparar_algoritmos(mercaderias, soluciones, sobornos):
    errores_greedy = []
    errores_dinamica = []
    for i in range(len(mercaderias)):
        mercaderia = mercaderias[i]
        solucion = soluciones[i]
        soborno = sobornos[i]
        error_greedy = calcular_error(sobornar_greedy, mercaderia, solucion, soborno)
        error_dinamica = calcular_error(sobornar_dinamico, mercaderia, solucion, soborno)
        errores_greedy.append(error_greedy)
        errores_dinamica.append(error_dinamica)

        print(f"Simulacion nro {i + 1}")
        print(f"Error de greedy: {error_greedy}%")
        print(f"Error de dinamica: {error_dinamica}%")

    error_promedio_greedy = sum(errores_greedy) / len(errores_greedy)
    error_promedio_dinamica = sum(errores_dinamica) / len(errores_dinamica)

    print("\n----Simulacion finalizada----")
    print(f"Promedio de error greedy: {error_promedio_greedy}%")
    print(f"Promedio de error dinamica: {error_promedio_dinamica}%")


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
        mercaderia, soborno, solucion = generar_contrabando(n, k)

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
