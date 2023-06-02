from empaquetar_aprox import empaquetar_aprox
from empaquetar_bt import empaquetar_bt
from random import uniform

def generar_objetos(n):
    return [round(uniform(0, 1), 3) for _ in range(n)]

def error_relativo(solucion_optima, solucion_aproximada):
    return abs(solucion_aproximada - solucion_optima) / solucion_optima * 100

def main():
    soluciones_optimas = []
    soluciones_aproximadas = []
    error_relativo_total = 0
    for i in range(500):
        print("Simulacion", i + 1)
        objetos = generar_objetos(15)

        soluciones_aproximadas.append(empaquetar_aprox(objetos))
        print(f"Solucion aproximada: {soluciones_aproximadas[-1]}")

        soluciones_optimas.append(empaquetar_bt(objetos))
        print(f"Solucion optima: {soluciones_optimas[-1]}")

        error_relativo_total += error_relativo(soluciones_optimas[-1], soluciones_aproximadas[-1])
        print(f"Error relativo: {error_relativo(soluciones_optimas[-1], soluciones_aproximadas[-1])}%\n")
    
    print(f"Error relativo promedio: {error_relativo_total / len(soluciones_optimas)}%")

if __name__ == '__main__':
    main()
