![](https://i.imgur.com/P0aqOMI.jpg)

# Trabajo Práctico 1

## Integrantes:

| Nombre         | Padrón | Email               |
| -------------- | ------ | ------------------- |
| Manuel Sanchez | 107951 | msanchezf@fi.uba.ar |
| Ian Shih       | 108349 | ishih@fi.uba.ar     |

### Clase de complejidad
Vamos a considerar el problema de empaquetamiento como un problema de decision. Es decir, dada una lista de objetos, se busca responder la siguiente pregunta: "¿Se puede empaquetar dichos objetos usando a lo sumo $k$ envases de tamaño 1?".

Para demostrar que un problema es NP-Completo se deben cumplir 2 condiciones:

Dado un problema $X$:
* Una solucion al problema $X$ se puede verificar en tiempo polinomial.
* Otro problema $Y$ NP-Completo se puede reducir al problema $X$, de forma que $X \ge_p Y$. Es decir, resolver $X$ es al menos tan dificil como resolver $Y$.

Analicemos si una solucion a nuestro problema se puede verificar en tiempo polinomial. Como entrada, esperamos recibir una lista de paquetes, y un valor $k$ que representa la cantidad de paquetes. Para saber si una solucion es valida, lo primero que verificamos es que la suma de objetos de cada paquete no supere 1. Una vez verificado esto, nos fijamos si la cantidad de paquetes es menor o igual a $k$. En codigo seria asi:

```py
for paquete in paquetes:
  if sum(paquete) > 1:
    return False

return len(paquetes) <= k
```

Todas estas operaciones se pueden hacer en tiempo polinomial. Consecuentemente, se cumple la primera condicion de un problema NP-Completo

### Complejidad temporal
Con el fin de simplificar el analisis, consideraremos a nuestro algoritmo como si fuera un algoritmo de _fuerza bruta_, es decir, que no realiza ningun tipo de poda del arbol de llamados recursivos con el fin de acelerar la velocidad de ejecucion. La complejidad real del algoritmo va a ser similar a la obtenida gracias al analisis (mas/menos ciertas constantes).

Para simplificar el analisis, podemos asumir que el algoritmo de fuerza bruta crea $n$ paquetes, $n$ siendo la cantidad de objetos a empaquetar. Esto se puede hacer debido a que una de las soluciones a la que va a llegar fuerza bruta, sera la solucion donde cada paquete tendra un solo objeto.

Cada vez que tengamos que agregar un nuevo objeto a un paquete, nuestro algoritmo prueba si el objeto se puede colocar en cada uno de mis n paquetes, a la vez, probamos si el resto de los paquetes agregados, se pueden distribuir a otros paquetes

