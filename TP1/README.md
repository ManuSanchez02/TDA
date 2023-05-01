# Trabajo Práctico 1

## Integrantes:

| Nombre         | Padrón | Email               |
| -------------- | ------ | ------------------- |
| Manuel Sanchez | 107951 | msanchezf@fi.uba.ar |
| Ian Shih       | 108349 | ishih@fi.uba.ar     |

## Primera parte

### "El algoritmo que usa heaps"

#### Descripcion

"El algoritmo que usa heaps" es un algoritmo que permite hacer un _merge_ de $k$ arreglos haciendo uso de un _min-heap_.
Para ello, sigue los siguientes pasos:

1. Insertar el primer elemento de cada arreglo en el heap. Es importante mantener un registro de a que arreglo
   pertenecia dicho elemento.
2. Extraer la raiz del heap e insertarla en un arreglo.
3. Extraer otro elemento del arreglo al que pertenecía la raiz antes de ser insertada al heap.
4. Insertar este nuevo elemento al heap.
5. Repetir desde el paso 2 hasta que no queden mas elementos en ningun arreglo.

#### Complejidad

En nuestra implementacion, dicho algoritmo esta compuesto por:

- `initialize_heap`: Esta funcion se encarga de recorrer todos los arreglos e insertar el primer elemento de cada uno de
  ellos en una lista, lo cual tiene una complejidad temporal de O(k). Luego, a esta lista se le hace _heapify_ para
  transformarla en un _min-heap_, lo cual tiene la misma complejidad temporal, O(k). Por ello, esta funcion tiene una
  complejidad temporal de O(k)
- `push_next`: Esta funcion inserta el siguiente elemento del arreglo donde se encontraba la raiz del heap previa a ser
  insertada al mismo. Si este arreglo no tiene mas elementos, inserta infinito en el heap, de forma que este se hunda
  hacia el fondo del todo. Insertar un elemento a un heap, usando `heapq.heappush` tiene una complejidad de O(log k).
- `HeapElement`: Todos los metodos de esta clase tienen una complejidad de O(1).
- `kmerge`: Esta es la funcion principal que se encarga de combinar multiples arreglos. Primero, llama
  a `initialize_heap` que tiene una complejidad O(k). Luego entra en un `while` que itera mientras la longitud del
  arreglo resultado sea menor a la cantidad total de elementos, es decir, $k*h$ veces que es igual a $N$ veces. Dentro
  del `while`, se realizan 3 operaciones:

    - Se extrae la raiz del heap (valor minimo) usando `heapq.heappop`, el cual tiene una complejidad de O(log k).
    - Se inserta un nuevo elemento al heap usando `push_next`, el cual tiene una complejidad de O(log k).
    - Se concatena el valor minimo al arreglo de resultado, lo cual tiene una complejidad de O(1).

  En total, la complejidad obtenida dentro del `while` es O(log k), y repitiendolo $k*h$ veces, resulta en una
  complejidad de O(k h \* log k).

## Segunda parte: Problema del contrabando

### Greedy

El algoritmo greedy hace los siguientes pasos:

1. Ordenar de mayor a menor los paquetes de cada producto de la mercaderia
2. Por cada producto de la mercaderia
    1. Tomar un paquete y fijarse si alcanza para pagar todo el soborno
        1. Si alcanza, me lo guardo como optimo local
        2. Si no alcanza, lo agrego a la solucion
3. Repetir 1 hasta que haber pagado todo el soborno

El algoritmo es unicamente capaz de optimizar el ultimo paquete de cada producto. Si un paquete no alcanza para pagar el
soborno, se agrega a la solucion y se pasa al siguiente paquete. Es decir, cuando no alcanza, siempre toma el mas
grande. Esta es la parte donde falla y no es optimo. Sin embargo, por esta misma razon es lo que lo hace greedy, la
solucion mas "voraz" siempre va a ser la que reduzca el soborno lo mas "rapido" posible

### Programacion dinamica

#### Descripcion general

Analizando el problema detalladamente, nos damos cuenta que es similar al problema de la mochila, aunque a diferencia de
la mochila, tenemos mas de una "mochila" y no tenemos la posibilidad de dejarle menos unidades de los que nos pide el
funcionario, tenemos que darle mas o la misma cantidad. Con estas consideraciones, diseñamos el siguiente algoritmo:

1. Por cada producto:
    1. Creamos una matriz de soluciones, donde las filas son los paquetes y las columnas son los valores del soborno
       para cada subproblema
    2. Iteramos cada celda de la matriz, llenando cada una con la solucion al subproblema, tomando la siguiente decision
        1. Buscamos la cantidad de productos que **minimice** la diferencia entre la cantidad y el soborno
        2. Se elige entre el subproblema de no usar el paquete actual y el subproblema de usarlo pero considerando un
           soborno menor y un paquete menos
    3. Se reconstruye la solucion a partir de la matriz generada

### Complejidad

Se establecen las siguientes variables:

* `n`: Cantidad **maxima** de paquetes por producto
* `k`: Cantidad de productos
* `s`: Soborno **maximo** pedido

#### Greedy

Para el algoritmo greedy, ordenamos los paquetes de mayor a menor por cada producto e iteramos los paquetes de cada
producto.

Ordenar los paquetes de cada producto cuesta `O(n log n)`, resultando en que la funcion `ordernar_mercaderia`
cueste `O(k * n log n)`

Iterar los paquetes de cada producto cuesta `O(k * n)` debido a que las instrucciones ejecutadas en el ciclo se hacen en
tiempo constante

Esto resulta en un algoritmo con complejidad total de `T(n, s, k) = O(k * n log n) + O(k * n) = O(k * n log n)`

#### Dinamica

Por **cada producto**, construimos una matriz de `s` columnas y `n` filas, la iteramos y luego reconstruimos la solucion
en base a la matriz.

Construir una matriz `s` * `n` cuesta `O(s*n)` lo mismo es iterarlo (todas las instrucciones se ejecutan en tiempo
constante)

Reconstruir la solucion tiene una complejidad de `O(n)` debido al ciclo de 1 hasta n+1

El algoritmo para calcular los paquetes optimos para **un producto** resulta
en `T(n, s) = O(s * n) + O(s * n) + O(n) = O (s * n)`

Esto resulta en un algoritmo con complejidad total de `T(n, s, k) = O(k * s * n)`

### Deficiencias de algoritmo greedy

Como se menciono anteriormente, al solo ser capaz de optimizar el **ultimo** paquete, en casos donde la solucion
optima **no** tiene en cuenta el paquete de mayor siempre va a fallar el algoritmo greedy

Ejemplo:

Cuando tengo los siguientes paquetes `[8, 6, 5]` y se pide un soborno de 11 unidades, nuestro algoritmo
devolvera `[8, 5]`
porque siempre se tiene en cuenta el mas grande

### Generacion de tests de volumen

Para la generacion de tests de volumen, se establece un `k` y un `n`, por cada `k` se crea un producto y se genera un
arreglo aleatorio de tamaño `n`, de ese arreglo se selecciona `n // 3` elementos que va ser nuestro soborno para ese
producto. El resultado correcto sera el resultado donde la suma de las cantidades de los paquetes sea igual al soborno
determinado para el producto, sabemos que siempre se encontrara el optimo porque el soborno se elige del mismo arreglo.