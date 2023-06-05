from empaquetar_aprox import empaquetar_aprox
from empaquetar_bt import empaquetar_bt
from empaquetar_aprox_2 import empaquetar_aprox_2
from utils import generar_objetos

OBJETOS_POR_SIMULACION = 15
SIMULACIONES = 1000
CONSTANTE_DE_APROXIMACION = 2

def error_relativo(solucion_optima, solucion_aproximada):
    return abs(solucion_aproximada - solucion_optima) / solucion_optima * 100

def empaquetar(objetos, empaquetamiento, soluciones, label):
    soluciones.append(len(empaquetamiento(objetos)))
    print(f"{label}: {soluciones[-1]}")

def calcular_r(solucion_aproximada, solucion_optima, label, relaciones):
    r = solucion_aproximada / solucion_optima
    print(f"{label}: {r}")
    relaciones.append(r)

def imprimir_resultados_r(relaciones, label):
    print(f"Maximo {label}: {max(relaciones)}")
    print(f"Promedio {label}: {sum(relaciones)/len(relaciones)}")

def calcular_error(solucion_optima, solucion_aproximada, label):
    error = error_relativo(solucion_optima, solucion_aproximada)
    print(f"{label}: {error_relativo(solucion_optima, solucion_aproximada)}%")

    return error

def main():
    soluciones_optimas = []
    soluciones_aproximadas = []
    soluciones_aproximadas_2 = []
    
    
    error_relativo_total = 0
    error_relativo_total_2 = 0

    relaciones = []
    relaciones_2 = []
    
    for i in range(SIMULACIONES):
        print("Simulacion", i + 1)
        objetos = generar_objetos(OBJETOS_POR_SIMULACION)

        empaquetar(objetos, empaquetar_aprox, soluciones_aproximadas, "Solucion (aproximada)")
        empaquetar(objetos, empaquetar_bt, soluciones_optimas, "Solucion optima")
        empaquetar(objetos, empaquetar_aprox_2, soluciones_aproximadas_2, "Solucion (aproximada 2)")

        calcular_r(soluciones_aproximadas[-1], soluciones_optimas[-1], "r(A)", relaciones)
        calcular_r(soluciones_aproximadas_2[-1], soluciones_optimas[-1], "r(A2)", relaciones_2)

        assert((soluciones_aproximadas[-1] / soluciones_optimas[-1]) <= CONSTANTE_DE_APROXIMACION)
        assert((soluciones_aproximadas[-1] / soluciones_optimas[-1]) >= 1)

        error_relativo_total += calcular_error(soluciones_optimas[-1], soluciones_aproximadas[-1], "Error relativo (aproximada)")
        error_relativo_total_2 += calcular_error(soluciones_optimas[-1], soluciones_aproximadas_2[-1], "Error relativo (aproximada 2)")
        print()
    
    print("===== Resultados =====")
    print(f"Error relativo promedio (aproximado): {error_relativo_total / len(soluciones_optimas)}%")
    print(f"Error relativo promedio (aproximado 2): {error_relativo_total_2 / len(soluciones_optimas)}%")
    imprimir_resultados_r(relaciones, "r(A)")
    imprimir_resultados_r(relaciones_2, "r(A2)")


if __name__ == '__main__':
    main()
