from empaquetar_aprox import empaquetar_aprox
from empaquetar_bt import empaquetar_bt
from utils import generar_objetos

OBJETOS_POR_SIMULACION = 15
SIMULACIONES = 1000

def error_relativo(solucion_optima, solucion_aproximada):
    return abs(solucion_aproximada - solucion_optima) / solucion_optima * 100

def main():
    soluciones_optimas = []
    soluciones_aproximadas = []
    error_relativo_total = 0

    relaciones_total = 0
    for i in range(SIMULACIONES):
        print("Simulacion", i + 1)
        objetos = generar_objetos(OBJETOS_POR_SIMULACION)

        soluciones_aproximadas.append(len(empaquetar_aprox(objetos)))
        print(f"Solucion aproximada: {soluciones_aproximadas[-1]}")

        soluciones_optimas.append(len(empaquetar_bt(objetos)))
        print(f"Solucion optima: {soluciones_optimas[-1]}")

        relaciones_total += soluciones_aproximadas[-1] / soluciones_optimas[-1]

        print("Relacion entre soluciones:", soluciones_aproximadas[-1] / soluciones_optimas[-1])

        suma_total = sum(objetos)

        assert((suma_total / len(objetos)) <= (soluciones_aproximadas[-1] / soluciones_optimas[-1]))


        error_relativo_total += error_relativo(soluciones_optimas[-1], soluciones_aproximadas[-1])
        print(f"Error relativo: {error_relativo(soluciones_optimas[-1], soluciones_aproximadas[-1])}%\n")
    
    print(f"Error relativo promedio: {error_relativo_total / len(soluciones_optimas)}%")
    print(f"Relacion entre aproximacion promedio: {relaciones_total / len(soluciones_optimas)}")

if __name__ == '__main__':
    main()
