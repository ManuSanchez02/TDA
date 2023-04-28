# Trabajo Práctico 1
## Integrantes:

| Nombre         | Padrón | Email               |
| -------------- | ------ | ------------------- |
| Manuel Sanchez | 107951 | msanchezf@fi.uba.ar |
| Ian Shih       | 108349 | ishih@fi.uba.ar     |

## Primera parte

### "El algoritmo que usa heaps"

#### Descripcion

"El algoritmo que usa heaps" es un algoritmo que permite hacer un _merge_ de $k$ arreglos haciendo uso de un _min-heap_. Para ello, sigue los siguientes pasos:

1. Insertar el primer elemento de cada arreglo en el heap. Es importante mantener un registro de a que arreglo pertenecia dicho elemento.
2. Extraer la raiz del heap e insertarla en un arreglo.
3. Extraer otro elemento del arreglo al que pertenecía la raiz antes de ser insertada al heap.
4. Insertar este nuevo elemento al heap.
5. Repetir desde el paso 2 hasta que no queden mas elementos en ningun arreglo.

#### Complejidad

En nuestra implementacion, dicho algoritmo esta compuesto por:

- `initialize_heap`: Esta funcion se encarga de recorrer todos los arreglos e insertar el primer elemento de cada uno de ellos en una lista, lo cual tiene una complejidad temporal de O(k). Luego, a esta lista se le hace _heapify_ para transformarla en un _min-heap_, lo cual tiene la misma complejidad temporal, O(k). Por ello, esta funcion tiene una complejidad temporal de O(k)
- `push_next`: Esta funcion inserta el siguiente elemento del arreglo donde se encontraba la raiz del heap previa a ser insertada al mismo. Si este arreglo no tiene mas elementos, inserta infinito en el heap, de forma que este se hunda hacia el fondo del todo. Insertar un elemento a un heap, usando `heapq.heappush` tiene una complejidad de O(log k).
- `HeapElement`: Todos los metodos de esta clase tienen una complejidad de O(1).
- `kmerge`: Esta es la funcion principal que se encarga de combinar multiples arreglos. Primero, llama a `initialize_heap` que tiene una complejidad O(k). Luego entra en un `while` que itera mientras la longitud del arreglo resultado sea menor a la cantidad total de elementos, es decir, $k*h$ veces que es igual a $N$ veces. Dentro del `while`, se realizan 3 operaciones:

  - Se extrae la raiz del heap (valor minimo) usando `heapq.heappop`, el cual tiene una complejidad de O(log k).
  - Se inserta un nuevo elemento al heap usando `push_next`, el cual tiene una complejidad de O(log k).
  - Se concatena el valor minimo al arreglo de resultado, lo cual tiene una complejidad de O(1).

  En total, la complejidad obtenida dentro del `while` es O(log k), y repitiendolo $k*h$ veces, resulta en una complejidad de O(k h \* log k).

## Segunda parte
